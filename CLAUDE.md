# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Streamlit UI Toolkit** (v1.0.0) - a Python library extracted from the SEDO TSS Converter application. It provides reusable UI components, theming, and Excel template generation for Streamlit-based data processing applications.

## Dependencies

The library requires (managed by consuming application):
- `streamlit` - UI framework
- `openpyxl` - Excel file handling
- `pyyaml` - YAML configuration

## Architecture

```
streamlit_ui_toolkit/
├── theme/          # Theme system (colors, typography, CSS generation)
├── components/     # UI components (MessageBox, FileUploader, ProgressDisplay, etc.)
├── templates/      # Excel template system with styling
├── utils/          # Validation utilities
└── config/         # Configuration loaders
```

### Key Architectural Patterns

1. **Dataclass Configuration**: All configs (`ThemeConfig`, `TemplateConfig`, `ColumnConfig`) are dataclasses with `to_dict()`/`from_dict()` and YAML serialization methods

2. **Theme Injection**: Apply theme CSS via `ThemeConfig.apply()` which injects `<style>` blocks through `st.markdown()`

3. **Component Pattern**: All UI components accept optional `ThemeConfig` and fall back to default theme:
   ```python
   def __init__(self, theme: Optional[ThemeConfig] = None):
       self.theme = theme or ThemeConfig()
   ```

4. **Excel Colors**: Use ARGB format (8-char hex including alpha), e.g., `"FFFFFF00"` for yellow

### Key Files

- `__init__.py` - Public API exports; see this for all available components
- `theme/theme.py` - `ThemeConfig` class with CSS generation
- `theme/colors.py` - Color palette constants
- `templates/builder.py` - `ExcelTemplateBuilder` creates styled Excel workbooks
- `templates/presets.py` - Pre-built templates including `get_tss_17column_template()` for 17-column TSS format
- `components/` - Individual component files (message_box, file_uploader, progress_display, section_header, buttons)

### TSS 17-Column Template Structure

The primary use case template (`get_tss_17column_template()`):
- Column A: Combination (yellow background)
- Columns B-G: Materials (red background, white text)
- Columns H-K: Regulations (blue background, white text)
- Columns L-Q: Testing (green background, black text)
- Header row: 10, Data starts row 11, Freeze panes at A11
