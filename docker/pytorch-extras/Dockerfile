# This Dockerfile pulls a CUDA-enabled PyTorch image and
# extends it with additional utilities and Python packages.

# Keep PYTORCH_TAG in sync with PYTORCH_TAG in the Makefile
ARG PYTORCH_TAG=2.4.0-cuda12.4-cudnn9-runtime

FROM docker.io/pytorch/pytorch:${PYTORCH_TAG}

WORKDIR /app

COPY requirements.txt .

RUN apt update -y && apt install -y wget curl tar && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt