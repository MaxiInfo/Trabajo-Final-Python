import PySimpleGUI as sg

from Class_tablero import Tablero

def main(configs):
    window = sg.Window('ScrabbleAR', Tablero.set_layout(configs))
    event,values = window.read()
    while True:
        if event in (None, 'salir'):
            return(None)
        elif event in ('Empezar'):
            Tablero.table_on()
    return event


#configs = {'name':values[0],'timing':values[1],'dificultad':'facil'if values[2] else 'medio' if values[3]else 'dificil'}