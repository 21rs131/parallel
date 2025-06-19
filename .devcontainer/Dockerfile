FROM continuumio/anaconda3

RUN conda create -n parallel-env python=3.11

SHELL [ "conda", "run", "-n", "parallel-env", "/bin/bash", "-c" ]
RUN conda install -c conda-forge mpi4py && echo "conda activate parallel-env" >> ~/.bashrc

RUN apt-get update && apt-get install -y \
    git \
    tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/opt/conda/envs/parallel-env/lib/python3.11/site-packages:$PYTHONPATH
ENV TZ="Asia/Tokyo"
