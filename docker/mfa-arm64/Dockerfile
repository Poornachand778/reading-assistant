FROM condaforge/mambaforge:latest

RUN apt-get update && apt-get install -y build-essential git wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN mamba create -n aligner -c conda-forge \
    python=3.11 kalpy openfst icu libsndfile sox \
    && mamba clean -a -y

SHELL ["bash","-lc"]
RUN conda activate aligner \
    && pip install --no-binary=:all: --upgrade pip wheel cython \
    && pip install --no-binary=:all: baumwelch montreal-forced-aligner

ENV PATH="/opt/conda/envs/aligner/bin:${PATH}"
ENTRYPOINT ["mfa"]
