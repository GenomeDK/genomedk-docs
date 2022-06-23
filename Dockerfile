ARG PYTHON_VERSION=3.10-slim

FROM python:${PYTHON_VERSION} AS builder

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel

RUN mkdir -p /build
WORKDIR /build

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN sphinx-build -b dirhtml . _build/html

FROM pierrezemb/gostatic
COPY --from=builder /build/_build/html /srv/http/
