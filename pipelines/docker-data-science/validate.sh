#!/bin/bash
# [wf] compare output with original

docker run --rm -v `pwd`:/pipeline --workdir=/pipeline \
  dspython scripts/compare-output.py
