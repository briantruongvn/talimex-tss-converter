"""
Template Presets - Pre-defined template configurations
Extracted from SEDO TSS Converter step3_template_creation.py lines 65-83
"""

from .schema import TemplateConfig, ColumnConfig


def get_tss_17column_template() -> TemplateConfig:
    """
    Get TSS 17-column template configuration

    This is the standard SEDO Internal TSS template with 17 columns (A-Q):
    - Column A: Combination (Yellow)
    - Columns B-G: Materials (Red background, white text)
    - Columns H-K: Regulations (Blue background, white text)
    - Columns L-Q: Testing (Green background, black text)
    - Column O: Level (Blue background, white text)

    Returns:
        TemplateConfig for TSS 17-column template

    Example:
        from streamlit_ui_toolkit.templates import get_tss_17column_template, ExcelTemplateBuilder

        template = get_tss_17column_template()
        builder = ExcelTemplateBuilder(template)
        builder.create_workbook("tss_template.xlsx")
    """
    columns = [
        ColumnConfig(
            name="Combination",
            bg_color="00FFFF00",
            font_color="00000000",
            width=15.0
        ),
        ColumnConfig(
            name="General Type Component(Type)",
            bg_color="00FF0000",
            font_color="00FFFFFF",
            width=20.0
        ),
        ColumnConfig(
            name="Sub-Type Component Identity Process Name",
            bg_color="00FF0000",
            font_color="00FFFFFF",
            width=25.0
        ),
        ColumnConfig(
            name="Material Designation",
            bg_color="00FF0000",
            font_color="00FFFFFF",
            width=18.0
        ),
        ColumnConfig(
            name="Material Distributor",
            bg_color="00FF0000",
            font_color="00FFFFFF",
            width=15.0
        ),
        ColumnConfig(
            name="Producer",
            bg_color="00FF0000",
            font_color="00FFFFFF",
            width=12.0
        ),
        ColumnConfig(
            name="Material Type In Process",
            bg_color="00FF0000",
            font_color="00FFFFFF",
            width=20.0
        ),
        ColumnConfig(
            name="Document type",
            bg_color="000000FF",
            font_color="00FFFFFF",
            width=15.0
        ),
        ColumnConfig(
            name="Requirement Source/TED",
            bg_color="000000FF",
            font_color="00FFFFFF",
            width=20.0
        ),
        ColumnConfig(
            name="Sub-type",
            bg_color="000000FF",
            font_color="00FFFFFF",
            width=12.0
        ),
        ColumnConfig(
            name="Regulation or substances",
            bg_color="000000FF",
            font_color="00FFFFFF",
            width=20.0
        ),
        ColumnConfig(
            name="Limit",
            bg_color="00B8E6B8",
            font_color="00000000",
            width=10.0
        ),
        ColumnConfig(
            name="Test method",
            bg_color="00B8E6B8",
            font_color="00000000",
            width=15.0
        ),
        ColumnConfig(
            name="Frequency",
            bg_color="00B8E6B8",
            font_color="00000000",
            width=12.0
        ),
        ColumnConfig(
            name="Level",
            bg_color="000000FF",
            font_color="00FFFFFF",
            width=10.0
        ),
        ColumnConfig(
            name="Warning Limit",
            bg_color="00B8E6B8",
            font_color="00000000",
            width=15.0
        ),
        ColumnConfig(
            name="Additional Information",
            bg_color="00B8E6B8",
            font_color="00000000",
            width=20.0
        ),
    ]

    return TemplateConfig(
        name="TSS 17-Column Template",
        description="Standard SEDO Internal TSS template with 17 columns",
        columns=columns,
        header_row=10,
        freeze_panes="A11",
        auto_filter=True
    )


def get_simple_template() -> TemplateConfig:
    """
    Get a simple 5-column template

    Basic template with standard columns for quick use.

    Returns:
        TemplateConfig for simple template
    """
    columns = [
        ColumnConfig(name="ID", width=10.0),
        ColumnConfig(name="Name", width=20.0),
        ColumnConfig(name="Description", width=30.0),
        ColumnConfig(name="Status", width=15.0),
        ColumnConfig(name="Date", width=15.0),
    ]

    return TemplateConfig(
        name="Simple Template",
        description="Basic 5-column template",
        columns=columns,
        header_row=1,
        auto_filter=True
    )
