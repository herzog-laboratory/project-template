# <Project name>

> One-paragraph summary: biological question, data type, main approach.

| | |
|---|---|
| **Lead** | name |
| **Contributors** | names |
| **Started** | YYYY-MM-DD |
| **Status** | planning / active / writing up / archived |
| **Canonical folder** | `<shared storage>/projects/YYYY-shortname/` (data lives here, gitignored) |
| **Raw data backup** | `<backup location>` (original, read-only copy) |
| **Related** | wet-lab notebook pages, manuscript link, tools used |

## Quick start

```bash
git clone git@github.com:<org>/<repo>.git
cd <repo>
cp config/config.example.yaml config/config.yaml   # edit paths for your machine
# R:      Rscript -e 'renv::restore()'
# Python: conda env create -f env/environment.yml   OR   uv sync   (see env/README.md)
# Notebooks: clear outputs before committing (or run `nbstripout --install` once)
```

Then run scripts in numerical order: `scripts/01_*.R`, `scripts/02_*.py`, ...

## Repository layout

```
scripts/   Numbered, annotated analysis steps. Run top to bottom.
src/       Reusable functions used by scripts (R/ and python/).
           If a function is needed in a second project, move it to the lab tools package.
config/    config.yaml (gitignored, machine-specific paths) + committed .example
env/       Environment definitions: renv.lock, environment.yml, Dockerfile, *.def
reports/   Rmd / Quarto / notebooks for write-ups. Outputs are NOT committed.
docs/      analysis_log.md (dated decisions), notes, protocols
data/      NEVER committed (gitignored). raw/ = working copy of backed-up original;
           interim/<NN_step>/ = output of script NN; processed/ = analysis-ready.
results/   NEVER committed except small summary tables explicitly whitelisted.
containers/ NEVER committed. Built .sif / images; definitions are in env/.
tests/     Tests for src/ functions
```

## Data

The project folder *is* the git repo; `data/`, `results/` and `containers/` are gitignored
and exist only in the canonical folder on shared storage (never inside OneDrive/Drive sync).

- `data/raw/` — working copy of the original, which is backed up separately at `<backup location>`.
  Keep `data/raw/README.md` with source, date, and md5 checksums so the copy can be verified.
- `data/interim/NN_step/` — one subfolder per script, e.g. `01_qc/`, `02_normalise/`.
  Everything here is regenerable by running scripts from that step onward.
- `data/processed/` — analysis-ready objects, versioned in dated subfolders if they change.

Sensitivity level: public / internal / restricted (human). Restricted data must stay on <approved system>.

## Containers

Built images are stored at `<shared storage>/projects/YYYY-shortname/containers/` or on GHCR,
not in git. Definitions are in `env/`.

## Close-out checklist

- [ ] Raw data archived - e.g., to cold storage; checksums verified
- [ ] Repo tagged (`git tag v1.0-submitted`)
- [ ] If manuscript: code deposited on Zenodo for DOI and cited in manuscript
- [ ] If manuscript: data deposited (GEO / SRA / PRIDE / institutional repo) with accession recorded here
- [ ] Reusable functions promoted to the lab tools package
