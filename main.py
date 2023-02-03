from tkinter import *

# ma fenetre
fen = Tk()
fen.title("mon télécran")
fen.geometry("600x600")
# mon interface
can = Canvas(fen, width=600, height=600, bg="white")
can.grid(column=0, row=0, columnspan=10, rowspan=10)
# mes boutons
Button(fen, text="HAUT").grid(column=0, row=0)
Button(fen, text="BAS").grid(column=0, row=1)
Button(fen, text="GAUCHE").grid(column=0, row=2)
Button(fen, text="DROITE").grid(column=0, row=3)
Button(fen, text="NOIR").grid(column=0, row=4)
Button(fen, text="ROUGE").grid(column=0, row=5)
# mes variables
x = 200
y = 200
couleur = "black"

fen.mainloop()
