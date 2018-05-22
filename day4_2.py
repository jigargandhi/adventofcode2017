import typing
passphrase_list = []

with open('day4.txt', mode='r') as f:
    for l in f.readlines():
        passphrase_list.append(l.strip())

passphrase_list.append("aa bb cc dd ee aa")

anagram_dict = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 31, 'j': 37, 'k': 41, 'l': 43, 'm': 47, 'n': 23,
                'o': 53, 'p': 59, 'q': 61, 'r': 67, 's': 71, 't': 73, 'u': 79, 'v': 83, 'w': 89, 'x': 97, 'y': 101, 'z': 103}


def anagram_hash(word):
    mul = 1
    for i in word:
        mul *= anagram_dict[i]
    return mul


def is_valid_passphrase(input):
    phrases = input.split(" ")
    phraseset = set()

    for phrase in phrases:
        hash = anagram_hash(phrase)
        if hash in phraseset:
            return False
        else:
            phraseset = phraseset.union(set([hash]))
    return True


acc = 0
for val in passphrase_list:
    if is_valid_passphrase(val):
        acc += 1

print(acc)
