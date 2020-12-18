import re
import itertools
import parser

"""
def get_data(parser = str, sep='\n'):
    with open("data/day3_trees.txt") as data:
        sections = data.read().rstrip().split(sep)
        return [x for x in sections]

rowlist = get_data()

def solution(slope):
    slope = slope
    y, dy = 1, 1
    x, dx = 3, 3
    trees = []

    for row, y in enumerate(rowlist):
        row = row + 2
        if y[row * 1 % len(y)] == "#":
            trees.append(1)
    print(sum(trees))
    return sum(trees)


solution(2)
print(84*289*89*71*73)
"""
