import argparse
import glob
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-filename", type=str, default="ml-10m/ratings.dat.libfm")
parser.add_argument("-trainfrac", type=float, default=0.9, help="")

args, _ = parser.parse_known_args()

filename = args.filename
train_frac = args.trainfrac

with open(filename, "r") as fh:
    lines: list[str] = fh.readlines()

n = len(lines)
idx = np.random.permutation(n)
train_n = int(train_frac*n)
test_n = n - train_n
train_idx = idx[:train_n]
test_idx = idx[train_n:train_n+test_n]

strarr = np.array(lines, dtype=str)
train_set = strarr[train_idx].tolist()
test_set = strarr[test_idx].tolist()

with open(filename+".train", "w") as fh:
    fh.writelines(train_set)

with open(filename+".test", "w") as fh:
    fh.writelines(test_set)
