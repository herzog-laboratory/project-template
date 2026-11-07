# Publishing code with a manuscript

The working repo is private and stays private. Publication is a **new public repo made from a
clean export**: no history, no analysis log, no exploratory scripts.

## 1. Tag the working repo
```bash
git tag v1.0-submitted && git push --tags
```

## 2. Export a clean snapshot
```bash
git archive v1.0-submitted --format=tar --prefix=PROJECT/ \
  -- . ':!docs/analysis_log.md' ':!scripts/explore' ':!.github' ':!docs/PUBLISHING.md' \
  | tar -x -C ~/tmp/
```

## 3. Check it by eye before it goes public
- [ ] README: no internal paths, server names, or people who shouldn't be named
- [ ] config/config.example.yaml: placeholder paths only
- [ ] No sample/participant identifiers in comments, tables or figure names
- [ ] No credentials, tokens, or `.env` files
- [ ] Environment lock files present so it actually runs
- [ ] LICENSE chosen (MIT is the lab default for code)
- [ ] README states where the data can be obtained (accession / access committee)

## 4. Create the public repo and mint a DOI
```bash
cd ~/tmp/PROJECT && git init && git add -A && git commit -m "Code for <paper>, v1.0"
# create herzog-laboratory/PROJECT-paper on GitHub (public), push, tag v1.0
```
Enable the repo in Zenodo (GitHub integration), create a GitHub release, and cite the DOI
in the manuscript. Revisions: repeat from step 1 with v1.1-revision; Zenodo versions the DOI.
