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

participantes_restantes = list(participantes)  # Lista de participantes restantes

def sorteo():
    # Desactivar el botón durante el sorteo
    boton_sorteo.config(state=DISABLED)

    if participantes_restantes:
        ganador = random.choice(participantes_restantes)
        participantes_restantes.remove(ganador)  # Eliminar el ganador de la lista de participantes restantes
        nivel = random.randint(1, 5)
        resultado.configure(text=f"Ganador: {ganador}\nNivel de furro: {nivel}")
    else:
        resultado.configure(text="Juego completado. Reiniciando...")
        participantes_restantes.extend(participantes)  # Restaurar la lista de participantes restantes

    # Reactivar el botón después del sorteo
    boton_sorteo.config(state=NORMAL)

root = Tk()
root.title("Sorteo de nivel de furro")
root.geometry("400x150")  # Ajustar el tamaño de la ventana

boton_sorteo = Button(root, text="Realizar Sorteo", command=sorteo)
boton_sorteo.pack(pady=10)

resultado = Label(root, text="", font=("Arial", 18))
resultado.pack()

root.mainloop()