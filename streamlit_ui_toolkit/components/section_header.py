"""
SectionHeader Component - Styled section headers
Extracted from SEDO TSS Converter app.py lines 182-202
"""

import streamlit as st
from typing import Optional
from ..theme import ThemeConfig


class SectionHeader:
    """
    Styled section header component

    Displays a title and optional subtitle with themed styling.
    """

    def __init__(self, theme: Optional[ThemeConfig] = None):
        """
        Initialize SectionHeader

        Args:
            theme: ThemeConfig instance. If None, uses default theme.
        """
        self.theme = theme if theme else ThemeConfig.default()

    def render(self,
               title: str,
               subtitle: Optional[str] = None,
               centered: bool = True) -> None:
        """
        Render section header

        Args:
            title: Header title text
            subtitle: Optional subtitle text
            centered: If True, center-align the header

        Example:
            header = SectionHeader()
            header.render("SEDO Internal TSS Converter",
                         "Convert SEDO Internal TSS to Standard Internal TSS")
        """
        colors = self.theme.colors
        text_align = "center" if centered else "left"

        subtitle_html = ""
        if subtitle:
            subtitle_html = f"""
            <div style="
                font-size: 1rem;
                color: {colors.get('text_secondary', '#6b7280')};
                font-weight: 400;
                margin-top: 0.5rem;
            ">{subtitle}</div>
            """

        html = f"""
        <div style="
            text-align: {text_align};
            padding: 0.5rem 0 1rem 0;
            margin-bottom: 1rem;
        ">
            <div style="
                font-size: 3rem;
                font-weight: 600;
                color: {colors.get('text_primary', '#1f2937')};
                margin-bottom: 0.5rem;
            ">{title}</div>
            {subtitle_html}
        </div>
        """

        st.markdown(html, unsafe_allow_html=True)


def render_section_header(title: str,
                          subtitle: Optional[str] = None,
                          centered: bool = True,
                          theme: Optional[ThemeConfig] = None) -> None:
    """
    Convenience function to render section header

    Args:
        title: Header title text
        subtitle: Optional subtitle text
        centered: If True, center-align the header
        theme: Optional ThemeConfig instance

    Example:
        render_section_header("My App", "Welcome to my application")
    """
    header = SectionHeader(theme)
    header.render(title, subtitle, centered)
