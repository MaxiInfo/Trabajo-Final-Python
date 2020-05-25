import PySimpleGUI as sg
from Class_tablero import Tablero
#from Class_Dificultad import dificultad as dif
def game_start (window):
    dif.establecer_dificultad(configs['dificultad'])
    pass

def main(configs):
    window = sg.Window('ScrabbleAR', Tablero.set_layout(configs))
    event,values = window.read()
    while True:
        if event in (None, 'salir'):
            return(None)
        elif event is 'Empezar':
            game_start(window)
        elif event is 'Posponer':
            window.FindElement('-MESSAGE-').Update('Debes comenzar el juego para podes posponerlo')
        else:
            window.FindElement('-MESSAGE-').Update('Comienza el juego para poder utilizar la interfaz')
    return event

#configs = dict({'name':'Player','timing':20,'dificultad':'medio'})

#configs = {'name':values[0],'timing':values[1],'dificultad':'facil'if values[2] else 'medio' if values[3]else 'dificil'}