import PySimpleGUI as sg
import time
import Class_administrador as administrador


class Tablero ():
    def __init__(self,lista_tuplas):
        self._MAX_ROWS = 15
        self._MAX_COL = 15
        self.board = [[0 for j in range(self._MAX_COL)]
                      for i in range(self._MAX_ROWS)]
        self.atril = [0 for n in range(7)]
        self.triple_letter = lista_tuplas[3]
        self.double_letter = lista_tuplas[2]
        self.double_word = lista_tuplas[0]
        self.triple_word = lista_tuplas[1]
        self.R10 = lista_tuplas[4]
        self.R20 = lista_tuplas[5]
        self.start_button = (7, 7)
        self.time_left = 0
        self.time_game = 0
        self.turn = 0
        pass

    def get_triple_letter(self):
        return self.triple_letter
    def get_double_letter(self):
        return self.double_letter
    def get_double_word(self):
        return self.double_word
    def get_triple_word(self):
        return self.triple_word
    def get_start_button(self):
        return self.start_button
    def get_r10(self):
        return self.R10
    def get_r20(self):
        return self.R20
    def set_time_left(self, timeleft):
        self.time_left = timeleft
    def set_time_game(self, timegame):
        self.time_game = timegame
    def set_turn(self, timeturn):
        self.turn = timeturn
    
    def get_time_game(self):
        return self.time_game
    def get_time_left(self):
        return self.time_left
    def get_turn(self):
        return self.turn

    def get_board(self):
        return self.board

    def mod_board(self, tuplas, palabra):
        #actualiza la matriz, la lista de tuplas son las posiciones de las letras
        k = 0
        for i,j in tuplas:
            self.board[i][j] = palabra[k]
            k += 1
        

    def set_layout(self, configs):
        col = [[sg.Button('Empezar')],
               [sg.Button('Posponer')],
               [sg.Button('Menu principal',key='-mainMenu-')],
               [sg.Text('Tiempo restante')],
               [sg.Text(' ', size=(8, 1), key=("-CLKTOTAL-"))],
               [sg.Text('Notas del juego', size=(15, 10), key=("-MESSAGE-"))],
               [sg.Text('Tiempo de jugada')],
               [sg.Text('', size= (8, 1), key= ('-CLKTURN-'))],
               [sg.Text('Puntaje = '),sg.Text('0',key='-SCORE-')],
               [sg.Text('letra actual')],
               [sg.Text('',size=(5,1),key=('-LetterSelected-'),justification=('center'))],
               [sg.Text(' ', size=(8, 1), key=("-TURN-"))]]

        col2 = [[sg.Button(' ', size=(4, 2), key=(i, j), pad=(0, 0),button_color=('white','blue')) for j in range(self._MAX_COL)] for i in range(self._MAX_ROWS)]

        col3 = [[sg.Button('', size=(4, 2), key= (str(n)), pad=(0, 0),button_color=('white','blue'))for n in range(7)] for m in range(1)]

        layout_tablero = [
            [sg.Text('COMPUTADORA'), sg.Text('', size=(30, 1),background_color='Brown', relief=sg.RELIEF_RIDGE)],
            [sg.Column(col2), sg.Column(col,background_color=('#C70F0F'))],
            [sg.Text(configs['name'], key=("-NOMBRE-")), sg.Column(col3), sg.Button('Comprobar'), sg.Button('Pasar'),sg.Button('Revertir'), sg.Button('cambiar', key=('-change-')), sg.Button('Change All', key=('-changeAll-'))]
        ]
        return layout_tablero

    def set_default_button(self,window,tupla):
        i,j=tupla
        if (i, j) in self.triple_letter:
            window.FindElement((i, j)).Update('TL')
        elif (i, j) in self.double_letter:
            window.FindElement((i, j)).Update('DL')
        elif (i, j) in self.triple_word:
            window.FindElement((i, j)).Update('TW')
        elif (i, j) in self.double_word:
            window.FindElement((i, j)).Update('DW')
        elif (i, j) == self.start_button:
            window.FindElement((i, j)).Update('ST')
        elif (i, j) in self.R10:
            window.FindElement((i, j)).Update('R10')
        elif (i, j) in self.R20:
            window.FindElement((i, j)).Update('R20')
        else:
            window.FindElement((i,j)).Update('')
            
    def table_on(self, window):
        for i in range(self._MAX_ROWS):
            for j in range(self._MAX_COL):
                self.set_default_button(window,(i,j))
        pass

    def update_fichas_player(self, window, fichas_player):
        for i in range(len(fichas_player)):
            window.FindElement(str(i)).Update(fichas_player[i])
        pass

    def calc_puntaje(self):
        pass

    def sabe_table(self):
        pass

    def calc_timeleft(self):
        '''
            Calcula el tiempo restante y lo devuelve en formato hh:mm:ss, o devuelve 0 si se terminó
        '''
        tiempo_restante = self.get_time_game() - int(round(time.time()))
        hora = tiempo_restante // 3600
        minutos = tiempo_restante // 60
        segundos = tiempo_restante % 60
        if minutos >= 60:
            minutos -= 60
        string = ('{:02d}:{:02d}:{:02d}'.format(hora, minutos, segundos))
        if tiempo_restante >= 0:
            return string
        else:
            return 0