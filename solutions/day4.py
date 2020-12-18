import urllib
import parser
import re

substr_a = r"byr|iyr|eyr|hgt|hcl|ecl|pid"
substr_cid = r"byr|iyr|eyr|hgt|hcl|ecl|pid|cid"

def get_data():
    with open("data/day4_passports.txt") as file:
        return file.read().split("\n\n")


def build_dict(list_of_data: list):
    passport_dict = {}
    for k, v in enumerate(list_of_data):
        v = str(v).strip("\n").split()
        passport_dict[k] = v

    return passport_dict


data = get_data()
data = build_dict(data)


def is_passport(passport_dict: dict, substr):
    strict_dict, cnt ={}, 0
    for k, v in passport_dict.items():
        val = str(v)
        if len(re.findall(substr_a, val)) == 7 or len(re.findall(substr_cid,val)) == 8:
            cnt += 1
            strict_dict[k] = v
    return cnt, strict_dict

#print(is_passport(data, substr_a))


def is_passport_2(strict_dict: dict):
    s_dict = {}
    conditions_list = []
    for k,v in strict_dict.items():
        s_list = []
        for i in v:
            if i.startswith("byr") and 1920 <= int(i.split(":")[1]) <= 2002:
                s_list.append(i)
            elif i.startswith("iyr") and 2010 <= int(i.split(":")[1]) <= 2020:
                s_list.append(i)
            elif i.startswith('eyr') and 2020 <= int(i.split(":")[1]) <= 2030:
                s_list.append(i)

            elif i.startswith('hgt'):
                x = i.split(":")[1]
                if (len(x) == 5 and x.endswith('cm')) and 150 <= int(x[:3]) <= 193:
                    s_list.append(i)

                elif (len(x) == 4 and x.endswith('in')) and 59 <= int(x[:2]) <= 76:
                    s_list.append(i)

            elif i.startswith('hcl') and re.search(r"[#^a-f0-9]{7}", i):
                s_list.append(i)

            elif i.startswith('ecl') and re.search(r"[amb|blu|brn|gry|grn|hzl|oth]{3}", i):
                s_list.append(i)

            elif i.startswith('pid') and re.search(r"\b\d{9}\b", i):
                s_list.append(i)

        if len(s_list) == 7:
            conditions_list.append(s_list)
            print(s_list)
    return len(conditions_list)


solution_1 = is_passport(data, substr_a)
print(is_passport_2(solution_1[1]))