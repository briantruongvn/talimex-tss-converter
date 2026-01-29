"""
Streamlit UI Toolkit

Reusable Streamlit components and templates extracted from SEDO TSS Converter.

Main modules:
- theme: Theme management (colors, fonts, CSS)
- components: UI components (MessageBox, FileUploader, ProgressDisplay, etc.)
- templates: Excel template system (ColumnConfig, TemplateConfig, ExcelTemplateBuilder)

Quick Start:
    import streamlit as st
    from streamlit_ui_toolkit.theme import ThemeConfig
    from streamlit_ui_toolkit.components import MessageBox, FileUploader
    from streamlit_ui_toolkit.templates import get_tss_17column_template, ExcelTemplateBuilder

    # Apply theme
    theme = ThemeConfig.default()
    theme.apply()

    # Use components
    uploader = FileUploader(theme=theme)
    file = uploader.render("Upload File", "Select Excel file")

    if file:
        MessageBox(theme).success("File uploaded!")

        # Create template
        template = get_tss_17column_template()
        builder = ExcelTemplateBuilder(template)
        output = builder.create_workbook("output.xlsx")
"""

from .version import __version__, __author__, __description__

# Import main modules
from . import theme
from . import components
from . import templates

# Import commonly used classes
from .theme import ThemeConfig
from .components import (
    MessageBox,
    FileUploader,
    ProgressDisplay,
    SectionHeader,
    render_section_header,
    centered_button,
    action_button,
    ButtonGroup,
)
from .templates import (
    ColumnConfig,
    TemplateConfig,
    ExcelTemplateBuilder,
    get_tss_17column_template,
    get_simple_template,
)

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__description__",
    # Modules
    "theme",
    "components",
    "templates",
    # Theme
    "ThemeConfig",
    # Components
    "MessageBox",
    "FileUploader",
    "ProgressDisplay",
    "SectionHeader",
    "render_section_header",
    "centered_button",
    "action_button",
    "ButtonGroup",
    # Templates
    "ColumnConfig",
    "TemplateConfig",
    "ExcelTemplateBuilder",
    "get_tss_17column_template",
    "get_simple_template",
]
