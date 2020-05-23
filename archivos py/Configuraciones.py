import PySimpleGUI as sg

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