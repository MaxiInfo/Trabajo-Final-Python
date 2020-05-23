import PySimpleGUI as sg
layout_main_menu = [
    [sg.Text('ScrabbleAR',size=(100,1),justification='center')],
    [sg.Text('')],
    [sg.Text('                  '),sg.Button('Jugar',size=(12,2))],
    [sg.Text('                  '),sg.Button('Continuar',size=(12,2))],
    [sg.Text('                  '),sg.Button('Configuracion',size=(12,2))],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Button('TOP 10',size=(12,2)),sg.Text('          '),sg.Button('Salir',size=(12,2))],
    ]

layout_configs = [
    [sg.Text('configuraciones',size=(100,1),font=(None,15),justification='center')],
    [sg.Text('nombre del jugador',size=(100,1),justification='center')],
    [sg.Text('                '),sg.InputText(size=(15,1))],
    [sg.Text('tiempo de juego',size=(100,1),justification='center')],
    [sg.Text('           '),sg.InputCombo(('1','5','10','20',),size=(20,1),default_value='10')],
    [sg.Text('dificultad',size=(100,1),justification='center')],
    [sg.Text('                      '),sg.Radio('facil','Dificultad',default=False,size=(10,1))],
    [sg.Text('                      '),sg.Radio('medio','Dificultad',default=True,size=(10,1))],
    [sg.Text('                      '),sg.Radio('dificil','Dificultad',default=False,size=(10,1))],
    [sg.Text('                                                   '),sg.Button('atras')]
    ]

layout_top = [
    [sg.Text('TOP 10',size=(100,1),font=(None,15),justification='center')],
    [sg.Text('')],
    [sg.Text('               '),sg.Button('facil',size=(15,2))],
    [sg.Text('               '),sg.Button('normal',size=(15,2))],
    [sg.Text('               '),sg.Button('dificil',size=(15,2))],
    [sg.Text('')],
    [sg.Text('               '),sg.Button('atras',size=(15,2))],
    ]

layout_tablro = [
    
    ]

window = sg.Window('ScrabbleAR', layout_top,size=(300,300))
x = window.read()
