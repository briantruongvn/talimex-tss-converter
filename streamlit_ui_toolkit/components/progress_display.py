"""
ProgressDisplay Component - Multi-step progress tracking with visual feedback
Extracted from SEDO TSS Converter app.py lines 261-274
"""

import streamlit as st
from typing import Optional
from ..theme import ThemeConfig


class ProgressDisplay:
    """
    Multi-step progress indicator with visual feedback

    Displays a progress bar and step indicator with numbered badges.
    """

    def __init__(self,
                 total_steps: int,
                 theme: Optional[ThemeConfig] = None):
        """
        Initialize ProgressDisplay

        Args:
            total_steps: Total number of steps in the process
            theme: ThemeConfig instance. If None, uses default theme.
        """
        self.total_steps = total_steps
        self.theme = theme if theme else ThemeConfig.default()
        self.current_step = 0

    def update(self,
               current: int,
               status: str,
               description: Optional[str] = None,
               progress_placeholder: Optional[st.delta_generator.DeltaGenerator] = None,
               status_placeholder: Optional[st.delta_generator.DeltaGenerator] = None) -> None:
        """
        Update progress display

        Args:
            current: Current step number (1-indexed)
            status: Status message for current step
            description: Optional detailed description
            progress_placeholder: Optional Streamlit placeholder for progress bar
            status_placeholder: Optional Streamlit placeholder for status

        Example:
            progress = ProgressDisplay(total_steps=5)

            for step in range(1, 6):
                progress.update(step, f"Processing step {step}")
                time.sleep(1)
        """
        self.current_step = current
        progress = current / self.total_steps

        # Get theme colors
        colors = self.theme.colors

        # Determine step badge color
        if current >= self.total_steps:
            badge_color = colors.get("success", "#10b981")
        else:
            badge_color = colors.get("warning", "#f59e0b")

        # Update progress bar
        if progress_placeholder:
            with progress_placeholder.container():
                st.progress(progress)
        else:
            st.progress(progress)

        # Build status HTML
        status_html = f"""
        <div style="
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
            color: {colors.get('text_tertiary', '#374151')};
        ">
            <div style="
                background: {badge_color};
                color: {colors.get('white', '#ffffff')};
                width: 24px;
                height: 24px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 0.75rem;
                font-weight: 500;
            ">{current}</div>
            <span><strong>{status}</strong></span>
        </div>
        """

        # Update status
        if status_placeholder:
            with status_placeholder.container():
                st.markdown(status_html, unsafe_allow_html=True)
                if description:
                    st.caption(description)
        else:
            st.markdown(status_html, unsafe_allow_html=True)
            if description:
                st.caption(description)

    def create_placeholders(self) -> tuple:
        """
        Create Streamlit placeholders for progress and status

        Returns:
            Tuple of (progress_placeholder, status_placeholder)

        Example:
            progress = ProgressDisplay(total_steps=5)
            prog_ph, status_ph = progress.create_placeholders()

            for step in range(1, 6):
                progress.update(step, f"Step {step}",
                               progress_placeholder=prog_ph,
                               status_placeholder=status_ph)
        """
        progress_placeholder = st.empty()
        status_placeholder = st.empty()
        return progress_placeholder, status_placeholder

    def complete(self, message: str = "Process completed!") -> None:
        """
        Display completion message

        Args:
            message: Completion message
        """
        from .message_box import MessageBox
        MessageBox(self.theme).success(message)
