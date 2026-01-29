"""
FileUploader Component - Styled file upload with validation
Extracted from SEDO TSS Converter app.py lines 197-202, 283-288
"""

import streamlit as st
from typing import Optional, List, Any
from ..theme import ThemeConfig


class FileUploader:
    """
    Enhanced file uploader with styled section and validation

    Provides a visually styled upload area with file type and size validation.
    """

    def __init__(self,
                 max_size_mb: int = 200,
                 allowed_types: Optional[List[str]] = None,
                 theme: Optional[ThemeConfig] = None):
        """
        Initialize FileUploader

        Args:
            max_size_mb: Maximum file size in megabytes
            allowed_types: List of allowed file extensions (e.g., ['xlsx', 'xls', 'csv'])
                          If None, defaults to ['xlsx', 'xls', 'xlsm']
            theme: ThemeConfig instance. If None, uses default theme.
        """
        self.max_size_mb = max_size_mb
        self.allowed_types = allowed_types if allowed_types else ['xlsx', 'xls', 'xlsm']
        self.theme = theme if theme else ThemeConfig.default()

    def render(self,
               title: str = "Upload File",
               subtitle: str = "Select file to process",
               help_text: Optional[str] = None,
               key: Optional[str] = None) -> Optional[Any]:
        """
        Render file uploader with styled section

        Args:
            title: Upload section title
            subtitle: Upload section subtitle
            help_text: Optional help text for file uploader
            key: Optional key for the file uploader widget

        Returns:
            Uploaded file object or None if no file selected/validation fails

        Example:
            uploader = FileUploader(max_size_mb=100, allowed_types=['xlsx', 'csv'])
            file = uploader.render("Upload Excel File", "Drag and drop or browse")

            if file:
                # Process file
                pass
        """
        # Get theme colors
        colors = self.theme.colors

        # Render styled upload section
        st.markdown(f"""
        <div style="
            background: {colors.get('upload_bg', '#fafafa')};
            border: 1px dashed {colors.get('border_dashed', '#d1d5db')};
            border-radius: {self.theme.border_radius};
            padding: 2rem 1rem;
            text-align: center;
            margin: 1rem 0;
        ">
            <div style="
                font-size: 1.2rem;
                font-weight: 500;
                color: {colors.get('text_tertiary', '#374151')};
                margin-bottom: 0.5rem;
            ">{title}</div>
            <div style="
                color: {colors.get('text_secondary', '#6b7280')};
                font-size: 0.9rem;
                margin-bottom: 1rem;
            ">{subtitle}</div>
        </div>
        """, unsafe_allow_html=True)

        # Build help text
        if help_text is None:
            extensions = ', '.join(self.allowed_types).upper()
            help_text = f"Drag and drop file here\nLimit {self.max_size_mb}MB per file • {extensions}"

        # Render Streamlit file uploader
        uploaded_file = st.file_uploader(
            "",
            type=self.allowed_types,
            help=help_text,
            label_visibility="collapsed",
            key=key
        )

        # Validate file if uploaded
        if uploaded_file:
            # Check file size
            file_size_mb = uploaded_file.size / (1024 * 1024)
            if file_size_mb > self.max_size_mb:
                from .message_box import MessageBox
                MessageBox(self.theme).error(
                    f"File too large: {file_size_mb:.1f}MB. Maximum size: {self.max_size_mb}MB",
                    title="File Size Error"
                )
                return None

        return uploaded_file

    def validate_file(self, uploaded_file) -> tuple[bool, str]:
        """
        Validate uploaded file

        Args:
            uploaded_file: File object from st.file_uploader

        Returns:
            Tuple of (is_valid: bool, message: str)
        """
        if not uploaded_file:
            return False, "No file uploaded"

        # Check file extension
        file_ext = uploaded_file.name.split('.')[-1].lower()
        if file_ext not in self.allowed_types:
            return False, f"Invalid file type: .{file_ext}. Allowed: {', '.join(self.allowed_types)}"

        # Check file size
        file_size_mb = uploaded_file.size / (1024 * 1024)
        if file_size_mb > self.max_size_mb:
            return False, f"File too large: {file_size_mb:.1f}MB. Maximum: {self.max_size_mb}MB"

        return True, "File valid"
