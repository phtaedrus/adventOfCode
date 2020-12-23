import pandas as pd
import numpy as np

FILE = "data/day5_boarding.txt"

raw_data = pd.read_csv(FILE, header=None)

data = raw_data[0].apply(lambda x: pd.Series(list(x)))

min_seat, max_seat = 0, 127

tmp = []
for i, row in enumerate(data.itertuples()):
    if row[1] == 'B':
        min_seat, max_seat = 64, 127

    elif row[1] == 'F':
        min_seat, max_seat = 0, 63
    #print(i, row)
    #print(min_seat, max_seat)
    for n in range(2,8):
        if n <= 8:
            if row[n] == 'B' :
                min_seat = min_seat + (128 / (2 ** n))
            else:
                max_seat = max_seat - (128 / (2 ** n))

    left, right = 0, 7
    for j in range(8, 11):
        if row[j] == 'R':
            left = left + (8 / (2 ** (j - 7)))
        else:
            right = right - (8 / (2 ** (j - 7)))

    tmp.append((i, max_seat, right, (max_seat * 8 + right)))

ids = []
for i in tmp:
    ids.append(i[3])
#print(max(products))
"""solution is 822"""

compare = list(range(13, 823))

my_seat = sum(compare) - sum(ids)

"""solution part 2 is 705..........yuck"""
print(my_seat)