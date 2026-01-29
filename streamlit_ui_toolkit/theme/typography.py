"""
Typography Settings - Extracted from SEDO TSS Converter app.py
Font family, sizes, and weights used in the application
"""

# Font family
FONT_FAMILY = "'Inter', sans-serif"
FONT_IMPORT_URL = "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"

# Font sizes (in rem)
FONT_SIZES = {
    "xs": "0.75rem",      # 12px - step number badges
    "sm": "0.875rem",     # 14px - file constraints
    "base": "0.9rem",     # 14.4px - step indicators, upload subtitle
    "md": "1rem",         # 16px - main subtitle
    "lg": "1.2rem",       # 19.2px - upload title
    "xl": "3rem",         # 48px - main title
}

# Font weights
FONT_WEIGHTS = {
    "light": 300,
    "normal": 400,
    "medium": 500,
    "semibold": 600,
    "bold": 700,
}

# Specific typography styles for components
TYPOGRAPHY = {
    "main_title": {
        "size": FONT_SIZES["xl"],
        "weight": FONT_WEIGHTS["semibold"],
    },
    "main_subtitle": {
        "size": FONT_SIZES["md"],
        "weight": FONT_WEIGHTS["normal"],
    },
    "upload_title": {
        "size": FONT_SIZES["lg"],
        "weight": FONT_WEIGHTS["medium"],
    },
    "upload_subtitle": {
        "size": FONT_SIZES["base"],
        "weight": FONT_WEIGHTS["normal"],
    },
    "file_constraints": {
        "size": FONT_SIZES["sm"],
        "weight": FONT_WEIGHTS["normal"],
    },
    "step_indicator": {
        "size": FONT_SIZES["base"],
        "weight": FONT_WEIGHTS["normal"],
    },
    "step_number": {
        "size": FONT_SIZES["xs"],
        "weight": FONT_WEIGHTS["medium"],
    },
    "button": {
        "size": FONT_SIZES["base"],
        "weight": FONT_WEIGHTS["medium"],
    },
}
