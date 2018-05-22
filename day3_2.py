target = 361527

sizeofgrid = 1

while sizeofgrid*sizeofgrid < target:
    sizeofgrid += 2

Matrix = [[0 for x in range(sizeofgrid)] for y in range(sizeofgrid)]


class Direction():
    def __init__(self):
        self.directions = ['Right', 'Top', 'Left', 'Bottom']
        self.position = 0
        self.nDirections = len(self.directions)

    def getNextPosition(self):
        self.position = (self.position+1) % self.nDirections
        return self.directions[self.position]


def neighbour_sum(matrix, i, j):

    # get the sum in all 8 directions
    # +---------+----------+----------+
    # |i-1,j-1  |  i-1, j  | i-1, j+1 |
    # |   lt    |          |          |
    # +-------------------------------+
    # |i, j-1   |   i,j    |    i,j+1 |
    # |         |          |          |
    # +-------------------------------+
    # | i+1 j-1 |  i+1, j  |  i+1,j+1 |
    # |         |          |          |
    # +---------+----------+----------+

    #print(matrix)
    left = 0
    top_left = 0
    bottom_left = 0
    top = 0
    bottom = 0
    right = 0
    top_right = 0
    bottom_right = 0
    if j+1 < sizeofgrid:
        right = matrix[i][j+1]

    if i != 0:
        top = matrix[i-1][j]

    if i+1 < sizeofgrid:
        bottom = matrix[i+1][j]

    if j != 0:
        left = matrix[i][j-1]

    if i != 0 and j != 0:
        top_left = matrix[i-1][j-1]

    if i != 0 and j+1 < sizeofgrid:
        top_right = matrix[i-1][j+1]

    if i+1 < sizeofgrid and j != 0:
        bottom_left = matrix[i+1][j-1]

    if i+1 < sizeofgrid and j+1 < sizeofgrid:
        bottom_right = matrix[i+1][j+1]

    return left+top_left+bottom_left+top+bottom+right+top_right+bottom_right


number = 1
to_target = 1
i, j = int(sizeofgrid/2), int(sizeofgrid/2)
initial_i, initial_j = i, j
Matrix[initial_i][initial_j] = 1
j=j+1
final_i = None
final_j = None
direction = Direction()
found = False
search = None
while to_target < sizeofgrid*sizeofgrid:
    nextDirection = direction.getNextPosition()
    for x in range(number):

        Matrix[i][j] = neighbour_sum(Matrix, i, j)
        if Matrix[i][j] > target:
            search = Matrix[i][j]
            break
        #print("{} {} {}".format(to_target, i, j))
        if nextDirection == "Right":
            i += 1
        elif nextDirection == "Left":
            i -= 1
        elif nextDirection == "Bottom":
            j += 1
        elif nextDirection == "Top":
            j -= 1

        to_target += 1

    if search is not None:
        break
    nextDirection = direction.getNextPosition()
    for x in range(number):

        Matrix[i][j] = neighbour_sum(Matrix, i, j)
        if Matrix[i][j] > target:
            search = Matrix[i][j]
            break
        #print("{} {} {}".format(to_target, i, j))
        if nextDirection == "Right":
            i += 1
        elif nextDirection == "Left":
            i -= 1
        elif nextDirection == "Bottom":
            j += 1
        elif nextDirection == "Top":
            j -= 1
        to_target += 1

    if search is not None:
        break
    number += 1

print(search)
