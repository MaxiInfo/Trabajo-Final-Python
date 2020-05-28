import PySimpleGUI as sg
from Class_tablero import Tablero
from Class_administrador import AdministradorDeJuego
from Class_Jugador import jugador
from random import randint as rand

board = Tablero()
admin = AdministradorDeJuego()
teclas = ('0','1','2','3','4','5','6')

def game_on (window,configs,fichas_jugador):
    window.FindElement('-MESSAGE-').Update('Comenzo la partida')
    admin.set_dificultad(configs['dificultad'])
    board.table_on(window)
    board.update_fichas_player(window,fichas_jugador)
    pass


def play_player (player, window):
    window.FindElement('-MESSAGE-').Update('Ingrese una palabra')
    pos_event = None
    cant_letras = 0
    palabra = ''
    while True:
        event,values = window.Read()
        if event in (None, '-mainMenu-'):
            break
        if event == 'cambiar':
            player.set_fichas(admin.tomar_fichas(7))
            board.update_fichas_player(window,player.get_fichas())
            continue
        if event == 'Comprobar':
            if cant_letras >= 2:
                if admin.es_correcta(palabra):
                    window.FindElement('-MESSAGE-').Update('palabra correcta')
                    break
                else:
                    window.FindElement('-MESSAGE-').Update('palabra incorrecta')
            elif (palabra == ''):
                window.FindElement('-MESSAGE-').Update('una palabra por favor')
            else:
                window.FindElement('-MESSAGE-').Update('palabra minima 2 caracteres')
            continue
        if event in teclas:
            letter = player.get_fichas()[int(event)]
            window.FindElement(event).Update('')
            while True:
                event,values = window.Read()
                print('palabra = ',palabra)
                if event in (None, '-mainMenu-'):
                    break
                if type(event) == tuple:
                    if cant_letras == 0:
                        palabra += letter
                        pos_event = event
                        window.FindElement(event).Update(letter)
                        next1 = (event[0]+1,event[1])
                        next2 = (event[0],event[1]+1)
                        window.FindElement(next1).Update(button_color = ('black','#4E61DC'))
                        window.FindElement(next2).Update(button_color = ('black','#4E61DC'))
                        cant_letras += 1
                    elif cant_letras == 1:
                        palabra += letter
                        if (event == next1):
                            window.FindElement(next2).Update(button_color = ('black','blue'))
                            window.FindElement(event).Update(letter)
                            window.FindElement(event).Update(letter,button_color = ('white','blue'))
                            next_button = (event[0]+1,event[1])
                            window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                            escritura = 'ArribaAbajo'
                            
                        elif (event == next2):
                            if event[1] < 15:
                                window.FindElement(next1).Update(button_color = ('black','blue'))
                            window.FindElement(event).Update(letter,button_color = ('white','blue'))

                            next_button = (event[0],event[1]+1)
                            window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                            escritura = 'IzqDer'
                        else:
                            continue
                        cant_letras += 1
                    elif cant_letras == 2:
                        palabra += letter
                        if event == next_button:
                            if escritura == 'IzqDer':
                                next_button =  (next_button[0],next_button[1]+1)
                            else:
                                next_button =  (next_button[0]+1,next_button[1])
                            window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                            window.FindElement(event).Update(letter,button_color = ('white','blue'))
                        else:
                            continue
                    break
    return event


def game_procces (window,player,compu):
    rand_start = rand(1,2)
    if (rand_start == 1):
        while True:
            event = play_player (player,window)
            #compu.jugar (compu,window)
            if event in (None, '-mainMenu-'):
                break
    else:
        while True:
            #compu.jugar (compu,window)
            event = play_player (player,window)
            if event in (None, '-mainMenu-'):
                break
    return event

def main(configs):
    board = Tablero()
    window = sg.Window('ScrabbleAR', board.set_layout(configs))
    while True:
        event,values = window.read()
        if event == 'Empezar':
            player = jugador(configs['name'],admin.tomar_fichas(7))
            compu = jugador('CPU',admin.tomar_fichas(7))
            game_on(window,configs,player.get_fichas())
            event = game_procces(window,player,compu)
        if event in (None, '-mainMenu-'):
            break
        else:
            window.FindElement('-MESSAGE-').Update('Comienza el juego para poder utilizar la interfaz')
    window.close()
    return event

#configs = dict({'name':'Player','timing':20,'dificultad':'medio'})