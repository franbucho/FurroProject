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
    # Desactivar el botón 
    boton_sorteo.config(state=DISABLED)

    # animacion
    for _ in range(10):
        ganador = random.choice(participantes)
        resultado.configure(text=ganador)
        resultado.update()
        resultado.after(100)

    # Asignar el ganador 
    ganador = random.choice(participantes)
    nivel = random.randint(0, 5)
    resultado.configure(text=f"Ganador: {ganador}\nNivel de furro: {nivel}")

    # Reactivar
    boton_sorteo.config(state=NORMAL)

root = Tk()
root.title("Sorteo de nivel de furro")

boton_sorteo = Button(root, text="Realizar Sorteo", command=sorteo)
boton_sorteo.pack(pady=10)

resultado = Label(root, text="", font=("Arial", 18))
resultado.pack()

root.mainloop()