#!/usr/bin/env python
import csv
import sys

fname = sys.argv[1]
fout = fname.replace('.csv', '') + '.md'

with open(fname, 'r') as fi, open(fout, 'w') as fo:
    r = csv.reader(fi)

    fo.write('| Year | Mean |\n')
    fo.write('| ---- | ---- |\n')

    for row in r:
        fo.write('| {} |\n'.format(' | '.join(row)))
