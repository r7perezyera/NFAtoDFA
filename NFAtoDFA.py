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
from tkinter import *
from tkinter import messagebox, filedialog

# it = iter(sys.stdin.read().splitlines())


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def init():
    # Do the GUI - Homescreen
    window = Tk()
    window.title("1st term project - Luis / Roberto")
    window.geometry("600x600")
    ANCHO = 600
    ALTO = 600
    window.attributes('-topmost', False)

    tagInfo = Label(window, text="Javier Martínez Hernández - A01375496\n"
                                 "Roberto Téllez Perezyera - A01374866", justify=RIGHT).place(x=ANCHO - 345, y=5)
    tag1 = Label(window, text="Bienvenido.").place(x=10, y=60)
    tag2 = Label(window,
                 text="A continuación podrá cargar el archivo de texto con el NFA que desea convertir a DFA.").place(
        x=10, y=90)
    tag3 = Label(window, text="Haga click en Start para iniciar.").place(x=10, y=120)
    tag4 = Label(window,
                 text="Aparecerá un prompt para abrir el archivo de texto.").place(
        x=10, y=150)
    tagn = Label(window, text="Puede cerrar esa nueva ventana y repetir el proceso desde esta ventana para la\n"
                              "segunda prueba.").place(x=10, y=180)
    tagn1 = Label(window, text="Click on Quit on the lower right corner to close this window.").place(x=10, y=265)

    startButton = Button(window, text="Start",command=aiDiseGratis ).place(x=(ANCHO // 2) - 30, y=ALTO // 2)
    exitButton = Button(window, text="Quit", command=window.quit).place(x=540, y=565)

    window.mainloop()


def aiDiseGratis():
    # we DON'T want home window at the very top anymore
    inputFilePath = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),  # path to file 1
                                                  ("All files", ".")))
    global inputFromGUI
    inputFromGUI = open(inputFilePath, 'r')#.readlines()

    messagebox.showinfo("Success", "File has been read.")
    messagebox.showinfo("See your output", "Puede encontrar el archivo .txt con el output en el mismo folder"
                                           " donde está este archivo .py :).")

    solutionWindow = Tk()
    solutionWindow.title("Solutions")
    solutionWindow.geometry("1000x840")


    tagTextbook = Label(solutionWindow, text="Textbook solution", justify=LEFT).grid(row=1, column=1)

    tagMultipCountTe = Label(solutionWindow, text="number of scalar multiplications: %d" % (1.0),
                             justify=LEFT).grid(row=2,
                                                column=1)
    tagStrassen = Label(solutionWindow, text="Textbook solution", justify=LEFT).grid(row=3, column=1)

    tagMultipCountStrassen = Label(solutionWindow,
                                   text="number of scalar multiplications: %d" % (2.0),
                                   justify=LEFT).grid(row=4,
                                                      column=1)
    tagFilePath = Label(solutionWindow, text="Matrix C is found at: %s" % ("the folder"), justify=LEFT).grid(row=5, column=1)

    solutionWindow.mainloop()



#fileToRead = input("Teclee el nombre del archivo: ")
init()

#it = open(fileToRead, "r")
out=open("output.txt","w")


# read input and create a list of triplets
#triplets = next(it).split("),(")
triplets = next(inputFromGUI).split("),(")
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
print("El archivo se ha escrito exitosamente. Revise la carpeta del proyecto.\n"
      "Este programa ha finalizado.")

init()
