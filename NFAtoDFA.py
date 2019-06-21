# Encoding: UTF-8
# Authors: Javier Martínez Hernández, Roberto Téllez Perezyera
"""
This program is rlly cool thks for using it
"""
import sys
it = iter(sys.stdin.read().splitlines())

# read input and create a list of triplets
triplets = next(it).split("),(")
triplets[0] = triplets[0][2::]
triplets[-1] = triplets[-1][:-2:]
print(triplets)



sigmaN = []

for triplet in triplets:
    if triplet[0] not in sigmaN:
        sigmaN.append(triplet[0])

# should we int them tho?
# this block does not work
for symbol in sigmaN:
    int(symbol)

sigmaD = sigmaN

print("SigmaN:",sigmaN)
print("Thus, sigmaD:",sigmaD)



