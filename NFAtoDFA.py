# Encoding: UTF-8
# Authors: Javier Martínez Hernández, Roberto Téllez Perezyera
"""
This program is rlly cool thks for using it
"""
import sys
from itertools import chain, combinations

it = open("test.txt", "r")



# it = iter(sys.stdin.read().splitlines())



def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


# read input and create a list of triplets
triplets = next(it).split("),(")
triplets[0] = triplets[0][2::]
triplets[-1] = triplets[-1][:-3:]

triples=[]
for x in range(0, len(triplets)):
    triples.append(triplets[x].split(","))
print(triples)




sigmaN = []
for x in range(0, len(triples)):
    if triples[x][2]not in sigmaN:
        sigmaN.append(triples[x][2])

sigmaD = sigmaN

#print("SigmaN:",sigmaN)
print("SigmaD:",sigmaD)



statesN = []
for triplet in triplets:
    if triplet[2] not in statesN:
        statesN.append(triplet[2])
    if triplet[4] not in statesN:
        statesN.append(triplet[4])

print("States in NFA (Q_N):",statesN)

statesD = []    # powerset of the set of states of NFA
statesNpowerset = powerset(statesN)
for element in statesNpowerset:
    statesD.append(list(element))
print(statesD)

statesD = powerset(statesN)
print("States in DFA (Q_D):",statesD)
print(powerset([1,2,3]))


