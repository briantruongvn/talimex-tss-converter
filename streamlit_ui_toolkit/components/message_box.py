"""
MessageBox Component - Styled success/error/warning messages
Extracted from SEDO TSS Converter app.py lines 303-339
"""

import streamlit as st
from typing import Optional, Literal
from ..theme import ThemeConfig


MessageType = Literal["success", "error", "warning", "info"]


class MessageBox:
    """
    Styled message box component for displaying alerts and notifications

    Supports success, error, warning, and info message types with themed styling.
    """

    def __init__(self, theme: Optional[ThemeConfig] = None):
        """
        Initialize MessageBox with theme

        Args:
            theme: ThemeConfig instance. If None, uses default theme.
        """
        self.theme = theme if theme else ThemeConfig.default()

    def render(self,
               message: str,
               message_type: MessageType = "info",
               title: Optional[str] = None) -> None:
        """
        Render a styled message box

        Args:
            message: Message content (supports markdown)
            message_type: Type of message - "success", "error", "warning", or "info"
            title: Optional title text (will be bolded)

        Example:
            msg = MessageBox()
            msg.render("File uploaded successfully!", "success", title="Success")
            msg.render("Missing required field", "error", title="Validation Error")
            msg.render("Large file detected", "warning")
        """
        # Get theme colors
        colors = self.theme.colors

        # Define message box styles
        styles = {
            "success": {
                "bg": colors.get("success_bg", "#f0fdf4"),
                "border": colors.get("success_border", "#bbf7d0"),
                "text": colors.get("success_text", "#166534"),
                "icon": "✅"
            },
            "error": {
                "bg": colors.get("error_bg", "#fef2f2"),
                "border": colors.get("error_border", "#fecaca"),
                "text": colors.get("error", "#dc2626"),
                "icon": "❌"
            },
            "warning": {
                "bg": "#fffbeb",
                "border": "#fde68a",
                "text": "#d97706",
                "icon": "⚠️"
            },
            "info": {
                "bg": "#eff6ff",
                "border": "#bfdbfe",
                "text": "#1e40af",
                "icon": "ℹ️"
            }
        }

        style = styles.get(message_type, styles["info"])

        # Build title HTML
        if title:
            title_html = f"<strong>{style['icon']} {title}</strong><br>"
        else:
            title_html = f"{style['icon']} "

        # Render message box
        st.markdown(f"""
        <div style="
            background: {style['bg']};
            border: 1px solid {style['border']};
            border-radius: {self.theme.border_radius};
            padding: {self.theme.spacing_unit};
            color: {style['text']};
            margin: {self.theme.spacing_unit} 0;
        ">
            {title_html}{message}
        </div>
        """, unsafe_allow_html=True)

    def success(self, message: str, title: Optional[str] = None) -> None:
        """Render success message box"""
        self.render(message, "success", title)

    def error(self, message: str, title: Optional[str] = None) -> None:
        """Render error message box"""
        self.render(message, "error", title)

    def warning(self, message: str, title: Optional[str] = None) -> None:
        """Render warning message box"""
        self.render(message, "warning", title)

    def info(self, message: str, title: Optional[str] = None) -> None:
        """Render info message box"""
        self.render(message, "info", title)
