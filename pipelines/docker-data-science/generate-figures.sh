#!/usr/bin/env bash
# [wf] execute generate-figures stage

docker run --workdir=/pipeline -v `pwd`:/pipeline \
  dspython scripts/generate-figures.py
