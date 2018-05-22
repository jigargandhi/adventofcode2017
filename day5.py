#day 1
# register = []

# with open('day5.txt', mode='r') as f:
#     for l in f.readlines():
#         register.append(int(l.strip()))
# step_count = 0
# index =0
# while index>=0 and index <len(register):
#     step_count+=1
#     old_index = index
#     index += register[index]
#     register[old_index]+=1

# print(step_count)


register = []

with open('day5.txt', mode='r') as f:
    for l in f.readlines():
        register.append(int(l.strip()))
step_count = 0
index =0
while index>=0 and index <len(register):
    step_count+=1
    old_index = index
    offset = register[index]
    index += register[index]
    if offset >=3:
        register[old_index]-=1
    else:
        register[old_index]+=1

print(step_count)