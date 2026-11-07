# data/ — gitignored, lives only in the canonical project folder

raw/        Working copy of the original data. Original is backed up at <backup location>.
            Keep raw/README.md: source, date received, md5 checksums (`md5sum * > checksums.md5`).
interim/    One subfolder per script: 01_qc/, 02_normalise/, ... Regenerable; safe to delete.
processed/  Analysis-ready objects used by reports.
