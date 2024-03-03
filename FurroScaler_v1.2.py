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

participantes_restantes = list(participantes)  # Lista de participantes

def sorteo():
    # Desactivar el botón
    boton_sorteo.config(state=DISABLED)

    if participantes_restantes:
        ganador = random.choice(participantes_restantes)
        participantes_restantes.remove(ganador)  # Eliminar el ganador
        nivel = random.randint(1, 5)
        resultado.configure(text=f"Ganador: {ganador}\nNivel de furro: {nivel}")
        contador.configure(text=f"Participantes restantes: {len(participantes_restantes)}")
    else:
        resultado.configure(text="Juego completado. Reiniciando...")
        participantes_restantes.extend(participantes)  # Restaurar la lista 
        contador.configure(text="Participantes restantes: 10")  # Restablecer el contador

    # Reactivar el botón
    boton_sorteo.config(state=NORMAL)

root = Tk()
root.title("Sorteo de nivel de furro")
root.geometry("400x250")  # Ajustar 

boton_sorteo = Button(root, text="Realizar Sorteo", command=sorteo)
boton_sorteo.pack(pady=10)

resultado = Label(root, text="", font=("Arial", 18))
resultado.pack()

contador = Label(root, text="Participantes restantes: 10", font=("Arial", 12))
contador.pack()

root.mainloop()