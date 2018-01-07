#!/usr/bin/env python
import csv
import sys

fname = sys.argv[1]


with open(fname, 'r') as fi:
    r = csv.reader(fi)

    print('| Year | Mean |')
    print('| ---- | ---- |')

    for row in r:
        print('| {} |'.format(' | '.join(row)))
