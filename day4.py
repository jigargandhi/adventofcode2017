import typing
passphrase_list =[]

with open('day4.txt', mode='r') as f:
    for l in f.readlines():
        passphrase_list.append(l.strip())

passphrase_list.append("aa bb cc dd ee aa")

def is_valid_passphrase(input):
    phrases= input.split(" ")
    phraseset = set()

    for phrase in phrases:
        if phrase in phraseset:
            return False
        else:
            phraseset = phraseset.union(set([phrase]))
    return True

acc=0
for val in passphrase_list:
    if is_valid_passphrase(val):
        acc+=1

print(acc)

is_valid_passphrase("aa bb cc dd")


