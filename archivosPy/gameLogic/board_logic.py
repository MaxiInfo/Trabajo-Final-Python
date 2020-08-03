import PySimpleGUI as sg
import json
import time
from random import randint as rand

from archivosPy.clases.class_tablero import Tablero
from archivosPy.clases.class_administrador import AdministradorDeJuego
from archivosPy.clases.class_Jugador import jugador
from archivosPy.IA.class_IA import Computer
from archivosPy.IA.gen_list_positions import main as serch_positions
from archivosPy.gameLogic.end_game import End

TECLAS = ('0','1','2','3','4','5','6')

PATH_LETRAS = 'Imagenes/tablero/letras/'
PATH_ESPECIALES = 'Imagenes/tablero/especiales/'
EXTENSION = '.png'

def guardar (board, jugador, admin, compu, name):
    '''
    Guarda diccionario en formato JSON. Información: "name" (nombre jugador, str), "turn" (tiempo de turno, int),
    "dificultad" (str), "atril_player" (list), "atril_compu" (list), "punt_player" (int), "punt_compu" (int),
    "tiempo_restante" (int, segundos para hacer cálculo), "bolsa_fichas" (dict, letra y cant),
    "puntaje_fichas" (dict, letra y puntaje), "tablero" (solo guarda las letras bloqueadas en una lista de tuplas,
    pos 0 es letra, 1 fila y 2 columna).
    '''
    letras_tablero = []
    tab_completo = board.get_board()
    for i in range(15): #desp cambiar por get del maximo de filas, lo mismo abajo
        for j in range(15):
            if tab_completo[i][j] != 0:
                tup = (tab_completo[i][j], i, j)
                letras_tablero.append(tup)
    diccionario = {
        'name': name,
        'turn': board.get_turn(),
        'dificultad': admin.get_dificultad(),
        'atril_player': jugador.get_fichas(),
        'atril_compu': compu.get_letters(),
        'punt_player': jugador.get_puntaje(),
        'punt_compu': compu.get_score(),
        'tiempo_restante': board.get_time_game() - int(round(time.time())),
        'bolsa_fichas': admin.get_cantidad(),
        'puntaje_fichas': admin.get_puntaje(),
        'tablero': letras_tablero
    }
    
    with open("archivosJSON/saved_game.json", "w") as saved_file:
        json.dump(diccionario, saved_file, ensure_ascii=False)
    
    '''
    dict_guardar = json.dumps(diccionario, ensure_ascii= False)
    print(dict_guardar)
    '''

def saved_board(lista_guardadas):
    '''
    Esta función crea una palabra con todas las letras guardadas y una lista de tuplas con las posiciones de cada letra.
    '''
    palabra = ''
    tuplas = []
    for i in lista_guardadas:
        palabra += i[0]
        pos = (i[1], i[2])
        tuplas.append(pos)
    return palabra, tuplas

def game_on (window,board,fichas_jugador):
    window.FindElement('-MESSAGE-').Update('Comenzo la partida')
    board.table_on(window)
    pass

def block_word(window,tuple_list,palabra,board):
    board.mod_board(tuple_list,palabra)
    j = 0
    for i in tuple_list:
        #window.FindElement(i).Update(disabled=True,button_color = ('black','#58F76D'))
        window.FindElement(i).Update(disabled=True,image_filename = PATH_LETRAS + palabra[j].upper() + EXTENSION,button_color = ('black','#58F76D')) ##
        j += 1
    pass

def vuelta_atras(window,player,board,letter,tupla,cant,escritura):
    board.set_default_button(window,tupla)
    pos = player.pos_libre()
    player.set_single_ficha(letter,pos)
    window.FindElement(str(pos)).Update(image_filename = PATH_LETRAS + letter.upper() + EXTENSION,disabled = False) ##
    if cant == 1:
        tupla_aux1 = (tupla[0],tupla[1]+1) 
        tupla_aux2 = (tupla[0]+1,tupla[1]) 
        try:
            if board.get_board()[tupla_aux1[0]][tupla_aux1[1]] == 0:
                window.FindElement(tupla_aux1).Update(button_color = ('white','blue'))
        except:
            None
        try:
            if board.get_board()[tupla_aux2[0]][tupla_aux2[1]] == 0:
                window.FindElement(tupla_aux2).Update(button_color = ('white','blue'))
        except:
            None
    elif cant == 2:
        if escritura == 'Horizontal':
            tupla_aux2 = (tupla[0]+1,tupla[1]-1) 
            tupla_aux3 = (tupla[0],tupla[1]+1) 
        else:
            tupla_aux2 = (tupla[0]-1,tupla[1]+1) 
            tupla_aux3 = (tupla[0]+1,tupla[1])

        window.FindElement(tupla).Update(button_color = ('black','#4E61DC'))
        try:
            if board.get_board()[tupla_aux2[0]][tupla_aux2[1]] == 0:
                window.FindElement(tupla_aux2).Update(button_color = ('black','#4E61DC'))
        except:
            None
        try:
            if board.get_board()[tupla_aux3[0]][tupla_aux3[1]] == 0:
                window.FindElement(tupla_aux3).Update(button_color = ('white','blue'))
        except:
            None
    elif cant > 2:
        if escritura == 'Horizontal':
            tupla_aux = (tupla[0],tupla[1]+1) 
        else:
            tupla_aux = (tupla[0]+1,tupla[1])
        try:
            if board.get_board()[tupla_aux[0]][tupla_aux[1]] == 0:
                window.FindElement(tupla_aux).Update(button_color = ('white','blue'))
        except:
            None
        window.FindElement(tupla).Update(button_color = ('black','#4E61DC'))

    pass

def cambiar_fichas(window,player,admin):
    cant = 0
    tecla_select = []
    window.FindElement('-MESSAGE-').Update('seleccione hasta 3 letras para cambiar')
    window.FindElement('-change-').Update(image_filename='Imagenes/board/Ok.png',image_size=(85,25))
    while True:
        event,_ = window.Read()
        if event in TECLAS:
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
            letters_ant = [player.get_single_ficha(int(i)) for i in tecla_select]
            fichas_nue = admin.tomar_fichas(cant)
            for i in range(cant):
                window.FindElement(tecla_select[i]).Update(image_filename = PATH_LETRAS + fichas_nue[i].upper() + EXTENSION,button_color = ('white','blue')) #Para el atril
                player.set_single_ficha(fichas_nue[i],int(tecla_select[i]))    
                window.FindElement('-change-').Update(image_filename='Imagenes/board/Cambiar.png',image_size=(85,25))
            admin.devolver_a_bolsa(letters_ant)
            break
        if event in (None, '-mainMenu-'):
            break
    return event

def ingresa_primera(window,event,letter,board):
    window.FindElement(event).Update(image_filename = PATH_LETRAS + letter.upper() + EXTENSION) ##
    #(fila,columna)
    next1 = (event[0]+1,event[1])#abajo
    next2 = (event[0],event[1]+1)#derecha
    try:
        if (board.get_board()[next1[0]][next1[1]] == 0):
            window.FindElement(next1).Update(button_color= ('black','#4E61DC'))
    except:
        None
    try:
        if (board.get_board()[next2[0]][next2[1]] == 0):
            window.FindElement(next2).Update(button_color = ('black','#4E61DC'))
    except:
        None    
    return next1,next2

def ingresa_segunda():
    #no me sale una forma facil de simplificar aca
    #para hacer
    pass

def ingresa_tercera(window,event,escritura,letter,next_button, board):
    window.FindElement(event).Update(image_filename = PATH_LETRAS + letter.upper() + EXTENSION, button_color = ('white','blue')) ##
    if escritura == 'Horizontal':
        next_button =  (next_button[0],next_button[1]+1)
    else:
        next_button =  (next_button[0]+1,next_button[1])
    try:
        if (board.get_board()[next_button[0]][next_button[1]] == 0):
            window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
    except:
        None
    return next_button

def fill_letters(player,window,admin):
    list_fichas = player.get_fichas()
    for i in range(len(list_fichas)):
        if list_fichas[i] == 0:
            ficha = admin.tomar_fichas(1)[0]
            list_fichas[i] = ficha
            window.FindElement(str(i)).Update(image_filename = PATH_LETRAS + ficha.upper() + EXTENSION,disabled=False) 
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
        tiempo_restante = board.calc_timeleft()
        window['-CLKTOTAL-'].update(tiempo_restante)
        #tiempo_restante = board.get_time_game() - int(round(time.time()))
        #window['-CLKTOTAL-'].update('{:02d}:{:02d}:{:02d}'.format(((tiempo_restante) // 60) // 60, (((tiempo_restante) // 60) - 60), (tiempo_restante) % 60))
        if turno_restante > 0:
            turno_restante = tiempo_turno - int(round(time.time()))
            window['-CLKTURN-'].update('{:02d}:{:02d}'.format((turno_restante) // 60, (turno_restante) % 60))
        else:
            window['-MESSAGE-'].update('Te quedaste sin tiempo papá')
            #acá iria un break, pero no puedo lograr que imprima el mensaje
        if tiempo_restante == 0:
            break
        #dar un cierre al juego, calcular puntaje, declarar ganador, etc.
#==========================================================================================================================#
        if event in (None, '-mainMenu-', '-SAVE-'):
            break
#==========================================================================================================================#
        if event == '-pasar-':
            if player.get_cambios() == 3:
                return '-GameOver-'
            else:
                player.add_cambio()
                if cant_letras != 0:
                    for i in range(cant_letras):
                        vuelta_atras(window,player,board,palabra[len(palabra)-1],tuple_list[len(tuple_list)-1],cant_letras,escritura)
                        tuple_list.pop()
                        palabra = palabra[0:-1]
                        cant_letras -= 1
                    window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
                break
#==========================================================================================================================#
        if event == '-changeAll-':
            '''if player.get_cambios() == 3:
                return '-GameOver-'
            player.add_cambio()
            if player.get_cambios() == 3:
                window.FindElement('-change-').Update(disabled=True)
                window.FindElement('-changeAll-').Update(disabled=True)
            if cant_letras != 0:
                    for i in range(cant_letras):
                        vuelta_atras(window,player,board,palabra[len(palabra)-1],tuple_list[len(tuple_list)-1],cant_letras,escritura)
                        tuple_list.pop()
                        palabra = palabra[0:-1]
                        cant_letras -= 1
                    window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
            letters_ant = player.get_fichas()
            player.set_fichas(admin.tomar_fichas(len(letters_ant)))
            admin.devolver_a_bolsa(letters_ant)
            board.update_fichas_player(window,player.get_fichas())'''
            break
#==========================================================================================================================#  
        if event == '-change-' and cant_letras == 0:
            if player.get_cambios() == 3:
                return '-GameOver-'
            player.add_cambio()
            if player.get_cambios() == 3:
                window.FindElement('-change-').Update(disabled=True)
                window.FindElement('-changeAll-').Update(disabled=True)
            if cant_letras != 0:
                    for i in range(cant_letras):
                        vuelta_atras(window,player,board,palabra[len(palabra)-1],tuple_list[len(tuple_list)-1],cant_letras,escritura)
                        tuple_list.pop()
                        palabra = palabra[0:-1]
                        cant_letras -= 1
                    window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
            event = cambiar_fichas(window,player,admin)
            break
#==========================================================================================================================#       
        if event in TECLAS:
            window.FindElement('-MESSAGE-').Update('Ingrese la letrra en el tablero')
            if not letter_selected:
                # si no hay fichas seleccionadas tomo una ficha del atril, actualizo fichas del jugador
                # update de ficha actual seleccionada
                pos_en_atril = event
                letter = get_ficha(int(event))
                window.FindElement(event).Update('')
                window.FindElement('-LetterSelected-').Update(filename = PATH_LETRAS + letter.upper() + EXTENSION)
                letter_selected = True
            else:
                # devoludion de ficha seleccionada
                if event == pos_en_atril:
                    # si se quiere devolver a la misma posicion donde se tomo
                    pos_en_atril = None
                    window.FindElement(event).Update(letter)
                    set_ficha(letter,int(event))
                    window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
                    letter_selected = False
                else:
                    # si se quiere intercambiar de ficha actual con otra en el atril
                    pos_en_atril = event
                    window.FindElement(event).Update(image_filename = PATH_LETRAS + letter.upper() + EXTENSION)
                    let_change = player.change_single_ficha(letter,int(event))
                    if let_change != 0:
                        letter = let_change
                        window.FindElement('-LetterSelected-').Update(filename = PATH_LETRAS + letter.upper() + EXTENSION)
                    else:
                        window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
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
                next1,next2 = ingresa_primera(window,event,letter,board)
                window.FindElement(pos_en_atril).Update(disabled=True)
                window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
            elif cant_letras == 1:
                #si ya esta ingresada la primera letra
                if (event == next1):
                    #si se ingreso de arriba a abajo
                    palabra += letter
                    letter_selected = False
                    cant_letras += 1
                    letra_ant = letter
                    tuple_list.append(event)
                    try:
                        if (board.get_board()[next2[0]][next2[1]] == 0):
                            window.FindElement(next2).Update(button_color = ('white','blue'))
                    except:
                        None
                    window.FindElement(event).Update(image_filename = PATH_LETRAS + letter.upper() + EXTENSION,button_color = ('white','blue'))
                    next_button = (event[0]+1,event[1])
                    try:
                        if (board.get_board()[next_button[0]][next_button[1]] == 0):
                            window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                    except:
                        None
                    window.FindElement(pos_en_atril).Update(disabled=True) 
                    window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
                elif (event == next2):
                    #si se ingreso de Izquierda a Derecha
                    palabra += letter
                    letter_selected = False
                    cant_letras += 1
                    letra_ant = letter 
                    tuple_list.append(event)
                    try:
                        if (board.get_board()[next1[0]][next1[1]] == 0):
                            window.FindElement(next1).Update(button_color = ('white','blue'))
                    except:
                        None
                    window.FindElement(event).Update(image_filename = PATH_LETRAS + letter.upper() + EXTENSION,button_color = ('white','blue'))
                    next_button = (event[0],event[1]+1)
                    try:
                        if (board.get_board()[next_button[0]][next_button[1]] == 0):
                            window.FindElement(next_button).Update(button_color = ('black','#4E61DC'))
                    except:
                        None
                    escritura = 'Horizontal'
                    window.FindElement(pos_en_atril).Update(disabled=True)
                    window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
                else: 
                    continue
            elif cant_letras >= 2:
                #Si ya se ingresaron 2 o mas letras
                if event == next_button:
                    letra_ant = letter
                    palabra += letter
                    letter_selected = False
                    tuple_list.append(event)
                    next_button = ingresa_tercera(window,event,escritura,letter,next_button, board)
                    cant_letras += 1
                    window.FindElement(pos_en_atril).Update(disabled=True)
                    window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
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
                    try:
                        window.FindElement(next_button).Update(button_color = ('white','blue'))
                    except:
                        None
                    block_word(window,tuple_list,palabra,board)
                    fill_letters(player,window,admin)
                    board_aux = board.get_board()
                    lis_pos = serch_positions(board_aux,len(board_aux),len(board_aux[0]))
                    if len(lis_pos) == 0:
                        return '-GameOver-'
                    break
                else:
                    window.FindElement('-MESSAGE-').Update(str(palabra)+', no es una palabra')
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
                window.FindElement('-LetterSelected-').Update(filename = PATH_ESPECIALES + 'VACIO' + EXTENSION)
            continue
    return event

def game_procces (window,admin,board,player,IA):
    if len(player.get_fichas()) == 0: #no hay juego guardado
        player.set_fichas(admin.tomar_fichas(7))
        IA.set_letters(admin.tomar_fichas(7))
        rand_start = rand(1,2)
    else:
        rand_start = 1 #hay juego guardado y empieza el jugador
    board.update_fichas_player(window,player.get_fichas())
    if (rand_start == 1):
        while True:
            event = play_player(player,window,admin,board)
            IA.play (window,admin,board)
            if event in (None, '-mainMenu-', '-SAVE-'):
                break
            if event =='-GameOver-':
                End(player,IA,admin)
                break
            if IA.get_changes() == 3:
                End(player,IA,admin)
                return '-ChangesDone-'
            
    else:
        while True:
            IA.play (window,admin,board)
            if IA.get_changes() == 3:
                return '-ChangesDone-'
            event = play_player (player,window,admin,board)
            if event in (None, '-mainMenu-', '-SAVE-'):
                break
            if event == '-GameOver-':
                End(player,IA,admin)
                break
    return event

def main(configs):
    admin = AdministradorDeJuego(configs['dificultad'],configs['modsBolsa'])
    board = Tablero(admin.devolver_tuplas())           
    window = sg.Window('ScrabbleAR', board.set_layout(configs),background_color=('#1CB7C3'))
    while True:
        event,_ = window.read()
        if event == 'Empezar':
            player = jugador(configs['name']) #subi estas variables para que cree las instancias y modificarlas con configs
            IA = Computer()
            if 'tablero' in configs: #si lo tiene, viene de un juego guardado
                player.set_fichas(configs['atril_player'])
                IA.set_letters(configs['atril_compu'])
                player.mod_puntaje(configs['punt_player'])
                window['-SCORE-'].Update(player.get_puntaje())
                IA.set_score(configs['punt_compu'])
                t = configs['timing']
            else:
                t = configs['timing'] * 60 #si viene de un juego nuevo, pasar de minutos a segundos
            tiempo_juego = int(round(time.time()) + (t))
            tiempo_restante = tiempo_juego - int(round(time.time()))
            board.set_time_game(tiempo_juego)
            board.set_time_left(tiempo_restante)
            board.set_turn(configs['turn'])
            #player = jugador()
            #IA = Computer()
            game_on(window,board,player.get_fichas()) #preguntar para que pasa el get_fichas, si es posible sacarlo
            if 'tablero' in configs: #prueba, queda horrible hacer el if de nuevo
                palabra, tuplas = saved_board(configs['tablero'])
                block_word(window, tuplas, palabra, board)
            event = game_procces(window,admin,board,player,IA)
        if event == '-SAVE-':
            guardar(board, player, admin, IA, configs["name"])
            break
        if event in (None, '-mainMenu-','-GameOver-'):

            break
        else:
            window.FindElement('-MESSAGE-').Update('Comienza el juego para poder utilizar la interfaz')
    window.close()
    return event