import PySimpleGUI as sg
import Configuraciones as config
import Tablero as board
import Top10 as top

layout_main_menu = [
    [sg.Text('ScrabbleAR',size=(100,1),justification='center',background_color='black',font=('Arial',20))],
    [sg.Text('')],
    [sg.Text(' '*18),sg.Button('Jugar',size=(12,2))],
    [sg.Text(' '*18),sg.Button('Continuar',size=(12,2))],
    [sg.Text(' '*18),sg.Button('Configuracion',size=(12,2))],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Button('TOP 10',size=(12,2)),sg.Text(' '*10),sg.Button('Salir',size=(12,2))]
    ]

configs = dict({'name':'Player','timing':20,'dificultad':'facil','modsBolsa':None})


window_menu = sg.Window('ScrabbleAR', layout_main_menu,size=(300,300))
event, values= window_menu.read()
while True:
    if event in (None,'Salir'):
        break
    elif event == 'Jugar':
        window_menu.hide()
        event = board.main(configs)
    elif event == 'Continuar':
        window_menu.close()
        #FAALTAAAAAAAAAAAAAAAAAAAAAAAAaaaa
        #event = board.main(configs)
    elif event in ('Configuracion'):
        window_menu.hide()
        event,configs = config.main(configs)
    elif event == 'TOP 10':
        window_menu.hide()
        event = top.main()
    if event == None:
        break
    window_menu.un_hide()
    event, values= window_menu.read()