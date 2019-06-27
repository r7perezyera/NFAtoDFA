# Encoding: UTF-8
# Authors: Javier Martínez Hernández, Roberto Téllez Perezyera
"""
This program implements an algorithm to convert an NFA to a DFA
It receives the NFA as a set of 3-tuples, and outputs the formal description
of its equivalent DFA
"""
import sys
from collections import defaultdict
from itertools import chain, combinations
#from tabulate import tabulate

fileToRead = input("Teclee el nombre del archivo: ")

it = open(fileToRead, "r")
out=open("output.txt","w")
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
out.write("SigmaD: %s\n" %(sigmaD))



statesN = []
for x in range(0,len(triples)):
    if triples[x][1]not in statesN:
        statesN.append(triples[x][1])

out.write("States in NFA (Q_N): %s\n" %(statesN))

statesD = []    # powerset of the set of states of NFA
statesNpowerset = powerset(statesN)
for element in statesNpowerset:
    statesD.append(list(element))
out.write("states of DFA (power set): %s\n" %(statesD))


#states accepted
statesAcceptD = []
for x in range(0,len(statesD)):
    if len(statesD[x])>0:
        for y in range(0,len(statesD[x])):
            if statesD[x][y] == statesN[-1]:
                statesAcceptD.append(statesD[x])
out.write("States accepted in DFA (Q_D): %s\n "%(statesAcceptD))

#first state
out.write("First state in DFA: %s\n"%(statesD[1]))

#delta first part
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

#print("Delta:",delta)


header = ["q","0","1"]
rows = []

for qi in statesD:
    row = [qi, [], []]
    for state in qi:
        for i in delta[state][0]:
            row[1].append(i)
        for i in delta[state][1]:
            row[2].append(i)
        row[1] = list(set(row[1]))
        row[2] = list(set(row[2]))
    rows.append(row)

#print(rows)
#
out.write("\n Transition table: \n")
out.write("%s\n"%(header))
out.write("_________________________________\n")
for x in range(0,len(rows)):
    out.write("%s \n"%(rows[x]))
out.close()
print("El archivo se ha escrito exitosamente. Revise la carpeta del proyecto.\nFin.")
