"""
Button Components - Styled and positioned buttons
Extracted from SEDO TSS Converter app.py lines 311-315
"""

import streamlit as st
from typing import Optional, Literal
from ..theme import ThemeConfig


def centered_button(label: str,
                   key: Optional[str] = None,
                   button_type: Literal["primary", "secondary"] = "primary",
                   use_container_width: bool = True,
                   theme: Optional[ThemeConfig] = None) -> bool:
    """
    Render a centered button using 3-column layout

    Args:
        label: Button label text
        key: Optional unique key for the button
        button_type: Button type - "primary" or "secondary"
        use_container_width: If True, button fills container width
        theme: Optional ThemeConfig instance

    Returns:
        True if button was clicked, False otherwise

    Example:
        if centered_button("🚀 Start Processing"):
            # Button was clicked
            st.write("Processing...")
    """
    # Create 3-column layout with centered button
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        st.markdown('<div style="display: flex; justify-content: center;">',
                   unsafe_allow_html=True)
        clicked = st.button(
            label,
            key=key,
            type=button_type,
            use_container_width=use_container_width
        )
        st.markdown('</div>', unsafe_allow_html=True)

    return clicked


def action_button(label: str,
                 key: Optional[str] = None,
                 button_type: Literal["primary", "secondary"] = "primary",
                 disabled: bool = False,
                 help_text: Optional[str] = None) -> bool:
    """
    Render a standard action button

    Args:
        label: Button label text
        key: Optional unique key for the button
        button_type: Button type - "primary" or "secondary"
        disabled: If True, button is disabled
        help_text: Optional help/tooltip text

    Returns:
        True if button was clicked, False otherwise

    Example:
        if action_button("Download", help_text="Download processed file"):
            # Button was clicked
            download_file()
    """
    return st.button(
        label,
        key=key,
        type=button_type,
        disabled=disabled,
        help=help_text
    )


class ButtonGroup:
    """
    Group of buttons with consistent styling

    Useful for creating action button groups with themed appearance.
    """

    def __init__(self, theme: Optional[ThemeConfig] = None):
        """
        Initialize ButtonGroup

        Args:
            theme: ThemeConfig instance. If None, uses default theme.
        """
        self.theme = theme if theme else ThemeConfig.default()

    def render_horizontal(self,
                         buttons: list[dict],
                         centered: bool = False) -> dict:
        """
        Render buttons horizontally in columns

        Args:
            buttons: List of button configs, each with keys:
                    - label: Button label
                    - key: Button key
                    - type: "primary" or "secondary"
                    - disabled: Optional bool
            centered: If True, center the button group

        Returns:
            Dictionary mapping button keys to clicked state

        Example:
            group = ButtonGroup()
            clicked = group.render_horizontal([
                {"label": "Save", "key": "save", "type": "primary"},
                {"label": "Cancel", "key": "cancel", "type": "secondary"},
            ], centered=True)

            if clicked.get("save"):
                # Save button clicked
                pass
        """
        num_buttons = len(buttons)
        clicks = {}

        if centered:
            # Add padding columns for centering
            cols = st.columns([1] + [1] * num_buttons + [1])
            start_idx = 1
        else:
            cols = st.columns(num_buttons)
            start_idx = 0

        for i, btn_config in enumerate(buttons):
            with cols[start_idx + i]:
                clicked = st.button(
                    btn_config.get("label", "Button"),
                    key=btn_config.get("key"),
                    type=btn_config.get("type", "secondary"),
                    disabled=btn_config.get("disabled", False),
                    use_container_width=True
                )
                clicks[btn_config.get("key")] = clicked

        return clicks
