# Load config/config.yaml and resolve ${paths.data_root} references.
# Usage:  source("src/R/config.R"); cfg <- load_config(); cfg$paths$raw
load_config <- function(path = here::here("config", "config.yaml")) {
  if (!file.exists(path)) stop("No config/config.yaml. Copy config/config.example.yaml and edit it.")
  cfg <- yaml::read_yaml(path)
  resolve <- function(x) {
    if (is.character(x)) x <- gsub("\\$\\{paths\\.data_root\\}", cfg$paths$data_root, x, fixed = FALSE)
    x
  }
  cfg$paths <- lapply(cfg$paths, resolve)
  cfg$paths <- lapply(cfg$paths, function(p) if (startsWith(p, "/")) p else here::here(p))
  cfg
}
