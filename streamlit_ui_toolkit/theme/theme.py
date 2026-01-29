"""
Theme Configuration - Main theme management class
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional
from pathlib import Path
import yaml

from . import colors
from . import typography as typo_module
from .css_generator import generate_css, inject_css


@dataclass
class ThemeConfig:
    """
    Theme configuration for Streamlit app

    Attributes:
        name: Theme name
        colors: Color palette dictionary
        typography: Typography settings dictionary
        font_family: Font family string
        font_import: Google Fonts import URL
        border_radius: Default border radius
        spacing_unit: Base spacing unit
    """

    name: str = "default"
    colors: Dict[str, str] = field(default_factory=lambda: colors.COLORS.copy())
    typography: Dict[str, Any] = field(default_factory=lambda: typo_module.TYPOGRAPHY.copy())
    font_family: str = typo_module.FONT_FAMILY
    font_import: str = typo_module.FONT_IMPORT_URL
    border_radius: str = "8px"
    spacing_unit: str = "1rem"

    @classmethod
    def default(cls) -> "ThemeConfig":
        """
        Create default theme configuration

        Returns:
            ThemeConfig with default SEDO styling
        """
        return cls()

    @classmethod
    def from_yaml(cls, path: str) -> "ThemeConfig":
        """
        Load theme configuration from YAML file

        Args:
            path: Path to YAML config file

        Returns:
            ThemeConfig loaded from file

        Example YAML structure:
            name: "Custom Theme"
            colors:
              primary: "#3b82f6"
              success: "#10b981"
              ...
            typography:
              main_title:
                size: "3rem"
                weight: 600
              ...
            font_family: "'Inter', sans-serif"
        """
        config_path = Path(path)
        if not config_path.exists():
            raise FileNotFoundError(f"Theme config file not found: {path}")

        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Merge with defaults
        theme = cls.default()

        if 'name' in data:
            theme.name = data['name']
        if 'colors' in data:
            theme.colors.update(data['colors'])
        if 'typography' in data:
            # Merge typography settings
            for key, value in data['typography'].items():
                if key in theme.typography:
                    if isinstance(value, dict):
                        theme.typography[key].update(value)
                    else:
                        theme.typography[key] = value
                else:
                    theme.typography[key] = value
        if 'font_family' in data:
            theme.font_family = data['font_family']
        if 'font_import' in data:
            theme.font_import = data['font_import']
        if 'border_radius' in data:
            theme.border_radius = data['border_radius']
        if 'spacing_unit' in data:
            theme.spacing_unit = data['spacing_unit']

        return theme

    def to_yaml(self, path: str) -> None:
        """
        Export theme configuration to YAML file

        Args:
            path: Output YAML file path
        """
        data = {
            'name': self.name,
            'colors': self.colors,
            'typography': self.typography,
            'font_family': self.font_family,
            'font_import': self.font_import,
            'border_radius': self.border_radius,
            'spacing_unit': self.spacing_unit,
        }

        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert theme to dictionary

        Returns:
            Dictionary representation of theme
        """
        return {
            'name': self.name,
            'colors': self.colors,
            'typography': self.typography,
            'font_family': self.font_family,
            'font_import': self.font_import,
            'border_radius': self.border_radius,
            'spacing_unit': self.spacing_unit,
        }

    def apply(self) -> None:
        """
        Apply theme to current Streamlit app

        Injects CSS into the app using st.markdown()

        Usage:
            import streamlit as st
            from streamlit_ui_toolkit.theme import ThemeConfig

            theme = ThemeConfig.default()
            theme.apply()

            st.title("My App")  # Will use themed styling
        """
        inject_css(self.to_dict())

    def generate_css(self) -> str:
        """
        Generate CSS string from this theme

        Returns:
            Complete CSS string
        """
        return generate_css(self.to_dict())
