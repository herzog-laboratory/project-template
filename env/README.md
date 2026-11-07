# Environments

Pick one tool per language and commit its lock/definition file here.

- **R**: `renv::init()` once, then `renv::snapshot()` after installing packages. Commit `renv.lock`.
- **Python**, either:
  - **conda** (or mamba/micromamba): `environment.yml` — needed if you use bioconda tools
    (samtools, bedtools, ...). `conda env create -f env/environment.yml`.
  - **uv**: `pyproject.toml` + `uv.lock` — fast, for pure-Python projects. `uv sync` from the repo root.
  Delete the file you are not using so it is clear which one is canonical.
- **Notebooks**: clear outputs before committing (tables and plots can leak data),
  or run `nbstripout --install` once per clone to do it automatically.
- **Containers**: `Dockerfile` / `project.def` are committed; built images are not.
  Push to GHCR/Docker Hub or store `.sif` files in `containers/`.
- Pin the lab tools package to a tag in the lock file so old projects keep working.
