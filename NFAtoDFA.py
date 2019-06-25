# Encoding: UTF-8
# Authors: Javier Martínez Hernández, Roberto Téllez Perezyera
"""
This program is rlly cool thks for using it
"""
import sys
from collections import defaultdict
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


sigmaN = []
for x in range(0, len(triples)):
    if triples[x][0]not in sigmaN:
        sigmaN.append(triples[x][0])

sigmaD = sigmaN

#print("SigmaN:",sigmaN)
print("SigmaD:",sigmaD)



statesN = []
for x in range(0,len(triples)):
    if triples[x][1]not in statesN:
        statesN.append(triples[x][1])

print("States in NFA (Q_N):",statesN)

statesD = []    # powerset of the set of states of NFA
statesNpowerset = powerset(statesN)
for element in statesNpowerset:
    statesD.append(list(element))
print("states of DFA (power set)",statesD)


#states accepted
statesAcceptD = []
for x in range(0,len(statesD)):
    if len(statesD[x])>0:
        for y in range(0,len(statesD[x])):
            if statesD[x][y] == statesN[-1]:
                statesAcceptD.append(statesD[x])

print("States accepted in DFA (Q_D):",statesAcceptD)
delta = defaultdict(list)
key = ""
for input,exit,destination in triples:
    if input == "0":
        index = 0
    elif input == "1":
        index = 1
    else:
        entry = -1
        index = -1

    if exit not in delta:
        delta[exit] = [[],[]]
    delta[exit][index].append(destination)

print("Delta:",delta)