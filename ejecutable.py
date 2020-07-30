import PySimpleGUI as sg
from sys import platform 
from archivosPy.configuracion import configuraciones as config
from archivosPy.gameLogic import board_logic as board
from archivosPy.gameLogic import saved_file as save
from archivosPy.top import top10 as top

sg.theme('LightBrown1')

color_fondo = ('#E6DECE','#E6DECE')

#sg.Button(' ',image_filename='Imagenes/menu/ScrabbleAr.png',image_size=(200,50),size=(15,2),button_color=color_fondo,key='Titulo')

layout_main_menu = [
    [sg.Text(' '*18),sg.Image('Imagenes/menu/ScrabbleAr.png',size=(250,60))],
    [sg.Text('')],
    [sg.Text(' '*28),sg.Button(' ',image_filename='Imagenes/menu/Jugar1.png',image_size=(122,40),size=(15,2),key='Jugar')],
    [sg.Text(' '*28),sg.Button(' ',image_filename='Imagenes/menu/Continuar1.png',image_size=(122,37),size=(15,2),key='Continuar')],
    [sg.Text(' '*28),sg.Button(' ',image_filename='Imagenes/menu/Configuracion1.png',image_size=(122,37),size=(15,2),key='Configuracion')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text(' '*3),sg.Button(' ',image_filename='Imagenes/menu/TOP10.png',image_size=(122,37),size=(12,2),key='TOP 10'),sg.Text(' '*12),
    sg.Button(' ',image_filename='Imagenes/menu/Salir.png',image_size=(122,37),size=(12,2),key='Salir')]
    ]

configs = {'name':'Player','timing':120, 'turn':60, 'dificultad':'facil','modsBolsa':[None, None]}
#'modsBolsa' guarda en la posición 0 la cantidad de fichas y en la posición 1 el puntaje

#[sg.Text(' '*18),sg.Button('',image_filename = 'Configuraciones5.png',image_size=(100,35),)], -->Ejemplo de uso de imagen como botón.
winSize = (400,350) if platform.startswith('win32') else (451,390)
window_menu = sg.Window('ScrabbleAR', layout_main_menu,size= winSize)
event, values= window_menu.read()
while True:
    if event in (None,'Salir'):
        break
    elif event == 'Jugar':
        window_menu.hide()
        event = board.main(configs)
    elif event == 'Continuar':
        try:
            guardado = save.main()
        except FileNotFoundError:
            sg.Popup('No hay un archivo de juego guardado')
        else:
            configs = save.load_saved(configs, guardado)
        event = board.main(configs)
    elif event in ('Configuracion'):
        window_menu.hide()
        event,configs = config.main(configs)
    elif event == 'TOP 10':
        window_menu.hide()
        event = top.main()
    if event == None:
        break
    window_menu.un_hide()
    event, values= window_menu.read()