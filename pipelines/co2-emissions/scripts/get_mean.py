#!/usr/bin/env python
import csv
import sys

try:
    # Python 3
    from itertools import zip_longest
except ImportError:
    # Python 2
    from itertools import izip_longest as zip_longest

fname = sys.argv[1]
group_size = int(sys.argv[2])
fout = fname.replace('_clean.csv', '') + '_per_capita_mean.csv'


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


with open(fname, 'r') as fi, open(fout, 'w') as fo:
    r = csv.reader(fi)
    w = csv.writer(fo)

    # get 0-based index of last column in CSV file
    last = len(next(r)) - 1

    for g in grouper(r, group_size):
        group_sum = 0
        year = 0

        for row in g:
            group_sum += float(row[last])
            year = row[0]

        w.writerow([year, group_sum / 5.0])
