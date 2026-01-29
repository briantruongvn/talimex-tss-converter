"""
Templates Module - Excel Template System

Provides Excel template generation with:
- Column configuration with colors, widths, fonts
- Template builder for creating formatted Excel files
- Pre-defined templates (TSS 17-column, simple templates)
- YAML configuration support
"""

from .schema import ColumnConfig, TemplateConfig
from .builder import ExcelTemplateBuilder
from .presets import get_tss_17column_template, get_simple_template

__all__ = [
    "ColumnConfig",
    "TemplateConfig",
    "ExcelTemplateBuilder",
    "get_tss_17column_template",
    "get_simple_template",
]
