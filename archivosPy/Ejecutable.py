import PySimpleGUI as sg
import Configuraciones as config
import Tablero as board
import Top10 as top

sg.theme('LightBrown1')

color_fondo = ('#E6DECE','#E6DECE')

layout_main_menu = [
    [sg.Text(' '*18),sg.Button(' ',image_filename='ScrabbleAr.png',image_size=(200,50),size=(15,2),button_color=color_fondo,key='Titulo')],
    [sg.Text('')],
    [sg.Text(' '*28),sg.Button(' ',image_filename='Jugar1.png',image_size=(122,40),size=(15,2),key='Jugar')],
    [sg.Text(' '*28),sg.Button(' ',image_filename='Continuar1.png',image_size=(122,37),size=(15,2),key='Continuar')],
    [sg.Text(' '*28),sg.Button(' ',image_filename='Configuracion1.png',image_size=(122,37),size=(15,2),key='Configuracion')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text(' '*3),sg.Button(' ',image_filename='TOP10.png',image_size=(122,37),size=(12,2),key='TOP 10'),sg.Text(' '*12),sg.Button(' ',image_filename='Salir.png',image_size=(122,37),size=(12,2),key='Salir')]
    ]

configs = dict({'name':'Player','timing':120, 'turn':60, 'dificultad':'facil','modsBolsa':[None, None]})
#'modsBolsa' guarda en la posición 0 la cantidad de fichas y en la posición 1 el puntaje

#[sg.Text(' '*18),sg.Button('',image_filename = 'Configuraciones5.png',image_size=(100,35),)], -->Ejemplo de uso de imagen como botón.

window_menu = sg.Window('ScrabbleAR', layout_main_menu,size=(400,350))
event, values= window_menu.read()
while True:
    if event in (None,'Salir'):
        break
    elif event == 'Jugar':
        window_menu.hide()
        event = board.main(configs)
    elif event == 'Continuar':
        window_menu.close()
        #FAALTAAAAAAAAAAAAAAAAAAAAAAAAaaaa
        #event = board.main(configs)
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