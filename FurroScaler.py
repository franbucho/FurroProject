import random
from tkinter import *

participantes = [
    "Francisco Alvarado",
    "Lucas Lacerda",
    "Irina Lapegna",
    "Santiago Kitashima",
    "Lautaro Bensoni",
    "Jimmy Nils",
    "Brendiña",
    "Tomas Gus",
    "Niconeitor",
    "Facundo Perez"
]

def sorteo():
    ganador = random.choice(participantes)
    nivel = random.randint(0, 5)
    resultado.configure(text=f"Ganador: {ganador}\nNivel de furro: {nivel}")

root = Tk()
root.title("Sorteo de nivel de furro")

boton_sorteo = Button(root, text="Realizar Sorteo", command=sorteo)
boton_sorteo.pack(pady=10)

resultado = Label(root, text="")
resultado.pack()

root.mainloop()