import PySimpleGUI as sg
import Configuraciones as config
import Tablero_2 as board
import Top10 as top
layout_main_menu = [
    [sg.Text('ScrabbleAR',size=(100,1),justification='center',background_color='black',font=('Arial',20))],
    [sg.Text('')],
    [sg.Text(' '*18),sg.Button('Jugar',size=(12,2))],
    [sg.Text(' '*18),sg.Button('Continuar',size=(12,2))],
    [sg.Text(' '*18),sg.Button('Configuracion',size=(12,2))],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Button('TOP 10',size=(12,2)),sg.Text(' '*10),sg.Button('Salir',size=(12,2))],
    ]

window = sg.Window('ScrabbleAR', layout_main_menu,size=(300,300))

while True:
    event, values= window.read()
    if event in (None,'Salir'):
        break
    elif event in ('Jugar'):
        window.close()
        Tablero_2.
    elif event in ('Continuar'):
        window.close()
        window = sg.Window('ScrabbleAR',layout_tablero,size=(300,300))
    elif event in ('Configuracion'):
        window.close()
        window = sg.Window('ScrabbleAR',layout_configs,size=(300,300))