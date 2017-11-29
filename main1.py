import random

def DNAgenerator(length):
    s = ''
    for i in range(length):
        s += random.choice('ACTG')
    return s

# print(DNAgenerator(10))


def DNAchanger(s, persent):
    inds = list(range(1,len(s)))
    for i in range(int(persent * len(s))):
        cur_ind = inds.pop(inds.index(random.choice(inds)))
        s = s[:cur_ind-1] + random.choice('ACTG') + s[cur_ind:]
        s = s[:cur_ind - 1] + random.choice('ACTG') + s[cur_ind:]

    return s


dna = DNAgenerator(100)
# print(dna)
# print(DNAchanger(dna, 0.25))

