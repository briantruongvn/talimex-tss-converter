"""
Template Schema - Column and Template configuration dataclasses
Extracted from SEDO TSS Converter step3_template_creation.py
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path
import yaml


@dataclass
class ColumnConfig:
    """
    Configuration for a single Excel column

    Attributes:
        name: Column header text
        width: Column width in characters
        bg_color: Background color in ARGB hex format (e.g., "00FFFF00")
        font_color: Font color in ARGB hex format (e.g., "00000000")
        font_bold: Whether font is bold
        horizontal_align: Horizontal alignment ("left", "center", "right")
        vertical_align: Vertical alignment ("top", "center", "bottom")
        wrap_text: Whether to wrap text
    """
    name: str
    width: float = 15.0
    bg_color: str = "00FFFFFF"  # White background
    font_color: str = "00000000"  # Black text
    font_bold: bool = True
    horizontal_align: str = "center"
    vertical_align: str = "center"
    wrap_text: bool = True

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ColumnConfig":
        """Create ColumnConfig from dictionary"""
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "width": self.width,
            "bg_color": self.bg_color,
            "font_color": self.font_color,
            "font_bold": self.font_bold,
            "horizontal_align": self.horizontal_align,
            "vertical_align": self.vertical_align,
            "wrap_text": self.wrap_text,
        }


@dataclass
class TemplateConfig:
    """
    Complete Excel template configuration

    Attributes:
        name: Template name
        description: Template description
        columns: List of column configurations
        header_row: Row number for headers (1-indexed)
        freeze_panes: Cell reference for freeze panes (e.g., "A11")
        auto_filter: Enable auto-filter on headers
    """
    name: str
    columns: List[ColumnConfig] = field(default_factory=list)
    description: str = ""
    header_row: int = 10
    freeze_panes: Optional[str] = None
    auto_filter: bool = True

    @classmethod
    def from_yaml(cls, path: str) -> "TemplateConfig":
        """
        Load template configuration from YAML file

        Args:
            path: Path to YAML config file

        Returns:
            TemplateConfig instance

        Example YAML structure:
            name: "TSS Template"
            description: "17-column template"
            header_row: 10
            columns:
              - name: "Combination"
                width: 15.0
                bg_color: "00FFFF00"
                font_color: "00000000"
              - name: "General Type"
                width: 20.0
                bg_color: "00FF0000"
                font_color: "00FFFFFF"
        """
        config_path = Path(path)
        if not config_path.exists():
            raise FileNotFoundError(f"Template config not found: {path}")

        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Parse columns
        columns = []
        for col_data in data.get('columns', []):
            columns.append(ColumnConfig.from_dict(col_data))

        return cls(
            name=data.get('name', 'Untitled'),
            description=data.get('description', ''),
            columns=columns,
            header_row=data.get('header_row', 10),
            freeze_panes=data.get('freeze_panes'),
            auto_filter=data.get('auto_filter', True)
        )

    def to_yaml(self, path: str) -> None:
        """
        Export template configuration to YAML file

        Args:
            path: Output YAML file path
        """
        data = {
            'name': self.name,
            'description': self.description,
            'header_row': self.header_row,
            'freeze_panes': self.freeze_panes,
            'auto_filter': self.auto_filter,
            'columns': [col.to_dict() for col in self.columns]
        }

        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'name': self.name,
            'description': self.description,
            'header_row': self.header_row,
            'freeze_panes': self.freeze_panes,
            'auto_filter': self.auto_filter,
            'columns': [col.to_dict() for col in self.columns]
        }
