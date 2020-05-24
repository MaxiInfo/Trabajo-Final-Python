import PySimpleGUI as sg
import Configuraciones as config
import Tablero_Definitivo.py as board
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

configs = {'name':'Player','timing':20,'dificultad':'medio'}

window = sg.Window('ScrabbleAR', layout_main_menu,size=(300,300))
event, values= window.read()
while True:
    if event in (None,'Salir'):
        break
    elif event in ('Jugar'):
        window.close()
        event = board.main(configs)
    elif event in ('Continuar'):
        window.close()
        #FAALTAAAAAAAAAAAAAAAAAAAAAAAAaaaa
        board.main()
    elif event in ('Configuracion'):
        window.close()
        configs = config.main()
    elif event in ('TOP 10'):
        window.close()
        event = top.main()
        if event in (None):
            break
    window = sg.Window('ScrabbleAR', layout_main_menu,size=(300,300))
    event, values= window.read()