import PySimpleGUI as sg
from string import ascii_uppercase as up
from random import choice
letrasRandom = lambda : [choice(up) for i in range(5)]
a=letrasRandom()


tam_celda =25
color_button = ('white','green')
tam_button = 10,5
button = lambda name : sg.Button(name,button_color=color_button,size=tam_button)
layout = [
        [sg.Graph((500,500),(0,260),(260,0), key='_GRAPH_', background_color='white',change_submits=True, drag_submits=False)],
        #[button("A"),button("E"),button("I"),button("O"),button("U")],
        [button(i) for i in a],
        [sg.Button("Evaluar")]]
window = sg.Window('Ejercicio1', ).Layout(layout).Finalize()
g = window.FindElement('_GRAPH_')

matriz=[]
selected=[]
text_box=[]
for i in range(0,10):
    matriz.append([0]*10)
    selected.append([False]*10)
    text_box.append([""]*10)

for row in range(10):
        for col in range(10):
            matriz[row][col]=g.DrawRectangle((col * tam_celda + 5, row * tam_celda + 3), 
                                            (col * tam_celda + tam_celda + 5, row * tam_celda + tam_celda + 3),
                                            line_color='black')

#print(matriz)

Check_box = lambda x,y : g.TKCanvas.itemconfig(matriz[box_y][box_x], fill="#CFF5E3")
Uncheck_box = lambda x,y: g.TKCanvas.itemconfig(matriz[box_y][box_x], fill="white")
despintar = lambda x: g.TKCanvas.itemconfig(x, fill="white")

Check_button = lambda x: window.FindElement(x).Update(button_color=('white','blue'))
Uncheck_button = lambda x: window.FindElement(x).Update(button_color=('white','green'))
current_Check_button = ''

word=''

button_selected = False
current_button_selected = ''
while True:
    event, values = window.Read()
    print(values)
    if event is None or 'tipo' == 'Exit':
        break
    if event == "Evaluar":
        from pattern.es import *
        print(parse(word).split('/'))
    if event == '_GRAPH_':
        if values['_GRAPH_'] == (None,None):
            continue
        mouse = values["_GRAPH_"]
        box_x = mouse[0]//tam_celda
        box_y = mouse[1]//tam_celda
        if mouse == (None, None) or box_x > 9 or box_y > 9:
            continue
        if button_selected: # logica de boton
            current_Check_button = box_x,box_y
            Check_box(box_x,box_y)
            selected[box_x][box_y]=True
            if text_box[box_x][box_y]=="":
                text_box[box_x][box_y] = g.DrawText(current_button_selected, (box_x * tam_celda + 18, box_y * tam_celda + 17))
                word+=current_button_selected
            else:
                # aca iria la actualizacion del cuadrado pero no me sale
                print(text_box[box_x][box_y])
                g.TKCanvas.itemconfig(text_box[box_y][box_x],text="")
                print((g.TKCanvas.itemconfigure(text_box[box_y][box_x])))
    else:
        if button_selected:
            if event == current_button_selected:
                Uncheck_button(event)
                button_selected = False
                current_button_selected = ''
        else:
            Check_button(event)
            button_selected = True
            current_button_selected = event