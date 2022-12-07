from collections import defaultdict
import re 


move_re = re.compile(r"move (\d+) from (\d+) to (\d+)\s*")
filename='./input.txt'
def line_iter(filename):
    for row in open(filename, "r"):
        yield row

stacks = defaultdict(list)

def add_to_stacks(line):
    l_iter = iter(line)
    for idx,i in enumerate(l_iter):
        j = next(l_iter)
        k = next(l_iter)
        #print(i, j ,k)
        if j!=" ":
            stacks[idx+1].insert(0, j)
        next(l_iter, None)

def calculate_move(moves):
    for i in range(int(moves[0])):
        item_to_move = stacks[int(moves[1])].pop()
        stacks[int(moves[2])].append(item_to_move)
    

def part_1():
    for line in line_iter(filename):
        #print(line)
        if "[" in line:
            add_to_stacks(line)
        elif move_re.match(line):
            #print("before", stacks)
            calculate_move(move_re.match(line).groups())
            #print("after", stacks)
            
    
    result = []
    for i in range(1, len(stacks)+1):
        result.append(stacks[i][-1])
    print(''.join(result))

#part_1()


def calculate_move_part2(moves):
    num_items = int(moves[0])
    stacks[int(moves[2])].extend(stacks[int(moves[1])][-num_items:])

    for i in range(num_items):
        stacks[int(moves[1])].pop()

def part_2():
    for line in line_iter(filename):
        #print(line)
        if "[" in line:
            add_to_stacks(line)
        elif move_re.match(line):
            #print("before", stacks)
            calculate_move_part2(move_re.match(line).groups())
            #print("after", stacks)
            
    
    result = []
    for i in range(1, len(stacks)+1):
        result.append(stacks[i][-1])
    print(''.join(result))

part_2()