# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**TALIMEX Internal TSS Converter** - A Streamlit web application that converts TALIMEX Internal TSS Excel files to Standard Internal TSS format.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Dependencies

- `streamlit>=1.28.0` - Web UI framework
- `openpyxl>=3.1.2` - Excel file handling
- `pyyaml>=6.0` - YAML configuration (for streamlit_ui_toolkit)

## Architecture

```
/
├── app.py                    # Main Streamlit application
├── step0_validate.py         # Validation logic & dataclasses
├── step1_create_template.py  # CLI: Create output template
├── step2_fill_product_info.py # CLI: Fill product info
├── step3_copy_data.py        # CLI: Copy data with column mapping
├── step4_cleanup.py          # CLI: Cleanup & deduplication
├── streamlit_ui_toolkit/     # Reusable UI toolkit library
│   ├── templates/presets.py  # get_tss_17column_template()
│   └── ...
├── input/                    # Input files folder (for CLI)
├── output/                   # Output files folder (for CLI)
└── requirements.txt
```

## Key Files

### `app.py` - Main Application

The Streamlit app handles the complete conversion workflow:

1. **File Upload**: Accept multiple `.xlsx`/`.xls` files
2. **Validation**: Check header row format against expected columns
3. **Processing**: 4-step pipeline (template → product info → copy data → cleanup)
4. **Download**: Single file or ZIP for multiple files

Key functions:
- `validate_file_content(file_bytes, filename)` - Validate Excel format
- `process_file(input_bytes, input_filename, progress_callback)` - Main conversion pipeline
- `main()` - Streamlit UI entry point

### `step0_validate.py` - Validation

Exports used by app.py:
- `EXPECTED_HEADERS` - Dict of column index → expected header text
- `HEADER_ROW = 9` - Row containing headers in input files
- `ValidationError` - Dataclass for column validation errors
- `ValidationResult` - Dataclass for file validation results

### Column Mapping

Input columns are mapped to output columns:
```python
COLUMN_MAPPING = {
    2: 17,   # B → Q (Material → temp column, cleared after)
    4: 2,    # D → B (General Type)
    5: 3,    # E → C (Sub-Type)
    6: 4,    # F → D (Material Designation)
    7: 5,    # G → E (Material Distributor)
    8: 6,    # H → F (Producer)
    9: 7,    # I → G (Material Type)
    10: 8,   # J → H (Document Type)
    11: 9,   # K → I (Requirement Source)
    12: 10,  # L → J (Sub-Type)
    14: 11,  # N → K (Details)
    15: 12,  # O → L (Test Requirement)
}
```

## Memory Management

The app includes memory leak prevention:
- **Workbook closing**: All openpyxl workbooks are closed after use
- **File bytes caching**: Files read once into cache, reused for validation & processing
- **Garbage collection**: `gc.collect()` called after processing
- **Auto-cleanup**: Old processed files cleared when new files uploaded

## TSS 17-Column Output Template

From `streamlit_ui_toolkit.templates.presets.get_tss_17column_template()`:
- Column A: Combination (yellow background)
- Columns B-G: Materials (red background, white text)
- Columns H-K: Regulations (blue background, white text)
- Columns L-Q: Testing (green background, black text)
- Header row: 10, Data starts row 11, Freeze panes at A11
- Product columns start at R (column 18) with peach background

## Processing Steps

1. **Create Template**: Build output workbook with styled header row
2. **Fill Product Info**: Extract product names & article numbers from input, add columns R+
3. **Copy Data**: Map input columns to output, mark products with "X"
4. **Cleanup**:
   - Clear column K if column H is not "Test Report" or "TR"
   - Set column A to "Art" if column Q contains "article"
   - Clear column Q (temp column)
   - Remove duplicate rows

## CLI Pipeline (Optional)

For batch processing without UI:
```bash
# Place files in input/ folder, then run:
python step0_validate.py  # Validate format
python step1_create_template.py
python step2_fill_product_info.py
python step3_copy_data.py
python step4_cleanup.py
# Results in output/ folder
```
