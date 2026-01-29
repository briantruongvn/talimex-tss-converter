"""
Bước 1: Tạo template TSS trống từ ui_toolkit
- Đọc tất cả file Excel từ folder input
- Tạo template với tên: {input_filename}-Step1.xlsx cho mỗi file
"""

from pathlib import Path
from streamlit_ui_toolkit.templates import get_tss_17column_template, ExcelTemplateBuilder

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"


def get_input_files() -> list[Path]:
    """Lấy tất cả file Excel từ folder input"""
    input_path = Path(INPUT_FOLDER)
    files = list(input_path.glob("*.xlsx")) + list(input_path.glob("*.xls"))
    if not files:
        raise FileNotFoundError(f"Không tìm thấy file Excel trong folder {INPUT_FOLDER}")
    return files


def main():
    # Lấy tất cả file input
    input_files = get_input_files()

    # Lấy template config TSS 17 cột
    template = get_tss_17column_template()

    # Tạo builder
    builder = ExcelTemplateBuilder(template)

    print(f"Tìm thấy {len(input_files)} file trong folder input")

    for input_file in input_files:
        input_name = input_file.stem  # Tên file không có extension

        # Xuất file: {input_name}-Step1.xlsx
        output_filename = f"{input_name}-Step1.xlsx"
        output_path = builder.create_workbook(f"{OUTPUT_FOLDER}/{output_filename}", sheet_name="TSS Data")

        print(f"  {input_file.name} → {output_filename}")

    print(f"\nHoàn thành! Đã tạo {len(input_files)} template.")


if __name__ == "__main__":
    main()
