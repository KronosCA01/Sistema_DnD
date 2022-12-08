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

########################## Pregunta 3 ##############################
canvas.create_text(
    443.0,
    197.0,
    anchor="nw",
    text="¿Que caracteristica es la más importante?",
    fill="#000000",
    font=("Inter Black", 24 * -1)
)

cuadro3 = tk.LabelFrame(window)

opcion_seleccionada3 = tk.IntVar()

opcion7 = tk.Radiobutton(cuadro3,
    text = "Fuerza",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada3,
    value = 1)
opcion7.pack()

opcion8 = tk.Radiobutton(cuadro3,
    text = "Destreza",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada3,
    value = 2)
opcion8.pack()

opcion9 = tk.Radiobutton(cuadro3,
    text = "Carisma",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada3,
    value = 3)
opcion9.pack()

cuadro3.pack()
cuadro3.place(x = 443, y=240)

########################## Pregunta 4 ##############################
canvas.create_text(
    443.0,
    370.0,
    anchor="nw",
    text="Que opinas de los linajes",
    fill="#000000",
    font=("Inter Black", 24 * -1)
)

cuadro4 = tk.LabelFrame(window)

opcion_seleccionada4 = tk.IntVar()

opcion10 = tk.Radiobutton(cuadro4,
    text = "El linaje puro es el mejor",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada4,
    value = 1)
opcion10.pack()

opcion11 = tk.Radiobutton(cuadro4,
    text = "Me es indiferente, las acciones valen más",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada4,
    value = 2)
opcion11.pack()

opcion12 = tk.Radiobutton(cuadro4,
    text = "Ser un mestizo te puede dar muchas ventajas",
    bg = "white",
    font = "arial 12",
    width = 35, anchor = tk.W,
    variable = opcion_seleccionada4,
    value = 3)
opcion12.pack()

cuadro4.pack()
cuadro4.place(x = 443, y=410)

def submitForm():
    sigpage()

submit = Button(window,bg = "#06FF1F",text="Resultado", command = submitForm, font =("",36))
submit.place(x = 850, y = 309)

  
    
def sigpage():
    window.destroy()
    window2 = Tk()
    window2.geometry("1198x600")
    window2.configure(bg = "#624D00")
    
    intimidacion = opcion_seleccionada.get()
    sociable = opcion_seleccionada2.get()
    fortaleza = opcion_seleccionada3.get()
    sangre = opcion_seleccionada4.get()
    
    canvas = Canvas(
        window2,
        bg = "#624D00",
        height = 600,
        width = 1198,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        200.0,
        63.0,
        anchor="nw",
        text="La mejor raza para ti es:",
        fill="#2C1800",
        font=("Inter Black", 70 * -1)
    )

    canvas.create_rectangle(
        0.0,
        174.0,
        1199.0,
        185.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        1188.0,
        11.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1188.0,
        0.0,
        1199.0,
        185.0,
        fill="#000000",
        outline="")
    
    canvas.create_rectangle(
        0.0,
        0.0,
        11.0,
        185.0,
        fill="#000000",
        outline="")
    
    if intimidacion == 1 and sangre == 3:
     canvas.create_text(
            513.0,
            185.0,
            anchor="nw",
            text="Semiorco",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="Esta raza es ideal para los jugadores que les gustaria el antiheroe de la\n historia odiados desde que nacen, pero tambien temidos por todos\n los seres con los que se cruza, el repudio que les tienen se deriva\n a que descienden de una relacion de un orco con un humano,\n iracundos por naturaleza y poseen gran poder fisico, el cual\n les ayuda en las batallas",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )
            
 ###############################    
    if intimidacion == 3 and sangre == 3:
     canvas.create_text(
            513.0,
            185.0,
            anchor="nw",
            text="Semielfo",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="Tienen la elegancia de los elfos y la astucia de los humanos unos\n seres equilibrados en muchos aspectos solo los desprecian los elfos\n por no ser sangre pura, agiles y testarudos, grandes acompañantes\n una gran opcion para un personaje versatil con pies ligeros que\n estan listos para afrontar cualquier reto que tenga en su camino",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )
 ###############################    
    if intimidacion == 2 and sangre == 3:
     canvas.create_text(
            551.0,
            185.0,
            anchor="nw",
            text="Tiflin",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="A pesar de ser considerado como un demonio y alguien malvado son\n personajes con los cuales te encantara pasar el rato, parlanchines\n por naturaleza, hacen que las personas alrededor suyo se sientan\n maravillados pero no de dejes engañar estan llenos de trucos,\n un personaje que se puede desenvolver en situaciones extrañas",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )
      
 ###############################    
    if intimidacion == 2 and sangre == 2:
     canvas.create_text(
            534.0,
            185.0,
            anchor="nw",
            text="Gnomo",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="Los guardianes del jardin por excelencia, pequeños guerreros, estas\n criaturas son despreciadas por el tamaño que tienen, un error\n comun a pesar de esto muchas razas los respetan, ya que hacen\n grandes hazañas, para ellos todo es un reto pero nunca retroceden,\n seres incomprendidos, unos aventureros que no tienen comparación ",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )
 ###############################    
    if intimidacion == 1 and sangre == 2:
     canvas.create_text(
            523.0,
            185.0,
            anchor="nw",
            text="Humano",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="No necesitan introducción alguna, el personaje más regular de todos\n a pesar de no poseer caracteristicas destacables como los demás\n su gran ingenio y adaptabilidad los logra posicionar en un nivel muy\n alto, los seres más versatiles para cualquier disciplina los más\n comunes, pero no significa que no sean extraordinarios",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )

 ###############################    
    if intimidacion == 3 and sangre == 2:
     canvas.create_text(
            514.0,
            185.0,
            anchor="nw",
            text="Mediano",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="Si todavia te preguntas que es un mediano,te dare una pista, pies\npeludos, uno de los personajes más queridos de la edad media,\n no por nada destruyeron el anillo que los gobernaba a todos,\n liberando a toda la gente del villano más temido de la tercera era,\n mientras coman su segundo desayuno todo estará bien y gracias\n a sus grandes pies son muy buenos viajeros",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )
     
 ###############################    
    if intimidacion == 1 and sangre == 1:
     canvas.create_text(
            505.0,
            185.0,
            anchor="nw",
            text="Draconido",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="Siendo del linaje de los dragones, estos seres demuestran un gran\n orgullo de sus raices, intimidantes por su piel llena de escamas,\n ojos que parecen verte el alma y un aliento elemental poderoso\n dependiendo de que dragon sean descendientes, aunque no\n tengan alas son grandes aventureros listos para el combate",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )  
     
 ###############################    
    if intimidacion == 2 and sangre == 1:
     canvas.create_text(
            564.0,
            185.0,
            anchor="nw",
            text="Elfo",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="Seres orgullosos con aires de grandeza, se sienten superiores a todos\n mucha gente les tiene odio porque siempre los tratan de plebeyos,\n son muy agiles en la batalla y grandes estrategas, son reconocidos\n por ser grandes arqueros, ligeros como pluma y tienen una belleza\n que atrapa a más de una especie, una raza extravagante",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )   
     
 ###############################    
    if intimidacion == 3 and sangre == 1:
     canvas.create_text(
            542.0,
            185.0,
            anchor="nw",
            text="Enano",
            fill="#000000",
            font=("Inter Black", 50 * -1)
        )
     
     canvas.create_text(
            0.0,
            250.0,
            anchor="nw",
            text="Además de ser los acompañantes para princesas blancas como\n la nieve, son los mineros por excelencia y formidables herreros, sus\n enemigos de toda la vida son los elfos, es tan antigua la rivalidad\n que ya no se sabe a ciencia cierta porque se odian entre ellos,\n buenos combatientes y la bebida es su deporte favorito",
            fill="#000000",
            font=("Inter Black", 40 * -1)
        )  
                         
window.resizable(False, False)
window.mainloop()
