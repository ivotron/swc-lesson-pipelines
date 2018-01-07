#!/usr/bin/env python
import csv
import sys

fname = sys.argv[1]
fout = fname.replace('.csv', '') + '_clean.csv'

with open(fname, 'r') as fi, open(fout, 'w') as fo:
    r = csv.reader(fi)
    w = csv.writer(fo)

    # get 0-based index of last column in CSV file
    last = len(next(r)) - 1

    # go back to first line
    fi.seek(0)

    for row in r:
        if not row[last]:
            row[last] = 0
        w.writerow(row)
