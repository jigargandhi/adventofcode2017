# its a nice parsing problem where we have to look back
# it can be handled as a state machine 
# think how to implement state machine in python
# i should learn abc in python and how to implement statemachine
# example states are 
#   a. Garbage State
#   b. Escape State
#   c. Group State
#   d. Finish State
# The application starts in groupopenstate and finishes in group close state
# each state reads one/ more character from input and writes to the o/p
# additionally, it also transitions to another state based on the input
# Group state can be hierarchical 
# Step 2: Count the groups and add their sum 

import io
from abc import ABC, abstractmethod

file_name = 'day9_input.txt'
#file_name = 'day9_test.txt'
with open(file_name,mode='r') as f:
    data= f.read()
    strm = io.StringIO(data)

output = io.StringIO()

class State(ABC):

    def __init__(self, output_stream):
        self.output_stream = output_stream
        

    @abstractmethod
    def transition(self, next_character):
        pass

class GroupState(State):
    def __init__(self,output_stream):
        #self.value = value
        super().__init__(output_stream)
        
    def transition(self, next_character):
        # if next_character == '!':
        #     return EscapeState(self.output_stream,self)
        # el
        if next_character == '<':
            return GarbageState(self.output_stream)
        
        if next_character== '{' or next_character=='}':
            self.output_stream.write(next_character)
        
        return self

class GarbageState(State):

    def __init__(self,output_stream):
        #self.value = value
        super().__init__(output_stream)
    
    def transition(self, next_character):
        if next_character =='>':
            return GroupState(self.output_stream)
        if next_character=='!':
            return EscapeState(self.output_stream,self)
        return self

class EscapeState(State):
    def __init__(self,output_stream,previous_state):
        #self.value = value
        super().__init__(output_stream)
        self.escape_start= True
        self.previous_state = previous_state
    
    def transition(self,next_character):
        if self.escape_start == True:
            self.escape_start = False
            return self
        
        return GarbageState(self.output_stream)

# state=GroupState(output)
# index=0
# for char in strm.read():
#     state = state.transition(char)
#     # print(char, state)
#     # index+=1
#     # if index ==100:
#     #     break

garbage= False
escape = False
start_count= True
count=0
for char in strm.read():
    #print(char)
    if escape == True:
        escape= False
        continue

    if char=='{' :
        if garbage== False and escape == False:
            output.write(char)
    if char=='<':
        garbage = True
        

    if char=='>':
        garbage = False

    if char=='!':
        if escape==False:
            escape = True
        
    if char=='}':
        if garbage== False and escape == False:
            output.write(char)
    
    if garbage == True and escape == False:
        count+=1
    
count=0
garbage= False
escape = False
with open(file_name,mode='r') as f:
    data= f.read()
    strm = io.StringIO(data)
for char in strm.read():
    #print(char)
    if escape == True:
        escape= False
        continue

    if char=='{' :
        if garbage== False and escape == False:
            continue

    if char=='<':
        if garbage == False:
            garbage=True
            continue
        
        

    if char=='>':
        garbage = False
        continue

    if char=='!':
        if escape==False:
            escape = True
            continue
        
    if char=='}':
        if garbage== False and escape == False:
            continue
    
    if garbage == True and escape == False:
        count+=1
        
    
groups = output.getvalue()

score= 0
acc=0
for l in groups:
    if l == '{':
        score+=1
    if l=='}':
        acc+=score
        score-=1
        
        
    # print(stack,acc)

print(acc,count)




