import PySimpleGUI as sg
from Class_tablero import Tablero
from Class_Dificultad import dificultad
from Class_Jugador import jugador
from random import randint as rand

board = Tablero()
dif = dificultad()

def game_on (window,configs,fichas_jugador):
    dif.set_dificultad(configs['dificultad'])
    board.table_on(window)
    board.update_fichas_player(window,fichas_jugador)
    pass

def play (player):
    pass

def game_procces (window,player,compu):
    rand_start = rand(1,2)
    if (rand_start == 1):
        play (player)
    else:
        play (compu)
    pass

def main(configs):
    board = Tablero()
    window = sg.Window('ScrabbleAR', board.set_layout(configs))
    event,values = window.read()
    while True:
        if event in (None, 'Menu principal'):
            break
        elif event == 'Empezar':
            juga1 = jugador(configs['name'],dif.tomar_fichas(7))
            compu = jugador('CPU',dif.tomar_fichas(7))
            game_on(window,configs,juga1.get_fichas())
            game_procces(window,juga1,compu)
        else:
            window.FindElement('-MESSAGE-').Update('Comienza el juego para poder utilizar la interfaz')
        event,values = window.read()
    window.close()
    return event

#configs = dict({'name':'Player','timing':20,'dificultad':'medio'})