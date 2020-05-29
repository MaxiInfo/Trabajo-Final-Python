import PySimpleGUI as sg
import time


class Tablero ():
    def __init__(self):
        self._MAX_ROWS = 15
        self._MAX_COL = 15
        self.board = [[0 for j in range(self._MAX_COL)]
                      for i in range(self._MAX_ROWS)]
        self.atril = [0 for n in range(7)]
        self.triple_letter = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9),(5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9))
        self.double_letter = ((0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 9), (14, 3), (14, 11))
        self.double_word = ((1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (10, 10), (11, 11), (12, 12), (13, 13))
        self.triple_word = ((0, 0), (0, 7), (0, 14), (7, 0),(7, 14), (14, 0), (14, 7), (14, 14))
        self.start_button = (7, 7)
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
               [sg.Text(' ', size=(8, 1), key=("-CLK"))],
               [sg.Text('Notas del juego', size=(15, 10), key=("-MESSAGE-"))],
               [sg.Text('Tiempo de jugada')],
               [sg.Text(' ', size=(8, 1), key=("-TURN-"))]]

        col2 = [[sg.Button(' ', size=(4, 2), key=(i, j), pad=(0, 0),button_color=('white','blue')) for j in range(self._MAX_COL)] for i in range(self._MAX_ROWS)]

        col3 = [[sg.Button('', size=(4, 2), key= (str(n)), pad=(0, 0))for n in range(7)] for m in range(1)]

        layout_tablero = [
            [sg.Text('COMPUTADORA'), sg.Text('', size=(30, 1),background_color='Brown', relief=sg.RELIEF_RIDGE)],
            [sg.Column(col2), sg.Column(col)],
            [sg.Text(configs['name'], key=("-NOMBRE-")), sg.Column(col3), sg.Button('Comprobar'), sg.Button('Pasar'), sg.Button('cambiar'),sg.Button('Revertir')]
        ]
        return layout_tablero

    def table_on(self, window):
        for i in range(self._MAX_ROWS):
            for j in range(self._MAX_COL):
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
                else:
                    window.FindElement((i, j)).Update('')
        pass

    def update_fichas_player(self, window, fichas_player):
        for i in range(len(fichas_player)):
            window.FindElement(str(i)).Update(fichas_player[i])
        pass

    def calc_puntaje(self):
        pass

    def sabe_table(self):
        pass
