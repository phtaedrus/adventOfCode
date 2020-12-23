import io
import pandas as pd
import itertools


with open('data/day6_groups.txt') as file:
    raw_groups = file.read().split('\n\n')

print(len(raw_groups))


df_groups = [x.rstrip().split(' ') for x in raw_groups]

tmp = []
for each_entry in raw_groups:
    list_of_groups = each_entry.split('\n')
    tmp.append(list_of_groups)

#print(len(tmp))
_list = []
final_answers = []
all_yes_list = []
for s in tmp:
    tmp_set = set(s)

    #count = sum(count_list[s])
    total_string = str()

    for grp in tmp_set:
        total_string += grp
    final_answers.append(len(set(total_string)))
"""res == 6680"""
res = sum(final_answers)

print(tmp)
in_list, out_list = [], []
for each_set in tmp:
    for i in each_set:
        #strips = [set(x) for x in each_set]

        intersecting_chars = set.intersection(*map(set, each_set))
    print(intersecting_chars)

    out_list.append(intersecting_chars)
cnt = 0
for x in out_list:
    if x == 'set()':
        pass
    else:
        cnt += len(x)

print(cnt)  #TODO this is the right answer but ugly bit of logic at the end Solution = 3117
#['vmzodatscnrfek', 'epjkrabmiusofzclt']
#['mozselrxb', 'sfjomkzl', 'stlomz', 'mlsjoqz', 'amoszl']]
#m, o, z, s, l,