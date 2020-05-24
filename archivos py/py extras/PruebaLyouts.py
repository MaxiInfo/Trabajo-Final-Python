import PySimpleGUI as sg
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

layout_configs = [
    [sg.Text('configuraciones',size=(100,1),font=(None,15),justification='center')],
    [sg.Text('nombre del jugador',size=(100,1),justification='center')],
    [sg.Text(' '*16),sg.InputText(size=(15,1))],
    [sg.Text('tiempo de juego',size=(100,1),justification='center')],
    [sg.Text(' '*23),sg.InputCombo(('1','5','10','20',),size=(5,1),default_value='10')],
    [sg.Text('dificultad',size=(100,1),justification='center')],
    [sg.Text(' '*24),sg.Radio('facil','Dificultad',default=False,size=(10,1))],
    [sg.Text(' '*23),sg.Radio('medio','Dificultad',default=True,size=(10,1))],
    [sg.Text(' '*23),sg.Radio('dificil','Dificultad',default=False,size=(10,1))],
    [sg.Text(' '*50),sg.Button('atras')]
    ]

layout_top = [
    [sg.Text('TOP 10',size=(100,1),font=(None,15),justification='center')],
    [sg.Text('')],
    [sg.Text(' '*15),sg.Button('facil',size=(15,2))],
    [sg.Text(' '*15),sg.Button('normal',size=(15,2))],
    [sg.Text(' '*15),sg.Button('dificil',size=(15,2))],
    [sg.Text('')],
    [sg.Text(' '*15),sg.Button('atras',size=(15,2))],
    ]

layout_tablero = [
    
    ]


window = sg.Window('ScrabbleAR', layout_main_menu,size=(300,300))

while True:
    event, values= window.read()
    if event in (None,'Salir'):
        break
    elif event in ('Jugar'):
        window.close()
        window = sg.Window('ScrabbleAR',layout_tablero,size=(300,300))
    elif event in ('Continuar'):
        window.close()
        window = sg.Window('ScrabbleAR',layout_tablero,size=(300,300))
    elif event in ('Configuracion'):
        window.close()
        window = sg.Window('ScrabbleAR',layout_configs,size=(300,300))
    elif event in ()

