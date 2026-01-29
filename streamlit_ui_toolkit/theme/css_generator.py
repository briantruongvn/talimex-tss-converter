"""
CSS Generator - Generate complete CSS from theme configuration
Reproduces the exact CSS styling from SEDO TSS Converter app.py
"""

from typing import Dict, Any
from . import colors, typography


def generate_css(theme_config: Dict[str, Any] = None) -> str:
    """
    Generate complete CSS for Streamlit app

    Args:
        theme_config: Optional theme configuration override
                     If None, uses default colors and typography

    Returns:
        Complete CSS string ready for st.markdown()
    """
    # Use provided config or defaults
    c = colors.COLORS if theme_config is None else theme_config.get("colors", colors.COLORS)
    t = typography.TYPOGRAPHY if theme_config is None else theme_config.get("typography", typography.TYPOGRAPHY)
    font_family = typography.FONT_FAMILY if theme_config is None else theme_config.get("font_family", typography.FONT_FAMILY)
    font_import = typography.FONT_IMPORT_URL if theme_config is None else theme_config.get("font_import", typography.FONT_IMPORT_URL)

    css = f"""
<style>
    @import url('{font_import}');

    html, body, [class*="css"] {{
        font-family: {font_family};
        background-color: {c['background']};
    }}

    .main-header {{
        text-align: center;
        padding: 0.5rem 0 1rem 0;
        margin-bottom: 1rem;
    }}

    .main-title {{
        font-size: {t['main_title']['size']};
        font-weight: {t['main_title']['weight']};
        color: {c['text_primary']};
        margin-bottom: 0.5rem;
    }}

    .main-subtitle {{
        font-size: {t['main_subtitle']['size']};
        color: {c['text_secondary']};
        font-weight: {t['main_subtitle']['weight']};
        margin-top: 0.5rem;
    }}

    .upload-section {{
        background: {c['upload_bg']};
        border: 1px dashed {c['border_dashed']};
        border-radius: 8px;
        padding: 2rem 1rem;
        text-align: center;
        margin: 1rem 0;
    }}

    .upload-title {{
        font-size: {t['upload_title']['size']};
        font-weight: {t['upload_title']['weight']};
        color: {c['text_tertiary']};
        margin-bottom: 0.5rem;
    }}

    .upload-subtitle {{
        color: {c['text_secondary']};
        font-size: {t['upload_subtitle']['size']};
        margin-bottom: 1rem;
    }}

    .file-constraints {{
        font-size: {t['file_constraints']['size']};
        color: {c['text_constraints']};
        margin-top: 1rem;
    }}

    .process-card {{
        background: {c['white']};
        border: 1px solid {c['border_default']};
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }}

    .step-indicator {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
        font-size: {t['step_indicator']['size']};
        color: {c['text_tertiary']};
    }}

    .step-number {{
        background: {c['primary']};
        color: {c['white']};
        width: 20px;
        height: 20px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: {t['step_number']['size']};
        font-weight: {t['step_number']['weight']};
    }}

    .step-completed {{
        background: {c['success']};
    }}

    .step-current {{
        background: {c['warning']};
    }}

    .success-message {{
        background: {c['success_bg']};
        border: 1px solid {c['success_border']};
        border-radius: 8px;
        padding: 1rem;
        color: {c['success_text']};
        margin: 1rem 0;
    }}

    .error-message {{
        background: {c['error_bg']};
        border: 1px solid {c['error_border']};
        border-radius: 8px;
        padding: 1rem;
        color: {c['error']};
        margin: 1rem 0;
    }}

    .download-section {{
        text-align: center;
        padding: 1.5rem;
        background: {c['surface']};
        border-radius: 8px;
        margin: 1rem 0;
    }}

    /* Hide Streamlit default elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}

    /* Custom button styling */
    .stButton > button {{
        background: {c['primary']};
        color: {c['white']};
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        font-weight: {t['button']['weight']};
        font-size: {t['button']['size']};
        transition: all 0.2s ease;
    }}

    .stButton > button:hover {{
        background: {c['primary_hover']};
    }}

    /* File uploader styling */
    .stFileUploader > div > div > div {{
        padding: 1rem;
    }}
</style>
"""
    return css


def inject_css(theme_config: Dict[str, Any] = None) -> None:
    """
    Generate and inject CSS into Streamlit app

    Usage:
        import streamlit as st
        from streamlit_ui_toolkit.theme.css_generator import inject_css

        inject_css()  # Use defaults
        # or
        inject_css(custom_theme_config)  # Use custom theme

    Args:
        theme_config: Optional custom theme configuration
    """
    import streamlit as st
    css = generate_css(theme_config)
    st.markdown(css, unsafe_allow_html=True)
