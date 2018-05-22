class Operation():

    def __init__(self, register, operation, value):
        self.register = register
        self.operation = operation
        self.value = value
        self.operations = {
            'inc': lambda x: lambda y: x + y,
            'dec': lambda x: lambda y: x - y
        }

    def evaluate(self, memory):
        memory[self.register] = self.operations[self.operation](memory[self.register])(self.value)


class Condition():

    def __init__(self, register, condition, value):
        self.conditions = {
            '!=': lambda x: lambda y: x != y,
            '>': lambda x: lambda y: x > y,
            '>=': lambda x: lambda y: x >= y,
            '<': lambda x: lambda y: x < y,
            '<=': lambda x: lambda y: x <= y,
            '==': lambda x: lambda y: x == y
        }
        self.register = register
        self.condition = condition
        self.value = value

    def evaluate(self, memory):
        return self.conditions[self.condition](memory[self.register])(self.value)


class Instruction():
    def __init__(self, operation, condition):
        self.operation = operation
        self.condition = condition

    def operate(self, memory):
        if self.condition.evaluate(memory) == True:
            self.operation.evaluate(memory)


class InstructionParser():

    def __init__(self, file_name, memory):
        self.file_name = file_name
        self.memory = memory

    def parse_instructions(self):
        instruction_set= []
        with open(self.file_name, mode='r') as file:
            for line in file.readlines():
                parts = line.strip().split(" ")
                self.memory.add_register(parts[0])
                self.memory.add_register(parts[4])
                operation = Operation(parts[0], parts[1], int(parts[2]))
                condition = Condition(parts[4], parts[5], int(parts[6]))
                instruction =  Instruction(operation, condition)
                instruction_set.append(instruction)
        return instruction_set


class Memory():
    def __init__(self):
        self.memory = {}
        self.max_value = 0

    def largest_value(self):
        return max(self.memory.values())

    def add_register(self, register):
        if register not in self.memory:
            self.memory[register] = 0
    
    def largest_assignment(self):
        return self.max_value
    
    def __getitem__(self, attribute):
        return self.memory[attribute]
    
    def __setitem__(self, attribute, value):
        if value > self.max_value:
            self.max_value = value
        self.memory[attribute] = value

memory = Memory()
parser = InstructionParser("day8_input.txt", memory)
instructions = parser.parse_instructions()
for instr in instructions:
    instr.operate(memory)

print(memory.largest_value()) #part1
print(memory.largest_assignment()) #part2
