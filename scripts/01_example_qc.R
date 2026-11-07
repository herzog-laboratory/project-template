#!/usr/bin/env Rscript
# 01_example_qc.R
# Purpose : <one line>
# Input   : cfg$paths$raw/<file>
# Output  : cfg$paths$interim/01_qc/
# Author  : <name>, YYYY-MM-DD
# Notes   : <decisions, caveats; mirror in docs/analysis_log.md>

suppressPackageStartupMessages({
  library(here)
})
source(here("src", "R", "config.R"))
cfg <- load_config()
set.seed(cfg$params$seed)
out_dir <- file.path(cfg$paths$interim, "01_qc")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

# ---- 1. Load --------------------------------------------------------------

# ---- 2. Process -----------------------------------------------------------

# ---- 3. Save --------------------------------------------------------------
# saveRDS(obj, file.path(out_dir, "qc.rds"))
sessionInfo()
