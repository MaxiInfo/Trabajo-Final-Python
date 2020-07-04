import PySimpleGUI as sg
from Class_tablero import Tablero
from Class_administrador import AdministradorDeJuego
from Class_Jugador import jugador
from ClassIA import Computer
from random import randint as rand
import time

teclas = ('0','1','2','3','4','5','6')


def game_on (window,board,fichas_jugador):
    window.FindElement('-MESSAGE-').Update('Comenzo la partida')
    board.table_on(window)
    pass

def block_word(window,tuple_list,palabra,board):
    board.mod_board(tuple_list,palabra)
    for i in tuple_list:
        window.FindElement(i).Update(disabled=True,button_color = ('black','#58F76D'))
    pass

def vuelta_atras(window,player,board,letter,tupla,cant,escritura):
    board.set_default_button(window,tupla)
    pos = player.pos_libre()
    player.set_single_ficha(letter,pos)
    window.FindElement(str(pos)).Update(letter,disabled = False)
    if cant == 1:
        tupla_aux1 = (tupla[0],tupla[1]+1) 
        tupla_aux2 = (tupla[0]+1,tupla[1]) 
        window.FindElement(tupla_aux1).Update(button_color = ('white','blue'))
        window.FindElement(tupla_aux2).Update(button_color = ('white','blue'))
    elif cant == 2:
        if escritura == 'IzqDer':
            tupla_aux1 = (tupla[0],tupla[1]) 
            tupla_aux2 = (tupla[0]+1,tupla[1]-1) 
            tupla_aux = (tupla[0],tupla[1]+1) 
        else:
            tupla_aux1 = (tupla[0],tupla[1]) 
            tupla_aux2 = (tupla[0]-1,tupla[1]+1) 
            tupla_aux = (tupla[0]+1,tupla[1]) 
        window.FindElement(tupla_aux).Update(button_color = ('white','blue'))
        window.FindElement(tupla_aux1).Update(button_color = ('black','#4E61DC'))
        window.FindElement(tupla_aux2).Update(button_color = ('black','#4E61DC'))
    elif cant > 2:
        if escritura == 'IzqDer':
            tupla_aux = (tupla[0],tupla[1]+1) 
        else:
            tupla_aux = (tupla[0]+1,tupla[1])
        window.FindElement(tupla_aux).Update(button_color = ('white','blue'))
        window.FindElement(tupla).Update(button_color = ('black','#4E61DC'))
    pass

def cambiar_fichas(window,player,admin):
    cant = 0
    tecla_select = []
    window.FindElement('-MESSAGE-').Update('seleccione hasta 3 letras para cambiar')
    window.FindElement('-change-').Update('OK')
    while True:
        event,_ = window.Read()
        if event in teclas:
            if event in tecla_select:
                cant -= 1
                tecla_select.remove(event)
                window.FindElement(event).Update(button_color = ('white','blue'))
            else:
                if (cant < 3):
                    cant += 1
                    tecla_select.append(event)
                    window.FindElement(event).Update(button_color = ('black','#73FFD6'))
                else:
                    window.FindElement('-MESSAGE-').Update('Ya Seleccionaste 3 Letras')
        if event == '-change-' and cant > 0:
            fichas_nue = admin.tomar_fichas(cant)
            for i in range(cant):
                window.FindElement(tecla_select[i]).Update(fichas_nue[i],button_color = ('white','blue'))
                player.set_single_ficha(fichas_nue[i],int(tecla_select[i]))    
                window.FindElement('-change-').Update('Cambiar')
            break
        if event in (None, '-mainMenu-'):
            break
    return event

def ingresa_primera(window,event,letter):
    window.FindElement(event).Update(letter)
    next1 = (event[0]+1,event[1])
    next2 = (event[0],event[1]+1)
    if(next1[0] < 15):
        window.FindElement(next1).Update(button_color= ('black','#4E61DC'))
    if(next2[1]<15):
        window.FindElement(next2).Update(button_color = ('black','#4E61DC'))
    return next1,next2

def ingresa_segunda():
    #no me sale una forma facil de simplificar aca
    #para hacer
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

def fill_letters(player,window,admin):
    list_fichas = player.get_fichas()
    for i in range(len(list_fichas)):
        if list_fichas[i] == 0:
            ficha = admin.tomar_fichas(1)
            list_fichas[i] = ficha
            window.FindElement(str(i)).Update(ficha,disabled=False)
    player.set_fichas(list_fichas)
    pass

def play_player (player, window,admin,board):
    '''
    el modulo play_player es el encargado del manejo de la colocacion de palabras en el tablero y el manejr de la interfaz 
    que el usuario va a tener dentro del juego
    '''

    get_ficha = lambda x: player.get_single_ficha(x)
    set_ficha = lambda letter,pos: player.set_single_ficha(letter,pos)
    window.FindElement('-MESSAGE-').Update('Ingrese una palabra')
    cant_letras = 0
    letter_selected = False
    escritura = None
    letra_ant = ''

    tiempo_turno = int(round(time.time())) + (board.get_turn())
    turno_restante = tiempo_turno - int(round(time.time()))

    while True:
        event,_ = window.Read(timeout= 10)
#==========================================================================================================================#
        tiempo_restante = board.get_time_game() - int(round(time.time()))
        window['-CLKTOTAL-'].update('{:02d}:{:02d}:{:02d}'.format(((tiempo_restante) // 60) // 60, ((tiempo_restante) // 60) - 60, (tiempo_restante) % 60))
        if turno_restante > 0:
            turno_restante = tiempo_turno - int(round(time.time()))
            window['-CLKTURN-'].update('{:02d}:{:02d}'.format((turno_restante) // 60, (turno_restante) % 60))
        else:
            window['-MESSAGE-'].update('Te quedaste sin tiempo papá')
            #acá iria un break, pero no puedo lograr que imprima el mensaje
        if tiempo_restante == 0:
            break
#==========================================================================================================================#
        if event in (None, '-mainMenu-'):
            break
#==========================================================================================================================#
        if event == '-changeAll-': #and cant_letras != 0
            player.set_fichas(admin.tomar_fichas(7))
            board.update_fichas_player(window,player.get_fichas())
            continue
#==========================================================================================================================#  
        if event == '-change-' and cant_letras == 0:
            event = cambiar_fichas(window,player,admin)
            break
#==========================================================================================================================#       
        if event in teclas:
            window.FindElement('-MESSAGE-').Update('Ingrese la letrra en el tablero')
            if not letter_selected:
                # si no hay fichas seleccionadas tomo una ficha del atril, actualizo fichas del jugador
                # update de ficha actual seleccionada
                pos_en_atril = event
                letter = get_ficha(int(event))
                window.FindElement(event).Update('')
                window.FindElement('-LetterSelected-').Update(letter)
                letter_selected = True
            else:
                # devoludion de ficha seleccionada
                if event == pos_en_atril:
                    # si se quiere devolver a la misma posicion donde se tomo
                    pos_en_atril = None
                    window.FindElement(event).Update(letter)
                    set_ficha(letter,int(event))
                    window.FindElement('-LetterSelected-').Update('')
                    letter_selected = False
                else:
                    # si se quiere intercambiar de ficha actual con otra en el atril
                    pos_en_atril = event
                    window.FindElement(event).Update(letter)
                    let_change = player.change_single_ficha(letter,int(event))
                    if let_change != 0:
                        letter = let_change
                        window.FindElement('-LetterSelected-').Update(letter)
                    else:
                        window.FindElement('-LetterSelected-').Update('')
                        letter_selected = False
            window.FindElement('-MESSAGE-').Update('Seleccione otra letra')
            continue
#==========================================================================================================================#            
        if type(event) == tuple and letter_selected:
            #si no hay letras ingresadas en la jugada actual
            if cant_letras == 0 and event != (14,14):
                palabra = letter
                letra_ant = letter
                letter_selected = False
                cant_letras += 1
                tuple_list = [event]
                next1,next2 = ingresa_primera(window,event,letter)
                window.FindElement(pos_en_atril).Update(disabled=True)
                window.FindElement('-LetterSelected-').Update('')
            elif cant_letras == 1:
                #si ya esta ingresada la primera letra
                if (event == next1):
                    #si se ingreso de arriba a abajo
                    palabra += letter
                    letter_selected = False
                    cant_letras += 1
                    letra_ant = letter
                    tuple_list.append(event)
                    if event[1] < 14:
                        window.FindElement(next2).Update(button_color = ('white','blue'))
                    window.FindElement(event).Update(letter,button_color = ('white','blue'))
                    next_button = (event[0]+1,event[1])
                    if 15 not in next_button:
                        window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                    escritura = 'ArribaAbajo'
                    window.FindElement(pos_en_atril).Update(disabled=True)
                    window.FindElement('-LetterSelected-').Update('')
                elif (event == next2):
                    #si se ingreso de Izquierda a Derecha
                    palabra += letter
                    letter_selected = False
                    cant_letras += 1
                    letra_ant = letter
                    tuple_list.append(event)
                    if event[0] < 14:
                        window.FindElement(next1).Update(button_color = ('white','blue'))
                    window.FindElement(event).Update(letter,button_color = ('white','blue'))
                    next_button = (event[0],event[1]+1)
                    if 15 not in next_button:
                        window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                    escritura = 'IzqDer'
                    window.FindElement(pos_en_atril).Update(disabled=True)
                    window.FindElement('-LetterSelected-').Update('')
                else: 
                    continue
            elif cant_letras >= 2:
                #Si ya se ingresaron 2 o mas letras
                if event == next_button:
                    letra_ant = letter
                    palabra += letter
                    letter_selected = False
                    tuple_list.append(event)
                    next_button = ingresa_tercera(window,event,escritura,letter,next_button)
                    cant_letras += 1
                    window.FindElement(pos_en_atril).Update(disabled=True)
                    window.FindElement('-LetterSelected-').Update('')
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
                    player.mod_puntaje(admin.calcular_puntaje(palabra,tuple_list))
                    window.FindElement('-SCORE-').Update(player.get_puntaje())
                    window.FindElement('-MESSAGE-').Update('palabra correcta')
                    window.FindElement(next_button).Update(button_color = ('white','blue'))
                    block_word(window,tuple_list,palabra,board)
                    fill_letters(player,window,admin)
                    break
                else:
                    window.FindElement('-MESSAGE-').Update(str(palabra)+' no es una palabra')
            else:
                window.FindElement('-MESSAGE-').Update('palabra minima 2 caracteres')
            continue
#==========================================================================================================================#                  
        if event == 'Revertir' and not letter_selected:
            if cant_letras == 0:
                window.FindElement('-MESSAGE-').Update('No Hay Letras Ingresadas En Este Turno')
            else:
                vuelta_atras(window,player,board,palabra[len(palabra)-1],tuple_list[len(tuple_list)-1],cant_letras,escritura)
                tuple_list.pop()
                palabra = palabra[0:-1]
                cant_letras -= 1
                window.FindElement('-LetterSelected-').Update('')
            continue
    return event


def game_procces (window,admin,board,player,IA):
    player.set_fichas(admin.tomar_fichas(7))
    board.update_fichas_player(window,player.get_fichas())
    IA.set_letters(admin.tomar_fichas(7))
    rand_start = rand(1,2)
    if (rand_start == 1):
        while True:
            event = play_player(player,window,admin,board)
            #IA.play (IA,window)
            if event in (None, '-mainMenu-'):
                break
    else:
        while True:
            #IA.play (IA,window)
            event = play_player (player,window,admin,board)
            if event in (None, '-mainMenu-'):
                break
    return event

def main(configs):
    admin = AdministradorDeJuego(configs['dificultad'],configs['modsBolsa'])
    lista_tuplas = admin.devolver_tuplas()
    board = Tablero(lista_tuplas)           
    window = sg.Window('ScrabbleAR', board.set_layout(configs),background_color=('#1CB7C3'))
    while True:
        event,_ = window.read()
        if event == 'Empezar':
            tiempo_juego = int(round(time.time()) + (configs['timing'] * 60))
            tiempo_restante = tiempo_juego - int(round(time.time()))
            board.set_time_game(tiempo_juego)
            board.set_time_left(tiempo_restante)
            board.set_turn(configs['turn'])
            player = jugador()
            IA = Computer()
            game_on(window,board,player.get_fichas())
            event = game_procces(window,admin,board,player,IA)
        if event in (None, '-mainMenu-'):
            break
        else:
            window.FindElement('-MESSAGE-').Update('Comienza el juego para poder utilizar la interfaz')
    window.close()
    return event