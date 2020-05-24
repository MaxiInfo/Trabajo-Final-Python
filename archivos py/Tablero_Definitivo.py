import PySimpleGUI as sg
import time

MAX_ROWS = MAX_COL = 15
board = []  #[0 for j in range(MAX_COL)] for i in range(MAX_ROWS)]
atril = []   #0 for n in range(7)]

col = [[sg.Button('Empezar')],
       [sg.Button('Posponer')],
       [sg.Text('Tiempo restante')],
       [sg.Text(' ', size= (8, 1), key = ("-CLK"))],
       [sg.Text(' ', size= (8, 10), key= ("-MESSAGE-"))],
       [sg.Text('Tiempo de jugada')],
       [sg.Text(' ', size= (8,1), key = ("-TURN-"))]
]

col2= [[sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

col3= [[sg.Button('', size=(4, 2), key=("-USERB" + str(n) + "-"), pad=(0,0)) for n in range(7)] for m in range(1)]

layout_tablero = [
    [sg.Text('COMPUTADORA'), sg.Text('', size=(30, 1), background_color = 'Brown', relief=sg.RELIEF_RIDGE)],
    [sg.Column(col2), sg.Column(col)],
    [sg.Text('JUGADOR', key = ("-NOMBRE-")), sg.Column(col3), sg.Button('Comprobar'), sg.Button('Pasar')]   
]

window = sg.Window('ScrabbleAR', layout_tablero, size=(750,750))

event, values = window.read()
window.close()