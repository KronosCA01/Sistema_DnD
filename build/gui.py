from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\Tareas\7mo Semestre\Sistema experto\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1198x600")
window.configure(bg = "#624D00")


canvas = Canvas(
    window,
    bg = "#624D00",
    height = 600,
    width = 1198,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    412.0,
    62.0,
    anchor="nw",
    text="Tu personaje en D&D",
    fill="#2C1800",
    font=("Inter Black", 50 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    175.0,
    92.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    174.0,
    1198.0,
    185.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    11.0,
    0.0,
    1187.0,
    11.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1187.0,
    0.0,
    1198.0,
    185.0,
    fill="#000000",
    outline="")


##########################Pregunta 1##############################

canvas.create_text(
    17.0,
    197.0,
    anchor="nw",
    text="¿Quieres intimidar a las personas?",
    fill="#000000",
    font=("Inter Black", 24 * -1)
)

cuadro1 = tk.LabelFrame(window)

opcion_seleccionada = tk.IntVar()

opcion1 = tk.Radiobutton(cuadro1,
    text = "Si, quiero que se asusten solo con verme",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada,
    value = 1)
opcion1.pack()

opcion2 = tk.Radiobutton(cuadro1,
    text = "Quiero que la gente me respete",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada,
    value = 2)
opcion2.pack()

opcion3 = tk.Radiobutton(cuadro1,
    text = "Prefiero no ser el centro de atención  ",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada,
    value = 3)
opcion3.pack()

cuadro1.pack()
cuadro1.place(x = 17, y=240)

##########################Pregunta 2##############################
canvas.create_text(
    17.0,
    370.0,
    anchor="nw",
    text="¿Como tratarias a los demas?",
    fill="#000000",
    font=("Inter Black", 24 * -1)
)

cuadro2 = tk.LabelFrame(window)

opcion_seleccionada2 = tk.IntVar()

opcion4 = tk.Radiobutton(cuadro2,
    text = "Trato de ser amigo de todos",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada2,
    value = 1)
opcion4.pack()

opcion5 = tk.Radiobutton(cuadro2,
    text = "Soy cordial, por educación",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada2,
    value = 2)
opcion5.pack()

opcion6 = tk.Radiobutton(cuadro2,
    text = "La gente me odia solo por existir",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada2,
    value = 3)
opcion6.pack()

cuadro2.pack()
cuadro2.place(x = 17, y=410)

##########################Pregunta 3##############################
canvas.create_text(
    443.0,
    197.0,
    anchor="nw",
    text="Pregunta 3:",
    fill="#000000",
    font=("Inter Black", 24 * -1)
)

cuadro3 = tk.LabelFrame(window)

opcion_seleccionada3 = tk.IntVar()

opcion7 = tk.Radiobutton(cuadro3,
    text = "Si, quiero que se asusten solo con verme",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada3,
    value = 1)
opcion7.pack()

opcion8 = tk.Radiobutton(cuadro3,
    text = "Quiero que la gente me respete",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada3,
    value = 2)
opcion8.pack()

opcion9 = tk.Radiobutton(cuadro3,
    text = "Prefiero no ser el centro de atención  ",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada3,
    value = 3)
opcion9.pack()

cuadro3.pack()
cuadro3.place(x = 443, y=240)

##########################Pregunta 4##############################
canvas.create_text(
    443.0,
    370.0,
    anchor="nw",
    text="Pregunta 4:",
    fill="#000000",
    font=("Inter Black", 24 * -1)
)

cuadro4 = tk.LabelFrame(window)

opcion_seleccionada4 = tk.IntVar()

opcion10 = tk.Radiobutton(cuadro4,
    text = "Si, quiero que se asusten solo con verme",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada4,
    value = 1)
opcion10.pack()

opcion11 = tk.Radiobutton(cuadro4,
    text = "Quiero que la gente me respete",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada4,
    value = 2)
opcion11.pack()

opcion12 = tk.Radiobutton(cuadro4,
    text = "Prefiero no ser el centro de atención  ",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada4,
    value = 3)
opcion12.pack()

cuadro4.pack()
cuadro4.place(x = 443, y=410)




window.resizable(False, False)

window.resizable(False, False)
window.mainloop()
