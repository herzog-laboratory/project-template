#!/usr/bin/env python
"""02_example_analysis.py

Purpose : <one line>
Input   : cfg["paths"]["interim"]/<file>
Output  : cfg["paths"]["interim"]/02_analysis/
Author  : <name>, YYYY-MM-DD
Notes   : <decisions, caveats; mirror in docs/analysis_log.md>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.python.config import load_config  # noqa: E402

cfg = load_config()
SEED = cfg["params"]["seed"]
OUT_DIR = Path(cfg["paths"]["interim"]) / "02_analysis"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---- 1. Load --------------------------------------------------------------

# ---- 2. Process -----------------------------------------------------------

# ---- 3. Save --------------------------------------------------------------
