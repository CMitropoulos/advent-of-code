filename='./input.txt'
def line_iter(filename):
    for row in open(filename, "r"):
        yield row


def part_1():
    members = 0
    for line in line_iter(filename):
        s1, s2 = [tuple(map(int, i.split("-"))) for i in line.strip().split(",")]
        if s1[0]>=s2[0] and s1[1]<=s2[1]:
            members+=1
        elif s2[0]>=s1[0] and s2[1]<=s1[1]:
            members+=1

    print("PART1", members)

def part_2():
    members = 0
    for line in line_iter(filename):
        s1, s2 = [tuple(map(int, i.split("-"))) for i in line.strip().split(",")]
        if any([s2[0]<=i<=s2[1] for i in s1]):
            members+=1
        elif any([s1[0]<=i<=s1[1] for i in s2]):
            members+=1

    print("PART2",members)  


#part_1()
part_2()