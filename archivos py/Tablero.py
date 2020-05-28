import PySimpleGUI as sg
from Class_tablero import Tablero
from Class_Dificultad import AdministradorDeJuego
from Class_Jugador import jugador
from random import randint as rand

board = Tablero()
admin = AdministradorDeJuego()
teclas = ('0','1','2','3','4','5','6')

def game_on (window,configs,fichas_jugador):
    window.FindElement('-MESSAGE-').Update('FELISITEISHO HAZ COMENSADEISHON EL JUEGEISHON')
    admin.set_dificultad(configs['dificultad'])
    board.table_on(window)
    board.update_fichas_player(window,fichas_jugador)
    pass

def play_player (player, window):
    while True:
        event,values = window.Read()
        if event == None:
            break
        if event in teclas:
            letter = player.get_fichas()[int(event)]
            window.FindElement(event).Update('')
            while True:
                event,values = window.Read()
                try:
                    event[1] 
                except IndexError:
                    continue
                else:
                    window.FindElement(event).Update(letter)
                    break
    pass

def game_procces (window,player,compu):
    #rand_start = rand(1,2)
    #if (rand_start == 1):
    play_player (player,window)
    pass

def main(configs):
    board = Tablero()
    window = sg.Window('ScrabbleAR', board.set_layout(configs))
    event,values = window.read()
    while True:
        if event in (None, 'Menu principal'):
            break
        elif event == 'Empezar':
            player = jugador(configs['name'],admin.tomar_fichas(7))
            compu = jugador('CPU',admin.tomar_fichas(7))
            game_on(window,configs,player.get_fichas())
            game_procces(window,player,compu)
        else:
            window.FindElement('-MESSAGE-').Update('Comienza el juego para poder utilizar la interfaz')
        print(event)
        event,values = window.read()
    window.close()
    return event

#configs = dict({'name':'Player','timing':20,'dificultad':'medio'})