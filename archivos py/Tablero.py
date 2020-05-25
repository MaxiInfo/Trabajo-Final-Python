import PySimpleGUI as sg
from Class_tablero import Tablero
from Class_Dificultad import dificultad
def game_start (window,configs):
    Tablero.table_on(window)
    #dificultad.establecer_dificultad(configs['dificultad'])
    #TERMINAAAR
    pass

def main(configs):
    window = sg.Window('ScrabbleAR', Tablero.set_layout(configs))
    event,values = window.read()
    while True:
        if event in (None, 'salir'):
            return(None)
        elif event is 'Empezar':
            game_start(window,configs)
        else:
            window.FindElement('-MESSAGE-').Update('Comienza el juego para poder utilizar la interfaz')
        print(event)
        event,values = window.read()
    return event

#configs = dict({'name':'Player','timing':20,'dificultad':'medio'})