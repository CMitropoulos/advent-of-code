from collections import Counter

with open('./input.txt', "r") as f:
    lines = f.readlines()

elf_calories = Counter()
elf_id = 1
cur_cals = 0
for idx,line in enumerate(lines):
    if line.strip() == "":
        elf_calories[elf_id] = cur_cals
        elf_id += 1
        cur_cals = 0
    else:
        cur_cals += float(line)
elf_calories[elf_id] = cur_cals
print(elf_calories.most_common(3))
total_cals = sum([i[1] for i in elf_calories.most_common(3)])
print(total_cals)
