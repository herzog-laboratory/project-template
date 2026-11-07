# Build:  docker build -t ghcr.io/<org>/YYYY-shortname:0.1 -f env/Dockerfile .
# Apptainer: apptainer build containers/project.sif docker://ghcr.io/<org>/YYYY-shortname:0.1
FROM rocker/r-ver:4.4.2
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxml2-dev libssl-dev libcurl4-openssl-dev python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN R -e "install.packages('renv')"
WORKDIR /project
COPY env/renv.lock renv.lock
RUN R -e "renv::restore()"
COPY env/environment.yml environment.yml
# Add python deps / micromamba here if needed
