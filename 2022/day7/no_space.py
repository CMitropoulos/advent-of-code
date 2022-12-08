from dataclasses import dataclass
from typing import List

FILENAME='./small_input.txt'

def line_iter(filename):
    for row in open(filename, "r"):
        yield row


@dataclass
class Node:
    name: str
    parent: str
    children: List[str] 
    type_of_file: str
    size: float = 0

    def __hash__(self) -> int:
        return hash(self.name)

class Part1Solution:
    pwd = ""
    tree = {"/": Node("/", None, [], "dir", )}
    state = ""
    def parse_command(self, line):
        cmd_type = line.split(" ")[1]
        if cmd_type == "cd":
            go_to = line.split(" ")[2] 
            self.pwd = go_to if go_to!=".." else self.tree[self.pwd].parent
        self.state = cmd_type

    def add_entry(self, line):
        _pre, f = line.split(" ")
        if _pre == "dir":
            if f not in self.tree:
                self.tree[f] = Node(f, self.pwd, [], "dir" )
                self.tree[self.pwd].children.append(f)
        else:
            _pre = float(_pre)
            if f not in self.tree:
                self.tree[f] = Node(f, self.pwd, [], "file", _pre)
                self.tree[self.pwd].children.append(f)
        print(self.tree)

    def construct_tree(self):
        
        #import pdb;pdb.set_trace()
        for line in line_iter(FILENAME):
            #print(line)
            #print(self.state)
            line = line.strip()
            if line.startswith("$"):
                self.parse_command(line)
                continue
            if "ls" in self.state:
                if line.startswith("$"):
                    self.parse_command(line)
                else:
                    self.add_entry(line)

p1 = Part1Solution()

p1.construct_tree()