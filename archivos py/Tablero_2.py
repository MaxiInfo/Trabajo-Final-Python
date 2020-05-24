import PySimpleGUI as sg
import time

MAX_ROWS = MAX_COL = 15
board = []  #[0 for j in range(MAX_COL)] for i in range(MAX_ROWS)]
atril = []   #0 for n in range(7)]

col = [[sg.Button('Empezar', size = (8,2), key = ("-BEGIN-"))],
       [sg.Button('Posponer')],
       [sg.Text('Tiempo restante')],
       [sg.Text(' ', size= (8, 1), key = ("-CLK"))],
       [sg.Text(' ', size= (8, 10), key= ("-MESSAGE-"))],
       [sg.Text('Tiempo de jugada')],
       [sg.Text(' ', size= (8,1), key = ("-TURN-"))]
]

col2= [[sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

col3= [[sg.Button('', button_color= ('white', '#1B4F72'), size=(4, 2), key=("-USERB" + str(n) + "-"), pad=(0,0)) for n in range(7)] for m in range(1)]

layout_tablero = [
    [sg.Text('COMPUTADORA', font = 'Helvetica 15'), sg.Text('', size=(30, 2), background_color = '#1B4F72', relief=sg.RELIEF_RIDGE)],
    [sg.Column(col2), sg.Column(col)],
    [sg.Text('JUGADOR', key = ("-NOMBRE-"), font = ('Helvetica 15')), sg.Column(col3), sg.Button('Comprobar'), sg.Button('Pasar')]   
]

window = sg.Window('ScrabbleAR', layout_tablero, size=(750,750), resizable= True)


while True:
    event, values = window.read()
    print(event,values)
    if event == None:
        break
    if event in ('Empezar'):
        #reparte las fichas, empiezan a correr los relojes y decide quien empieza (lo podria avisar en los mensajes)
        info_dificultad = datos_nivel() # que obtenga los datos del nivel para la bolsa, el tiempo, etc
        letras_jugador = fj.repartir_letras(bolsa, 7) #podriamos usar esta misma funcion para repartir siempre,
    if event in (None, 'Posponer'):
        #guarda los datos en un archivo y vuelve al menu principal
        break
    
    
window.close()