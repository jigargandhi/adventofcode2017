target = 361527

sizeofgrid = 1

while sizeofgrid*sizeofgrid < target:
    sizeofgrid += 2

Matrix = [[0 for x in range(sizeofgrid)] for y in range(sizeofgrid)]

class Direction():
    def __init__(self):
        self.directions = ['Right','Top','Left','Bottom']
        self.position =3
        self.nDirections = len(self.directions)
    
    def getNextPosition(self):
        self.position= (self.position+1)%self.nDirections
        return self.directions[self.position]

number = 1
to_target=1
i, j = int(sizeofgrid/2), int(sizeofgrid/2)
initial_i, initial_j = i,j
print("Initial {} {}".format(i, j))
final_i = None
final_j = None
direction = Direction()
found = False
while to_target < sizeofgrid*sizeofgrid:
    nextDirection = direction.getNextPosition()
    for x in range(number):
        if to_target==target:
            final_i = i
            final_j = j
            found = True
            break
        #print("{} {} {}".format(to_target, i, j))
        if nextDirection == "Right":
            i+=1
        elif nextDirection == "Left":
            i-=1
        elif nextDirection =="Bottom":
            j+=1
        elif nextDirection =="Top":
            j-=1
        to_target+=1

    if found:
        break
    nextDirection = direction.getNextPosition()
    for x in range(number):
        if to_target==target:
            final_i = i
            final_j = j
            found = True
            break
        #print("{} {} {}".format(to_target, i, j))
        if nextDirection == "Right":
            i+=1
        elif nextDirection == "Left":
            i-=1
        elif nextDirection =="Bottom":
            j+=1
        elif nextDirection =="Top":
            j-=1
        to_target+=1
    
    if to_target==target+1:
        break
    if found:
        break
    number +=1
    
print("{} {}".format(final_i, final_j))

total_steps = abs(initial_i-final_i)+abs(initial_j-final_j)
print(total_steps)