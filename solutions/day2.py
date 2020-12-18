#python3
import os

pw_dict = {}
pw_list = []
with open('data/day2_pwd.txt') as file:
    tmp = []
    cnt = 0
    for line in file:

        pw_dict = {"threshold": line.split()[0], "key": line.split()[1].strip(':'), "entry": line.split()[2]}
        pw_list.append(pw_dict)

res = 0
for line in pw_list:
    count = 0
    rng_min, rng_max = int(line['threshold'].split("-")[0]), int(line['threshold'].split('-')[1])
    for char in line['entry']:
        if char == line['key']:
            count += 1

    if count >= rng_min and count <= rng_max:
        res += 1
"""res is the number of passwords that meet the threshold criteria
    example--> '1-13', 'key': 'q', 'entry': 'qdrqgpcqzbpqftws' """
print(res)

count2 = 0
for line in pw_list:
    string = line['entry']
    first = int(line['threshold'].split('-')[0])
    second = int(line['threshold'].split('-')[1])

    if line['key'] == string[first - 1] and line['key'] != string[second - 1]\
            or line['key'] != string[first - 1] and line['key'] == string[second - 1]:
        count2 += 1
print(count2)