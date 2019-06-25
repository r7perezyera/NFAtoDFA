# Encoding: UTF-8
# Authors: Javier Martínez Hernández, Roberto Téllez Perezyera
"""
This program is rlly cool thks for using it
"""
import sys
it = iter(sys.stdin.read().splitlines())



def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


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

#print("SigmaN:",sigmaN)
print("SigmaD:",sigmaD)



statesN = []
for triplet in triplets:
    if triplet[2] not in statesN:
        statesN.append(triplet[2])
    if triplet[4] not in statesN:
        statesN.append(triplet[4])

print("States in NFA (Q_N):",statesN)


statesD = powerset(statesN)
print("States in DFA (Q_D):",statesD)
print(powerset([1,2,3]))


