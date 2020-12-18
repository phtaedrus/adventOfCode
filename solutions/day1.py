import pandas as pd
import itertools


FILE = "data/day1_expense.txt"

with open(FILE) as f:
    lines = list(f.read().split())

lines = [int(l) for l in lines]

target = 2020

print(lines)
for i in itertools.combinations(lines, 2):
    if sum(i) == target:
        print(i, (i[0] * i[1]))


for i in itertools.combinations(lines, 3):
    if sum(i) == target:
        print(i, i[0] * i[1] * i[2])


