import PySimpleGUI as sg
import time
class Tablero ():
    import PySimpleGUI as sg
    import time
    
    def set_layout(configs):
        #configs = {'name':values[0],'timing':values[1],'dificultad':'facil'if values[2] else 'medio' if values[3]else 'dificil'}
        MAX_ROWS = MAX_COL = 15
        board = [[0 for j in range(MAX_COL)] for i in range(MAX_ROWS)]
        atril = [0 for n in range(7)]

        col = [[sg.Button('Empezar')],
            [sg.Button('Posponer')],
            [sg.Text('Tiempo restante')],
            [sg.Text(' ', size= (8, 1), key = ("-CLK"))],
            [sg.Text('Hello itese me', size= (8, 10), key= ("-MESSAGE-"))],
            [sg.Text('Tiempo de jugada')],
            [sg.Text(' ', size= (8,1), key = ("-TURN-"))]
        ]

        col2= [[sg.Button(' ', size=(4, 2), key=("-row"+str(i)+"-","-col"+str(j)+"-"), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

        col3= [[sg.Button('', size=(4, 2), key=("-USERB" + str(n) + "-"), pad=(0,0)) for n in range(7)] for m in range(1)]
                
        layout_tablero = [
            [sg.Text('COMPUTADORA'), sg.Text('', size=(30, 1), background_color = 'Brown', relief=sg.RELIEF_RIDGE)],
            [sg.Column(col2), sg.Column(col)],
            [sg.Text(configs['name'], key = ("-NOMBRE-")), sg.Column(col3), sg.Button('Comprobar'), sg.Button('Pasar'),sg.Text(' '*40),sg.Button('salir')]   
        ]
        return layout_tablero


    def table_on(window):
        pass
    def sabe_table():
        pass