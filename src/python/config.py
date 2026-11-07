"""Load config/config.yaml and resolve ${paths.data_root} references.

Usage:
    from src.python.config import load_config
    cfg = load_config(); cfg["paths"]["raw"]
"""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_config(path: Path = ROOT / "config" / "config.yaml") -> dict:
    if not path.exists():
        raise FileNotFoundError("No config/config.yaml. Copy config/config.example.yaml and edit it.")
    cfg = yaml.safe_load(path.read_text())
    root = cfg["paths"]["data_root"]
    paths = {k: str(v).replace("${paths.data_root}", root) for k, v in cfg["paths"].items()}
    cfg["paths"] = {k: str(p if Path(p).is_absolute() else ROOT / p) for k, p in paths.items()}
    return cfg
