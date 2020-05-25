import PySimpleGUI as sg
import time
class Tablero ():
    import PySimpleGUI as sg
    import time
    

    def set_layout(configs):
    
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

        col2= [[sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

        col3= [[sg.Button('', size=(4, 2), key=("-USERB" + str(n) + "-"), pad=(0,0)) for n in range(7)] for m in range(1)]
                
        layout_tablero = [
            [sg.Text('COMPUTADORA'), sg.Text('', size=(30, 1), background_color = 'Brown', relief=sg.RELIEF_RIDGE)],
            [sg.Column(col2), sg.Column(col)],
            [sg.Text(configs['name'], key = ("-NOMBRE-")), sg.Column(col3), sg.Button('Comprobar'), sg.Button('Pasar'),sg.Text(' '*40),sg.Button('salir')]   
        ]
        return layout_tablero

    def table_on (window):
    
        triple_letter = ((1,5),(1,9),(5,1),(5,5),(5,9),(5,13),(9,1),(9,5),(9,9),(9,13),(13,5),(13,9))
        double_letter = ((0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,9),(14,3),(14,11))

        double_word = ((1,1),(2,2),(3,3),(4,4),(1,13),(2,12),(3,11),(4,10),(13,1),(12,2),(11,3),(10,4),(10,10),(11,11),(12,12),(13,13))
        triple_word = ((0,0),(0,7),(0,14),(7,0),(7,14),(14,0),(14,7),(14,14))
    
        start_button = (7,7)

        MAX_ROWS = MAX_COL = 15

        for i in range(MAX_ROWS):
            for j in range(MAX_COL):
                if (i,j) in triple_letter:
                    window.FindElement((i,j)).Update('TL')
                elif (i,j) in double_letter:
                    window.FindElement((i,j)).Update('DL')
                elif (i,j) in triple_word:
                    window.FindElement((i,j)).Update('TW')
                elif (i,j) in double_word:
                    window.FindElement((i,j)).Update('DW')
                elif (i,j) is start_button:
                    window.FindElement((i,j)).Update('ST') #no anda
                else:
                    window.FindElement((i,j)).Update('')
        pass

    def calc_puntaje():
        pass

    def sabe_table():
        pass