#!/bin/bash
# [wf] obtain n-year means
set -ex

# [wf] group every n years and obtain mean over each group
scripts/get_mean.py data/global_clean.csv 5
