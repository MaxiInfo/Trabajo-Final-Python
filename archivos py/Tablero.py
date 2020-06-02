import PySimpleGUI as sg
from Class_tablero import Tablero
from Class_administrador import AdministradorDeJuego
from Class_Jugador import jugador
from random import randint as rand
import time

admin = AdministradorDeJuego()
lista_tuplas = admin.devolver_tuplas()
board = Tablero(lista_tuplas)
teclas = ('0','1','2','3','4','5','6')

#tiempo_juego = 0
#tiempo_restante = 0

def game_on (window,configs,fichas_jugador):
    window.FindElement('-MESSAGE-').Update('Comenzo la partida')
    admin.set_dificultad(configs['dificultad'])
    board.table_on(window)
    board.update_fichas_player(window,fichas_jugador)
    pass

def block_word(window,tuple_list,palabra):
    board.mod_board(tuple_list,palabra)
    for i in tuple_list:
        window.FindElement(i).Update(disabled=True,button_color = ('black','#58F76D'))
    pass

def ingresa_primera(window,event,letter):
    window.FindElement(event).Update(letter)
    next1 = (event[0]+1,event[1])
    next2 = (event[0],event[1]+1)
    if(next1[0] < 15):
        window.FindElement(next1).Update(button_color = ('black','#4E61DC'))
    if(next2[1]<15):
        window.FindElement(next2).Update(button_color = ('black','#4E61DC'))
    return next1,next2

def ingresa_segunda():
    #no me sale una forma facil de simplificar aca
    pass

def ingresa_tercera(window,event,escritura,letter,next_button):
    if escritura == 'IzqDer':
        next_button =  (next_button[0],next_button[1]+1)
    else:
        next_button =  (next_button[0]+1,next_button[1])
    if 15 not in next_button:
        window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
    window.FindElement(event).Update(letter,button_color = ('white','blue'))
    return next_button

def fill_letters(player,window):
    list_fichas = player.get_fichas()
    for i in range(len(list_fichas)):
        if list_fichas[i] == 0:
            ficha = admin.tomar_fichas(1)
            list_fichas[i] = ficha
            window.FindElement(str(i)).Update(ficha)
    player.set_fichas(list_fichas)
    pass

def play_player (player, window):
    '''
    el modulo play_player es el encargado del manejo de la colocacion de palabras en el tablero y el manejr de la interfaz 
    que el usuario va a tener dentro del juego
    '''

    get_ficha = lambda x: player.get_single_ficha(x)
    set_ficha = lambda letter,pos: player.set_single_ficha(letter,pos)
    window.FindElement('-MESSAGE-').Update('Ingrese una palabra')
    cant_letras = 0
    letter_selected = False

    cant_test = 0

    tiempo_turno = int(round(time.time() * 100)) + 500
    turno_restante = tiempo_turno - int(round(time.time() * 100))  

    while True:
        event,_ = window.Read(timeout= 10)
#==========================================================================================================================#
        #tiempo_restante = tiempo_juego - int(round(time.time() * 100))
        tiempo_restante = board.get_time_game() - int(round(time.time() * 100))
        window['-CLKTOTAL-'].update('{:02d}:{:02d}:{:02d}'.format(((tiempo_restante // 100) // 60) // 60, ((tiempo_restante // 100) // 60) - 60, (tiempo_restante // 100) % 60))
        if turno_restante > 0:
            turno_restante = tiempo_turno - int(round(time.time() * 100))
            window['-CLKTURN-'].update('{:02d}:{:02d}'.format((turno_restante // 100) // 60, (turno_restante // 100) % 60))
        else:
            window['-MESSAGE-'].update('Te quedaste sin tiempo papá')
            #acá iria un break, pero no puedo lograr que imprima el mensaje
        if tiempo_restante == 0:
            break
#==========================================================================================================================#
        if event in (None, '-mainMenu-'):
            break
#==========================================================================================================================#
        if event == 'cambiar':
            player.set_fichas(admin.tomar_fichas(7))
            board.update_fichas_player(window,player.get_fichas())
            continue # ACA VA BREAK
#==========================================================================================================================#        
        if event in teclas:
            if not letter_selected:
                # si no hay fichas seleccionadas tomo una ficha del atril, actualizo fichas del jugador
                # update de ficha actual seleccionada
                letter = get_ficha(int(event))
                window.FindElement(event).Update('')
                window.FindElement('-LetterSelected-').Update(letter)
                letter_selected = True
            else:
                # devoludion de ficha seleccionada
                if player.ficha_pos(int(event)) == 0:
                    # si se quiere devolver a la misma posicion donde se tomo
                    window.FindElement(event).Update(letter)
                    set_ficha(letter,int(event))
                    window.FindElement('-LetterSelected-').Update('')
                    letter_selected = False
                else:
                    # si se quiere intercambiar de ficha actual con otra en el atril
                    cant_test += 1
                    window.FindElement(event).Update(letter)
                    letter = player.change_single_ficha(letter,int(event))
                    window.FindElement('-LetterSelected-').Update(letter)
            continue
#==========================================================================================================================#            
        if type(event) == tuple and letter_selected:
            if cant_letras == 0 and event != (14,14):
                palabra = letter
                letter_selected = False
                cant_letras += 1
                tuple_list = [event]
                next1,next2 = ingresa_primera(window,event,letter)
            elif cant_letras == 1:
                palabra += letter
                letter_selected = False
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
                letter_selected = False
                tuple_list.append(event)
                if event == next_button:
                    next_button = ingresa_tercera(window,event,escritura,letter,next_button)
                else:
                    continue
            elif event == (14,14):
                window.FindElement('-MESSAGE-').Update('no se puede ingresar la primera letra en el ultimo casillero')
                continue
#==========================================================================================================================#                  
        if event == 'Comprobar':
            if (palabra == ''):
                window.FindElement('-MESSAGE-').Update('Debe ingresar una palabra')
            elif cant_letras >= 2:
                if admin.es_correcta(palabra):
                    window.FindElement('-MESSAGE-').Update('palabra correcta')
                    window.FindElement(next_button).Update(button_color = ('white','blue'))
                    block_word(window,tuple_list,palabra)
                    fill_letters(player,window)
                    break
                else:
                    window.FindElement('-MESSAGE-').Update(str(palabra)+' no es una palabra')
            else:
                window.FindElement('-MESSAGE-').Update('palabra minima 2 caracteres')
            continue
        #if event == 'Revertir':

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
    #board = Tablero()
    window = sg.Window('ScrabbleAR', board.set_layout(configs),background_color=('#1CB7C3'))
    while True:
        event,_ = window.read()
        if event == 'Empezar':
            #global tiempo_restante
            #global tiempo_juego
            tiempo_juego = int(round(time.time() * 100)) + 720000
            tiempo_restante = tiempo_juego - int(round(time.time() * 100))
            board.set_time_game(tiempo_juego)
            board.set_time_left(tiempo_restante)
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