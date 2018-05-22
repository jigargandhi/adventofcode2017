class Node():
    """
    Defines a program in advent of code day 7 puzzle
    """

    def __init__(self, name, weight=None, children=None):
        """
        """
        self.name = name
        self.weight = weight
        self.parent = None
        self.total_weight = weight
        if children is None:
            self.children = []
        else:
            self.children = children
            for child in self.children:
                child.parent = self

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def __repr__(self):
        return "Node[name = {}, weight = {}, total_weight = {}]"\
            .format(self.name, self.weight, self.total_weight)

    def get_total_weight(self):
        if len(self.children)==0:
            return self.weight
        else:
            return self.weight + sum([ child.get_total_weight() for child in self.children ])
    
    def find_unbalanced_node(self):
        if len(self.children) <2:
            return None
        else:
            differentNode = None
            for i in range(1, len(self.children)-1):
                prev= self.children[i-1].get_total_weight()
                current = self.children[i].get_total_weight()
                next = self.children[i+1].get_total_weight()
                if prev!= current and current!=next:
                    differentNode = self.children[i]
                    break
                elif prev!=current and current== next:
                    differentNode = self.children[i-1]
                    break
                elif prev ==current and current!=next:
                    differentNode = self.children[i+1]
                    break
                else:
                    continue
            
            if differentNode is not None:
                still_unbalanced= differentNode.find_unbalanced_node()
                if still_unbalanced is None:
                    return differentNode
                else:
                    return still_unbalanced
        return None
    



class World():

    def __init__(self, file_name):
        self.programs = {}
        self.file_name = file_name
        self.raw_programs = {}

    def parse_world(self):
        with open(self.file_name, mode='r') as f:
            for line in f.readlines():
                line = line.strip()
                key, weight, children = self.line_parser(line)
                if key not in self.raw_programs:
                    self.raw_programs[key] = (weight, children)
                else:
                    weight, current_children = self.raw_programs[key]
                    self.raw_programs[key] = (
                        weight, current_children + children)

            print("parsing finished")

    def prepare_world(self):

        # 1st pass
        for program_name in self.raw_programs.keys():
            weight, _ = self.raw_programs[program_name]
            node = Node(program_name, weight, [])
            self.programs[program_name] = node

        # 2nd pass
        for program_name in self.raw_programs.keys():
            parent_program = self.programs[program_name]
            _, children = self.raw_programs[program_name]
            for child_program_name in children:
                child_node = self.programs[child_program_name]
                parent_program.add_child(child_node)

    def line_parser(self, text_input):
        parts = text_input.split("->")
        part1 = parts[0].strip()
        if len(parts) == 1:
            part2 = ""
        else:
            part2 = parts[1].strip()
        part1parts = part1.split("(")
        program_name = part1parts[0].strip()
        weight = int(part1parts[1][:-1].strip())
        if part2 == "":
            children = []
        else:
            children = [k.strip() for k in part2.split(",")]
        return program_name, weight, children

    def get_random_node(self):
        import random
        nodeIndex = random.randint(0, len(self.programs)-1)
        randomr_key = list(self.programs.keys())[nodeIndex]
        node = self.programs[randomr_key]
        return node

    def propogate_weight(self):
        pass


def traverse_node(node):
    if node.parent is None:
        return node
    else:
        return traverse_node(node.parent)


world = World("day7_input2.txt")
world.parse_world()
world.prepare_world()
node = world.get_random_node()
world.propogate_weight()
root = traverse_node(node)

# for child in root.children:
#     print("{} ({}) ({}) ".format(child.name, child.weight, child.get_total_weight()))

print(root.find_unbalanced_node())
