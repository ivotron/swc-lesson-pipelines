#!/usr/bin/env bash
# [wf] execute generate-learning-curves stage

docker run --workdir=/pipeline -v `pwd`:/pipeline \
  dspython scripts/generate-learning-curves.py
