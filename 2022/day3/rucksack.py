filename='./input.txt'
def line_iter(filename):
    for row in open(filename, "r"):
        yield row

def part_1():
    priorities = 0
    for line in line_iter(filename):
        common = set(line[:len(line)//2]).intersection(line[len(line)//2:])
        for letter in common:
            if str.islower(letter):
                priorities+=ord(letter)-96
            else:
                priorities+=ord(letter)-38

    print(f'part 1:{priorities}')


def part_2():
    priorities = 0
    _line_iter = line_iter(filename)
    for line_1 in _line_iter:
        line_2 = next(_line_iter)
        line_3 = next(_line_iter)
        common = set(line_1.strip()).intersection(line_2.strip()).intersection(line_3.strip())
        for letter in common:
            if str.islower(letter):
                priorities+=ord(letter)-96
            else:
                priorities+=ord(letter)-38
    print(f'part 2:{priorities}')
part_1()
part_2()