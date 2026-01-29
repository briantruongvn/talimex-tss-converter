"""
Theme Colors - Extracted from SEDO TSS Converter app.py
All color constants used in the application
"""

# Primary colors
PRIMARY = "#3b82f6"  # Blue - buttons, step indicators
PRIMARY_HOVER = "#2563eb"  # Darker blue for hover states

# State colors
SUCCESS = "#10b981"  # Green - success messages, completed steps
SUCCESS_BG = "#f0fdf4"  # Light green background
SUCCESS_BORDER = "#bbf7d0"  # Green border
SUCCESS_TEXT = "#166534"  # Dark green text

ERROR = "#dc2626"  # Red - error messages
ERROR_BG = "#fef2f2"  # Light red background
ERROR_BORDER = "#fecaca"  # Red border

WARNING = "#f59e0b"  # Orange - warnings, current step

# Neutral colors
BACKGROUND = "#ffffff"  # White - main background
SURFACE = "#f8fafc"  # Light blue-gray - cards, download section
UPLOAD_BG = "#fafafa"  # Very light gray - upload section background

# Text colors
TEXT_PRIMARY = "#1f2937"  # Dark gray - main text, titles
TEXT_SECONDARY = "#6b7280"  # Medium gray - subtitles, secondary text
TEXT_TERTIARY = "#374151"  # Gray - upload titles, step indicators
TEXT_CONSTRAINTS = "#9ca3af"  # Light gray - file constraints text

# Border colors
BORDER_DEFAULT = "#e5e7eb"  # Light gray - card borders
BORDER_DASHED = "#d1d5db"  # Dashed border for upload section

# Special colors
WHITE = "#ffffff"


# Color groups for easier access
COLORS = {
    "primary": PRIMARY,
    "primary_hover": PRIMARY_HOVER,
    "success": SUCCESS,
    "success_bg": SUCCESS_BG,
    "success_border": SUCCESS_BORDER,
    "success_text": SUCCESS_TEXT,
    "error": ERROR,
    "error_bg": ERROR_BG,
    "error_border": ERROR_BORDER,
    "warning": WARNING,
    "background": BACKGROUND,
    "surface": SURFACE,
    "upload_bg": UPLOAD_BG,
    "text_primary": TEXT_PRIMARY,
    "text_secondary": TEXT_SECONDARY,
    "text_tertiary": TEXT_TERTIARY,
    "text_constraints": TEXT_CONSTRAINTS,
    "border_default": BORDER_DEFAULT,
    "border_dashed": BORDER_DASHED,
    "white": WHITE,
}
