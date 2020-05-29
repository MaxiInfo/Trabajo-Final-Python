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

def block_word(window,tuple_list):
    for i in tuple_list:
        window.FindElement(i).Update(disabled=True,button_color = ('black','#58F76D'))
    pass

def ingresa_primera():
    pass

def ingresa_segunda():
    pass

def ingresa_tercera():
    pass

def play_player (player, window):
    window.FindElement('-MESSAGE-').Update('Ingrese una palabra')
    cant_letras = 0
    while True:
        event,_ = window.Read()

        if event in (None, '-mainMenu-'):
            break
        if event == 'cambiar':
            player.set_fichas(admin.tomar_fichas(7))
            board.update_fichas_player(window,player.get_fichas())
            continue
        
        if event in teclas:
            letter = player.get_fichas()[int(event)]
            window.FindElement(event).Update('')
            while True:
                event,_ = window.Read()
                if event in (None, '-mainMenu-'):
                    break
                if type(event) == tuple:
                    if cant_letras == 0 and event != (14,14):
                        palabra = letter
                        cant_letras += 1
                        tuple_list = [event]
                        window.FindElement(event).Update(letter)
                        next1 = (event[0]+1,event[1])
                        next2 = (event[0],event[1]+1)
                        if(next1[0] < 15):
                            window.FindElement(next1).Update(button_color = ('black','#4E61DC'))
                        if(next2[1]<15):
                            window.FindElement(next2).Update(button_color = ('black','#4E61DC'))
                    elif cant_letras == 1:
                        palabra += letter
                        cant_letras += 1
                        tuple_list.append(event)
                        if (event == next1):
                            if event[1] < 14:
                                window.FindElement(next2).Update(button_color = ('white','blue'))
                            window.FindElement(event).Update(letter,button_color = ('white','blue'))
                            next_button = (event[0]+1,event[1])
                            if 15 not in next_button:
                                window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                            escritura = 'ArribaAbajo'
                            
                        elif (event == next2):
                            if event[0] < 14:
                                window.FindElement(next1).Update(button_color = ('white','blue'))
                            window.FindElement(event).Update(letter,button_color = ('white','blue'))
                            next_button = (event[0],event[1]+1)
                            if 15 not in next_button:
                                window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                            escritura = 'IzqDer'
                        else:
                            continue
                    elif cant_letras == 2:
                        palabra += letter
                        tuple_list.append(event)
                        if event == next_button:
                            if escritura == 'IzqDer':
                                next_button =  (next_button[0],next_button[1]+1)
                            else:
                                next_button =  (next_button[0]+1,next_button[1])
                            if 15 not in next_button:
                                window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                            window.FindElement(event).Update(letter,button_color = ('white','blue'))
                        else:
                            continue
                    elif event == (14,14):
                        window.FindElement('-MESSAGE-').Update('no se puede ingresar la primera letra en el ultimo casillero')
                        continue
                    break
        if event == 'Comprobar':
            if cant_letras >= 2:
                if admin.es_correcta(palabra):
                    window.FindElement('-MESSAGE-').Update('palabra correcta')
                    window.FindElement(next_button).Update(button_color = ('white','blue'))
                    block_word(window,tuple_list)
                    break
                else:
                    window.FindElement('-MESSAGE-').Update(str(palabra)+' no es una palabra')
            elif (palabra == ''):
                window.FindElement('-MESSAGE-').Update('Debe ingresar una palabra')
            else:
                window.FindElement('-MESSAGE-').Update('palabra minima 2 caracteres')
            continue
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
        event,_ = window.read()
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