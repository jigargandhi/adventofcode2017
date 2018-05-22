banks = [0,2,7,0]
banks = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]
print(sum(banks))
def redistribute(banks):
    maxIndex = 0
    maxValue = banks[0]
    memory_length = len(banks)
    #find max
    for i in range(memory_length):
        if banks[i] > maxValue:
            maxValue = banks[i]
            maxIndex = i
    
    #redistribute

    blocks = banks[maxIndex]
    banks[maxIndex] = 0
    index = (maxIndex+1)%memory_length
    while blocks>0:
        banks[index]+=1
        blocks-=1
        index= (index+1)%memory_length
    
    return banks


def hash_list(banks):
    return str(banks)

seen = {}

steps = 0
seen_again=None
while True:
    
    banks = redistribute(banks)
    steps+=1
    
    hash = hash_list(banks)
    print(hash)
    if hash in seen:
        seen_again= seen[hash]
        break
    else:
        seen[hash]= steps
    

print(steps-seen_again)
