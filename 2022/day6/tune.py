filename='./input.txt'
def line_iter(filename):
    for row in open(filename, "r"):
        yield row

def process_line(line, window = 4):
    
    for idx in range(len(line)-window-1):
        print(line[idx:idx+window])
        if len(set(line[idx:idx+window]))== window:
            return (idx+window)
    return False

def part_1():
    for line in line_iter(filename):
        res = process_line(line)
    if res:
        print(res)
    else:
        print("ERROR")
#part_1()

def part_2():
    for line in line_iter(filename):
        res = process_line(line, 14)
    if res:
        print(res)
    else:
        print("ERROR")
part_2()

