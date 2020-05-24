import PySimpleGUI as sg
from Class_tablero import Tablero

def game_start (window):
    pass

def main(configs):
    window = sg.Window('ScrabbleAR', Tablero.set_layout(configs))
    event,values = window.read()
    while True:
        if event in (None, 'salir'):
            return(None)
        elif event in ('Empezar'):
            game_start(window)
        elif event in ('Posponer'):
            window.FindElement('-MESSAGE-').Update('Debes comenzar el juego para podes posponerlo')
    return event


#configs = {'name':values[0],'timing':values[1],'dificultad':'facil'if values[2] else 'medio' if values[3]else 'dificil'}