import PySimpleGUI as sg
from sys import platform 
from archivosPy.configuracion import fichas
from archivosPy.configuracion import puntajes
PATH_LETRAS = 'Imagenes/configuracion/'
EXTENSION = '.png'

def set_layout ():
    layout_configs = [
        [sg.Text('Configuraciones',size=(100,1),font=(None,15),text_color='black',justification='center')],
        [sg.Text('Nombre del jugador',size=(100,1),font=(None,11),justification='center')],
        [sg.Text(' '*30),sg.InputText('',size=(25,1),key='nom',justification='center')],
        [sg.Text(' '*12),sg.Text('Tiempo de juego',font=(None,11)),sg.Text(' '*2),sg.Text('Tiempo de turno',font=(None,11))],
        [sg.Text(' '*14),sg.InputCombo((2,5,15,30,60,90,120,),size=(4,1),default_value='120',readonly=True,pad=(0,0)),sg.Text('minutos'),
        sg.Text(' '*6),sg.InputCombo((20,30,40,60,),size=(3,1),default_value='60',readonly=True,pad=(0,0)),sg.Text('segundos')],
        [sg.Text('Dificultad',size=(100,1),font=(None,11),justification='center')],
        [sg.Text(' '*35),sg.Radio('Fácil','Dificultad',default=False,size=(10,1))],
        [sg.Text(' '*35),sg.Radio('Medio','Dificultad',default=True,size=(10,1))],
        [sg.Text(' '*35),sg.Radio('Difícil','Dificultad',default=False,size=(10,1))],
        [sg.Text(' '*5),sg.Text('Modificar fichas:',font=(None,11)),sg.Button(' ',image_filename=PATH_LETRAS+'Cantidad'+EXTENSION,image_size=(105,28),size=(15,2),key='-cantfichas-'),
        sg.Button(' ',image_filename=PATH_LETRAS+'Puntaje'+EXTENSION,image_size=(105,28),size=(15,2),key='-puntfichas-')],
        [sg.Text('')],
        [sg.Text(' '*4),sg.Button(' ',image_filename=PATH_LETRAS+'Guardar'+EXTENSION,image_size=(120,28),size=(15,2),key='Guardar'),sg.Text(' '*10),
        sg.Button(' ',image_filename=PATH_LETRAS+'Atras'+EXTENSION,image_size=(120,28),size=(15,2),key='Atrás')]
        ]
    return layout_configs

def main (configs):
    msj=('','Ingrese un nombre','Tiene que ingresar un nombre')
    winSize = (400,360) if platform.startswith('win32') else (500,390)
    window = sg.Window('ScrabbleAR', set_layout(),size=winSize)
    while True:
        event, values = window.read()
        if event == 'Guardar':
            if values['nom'] not in (msj):
                if len(values['nom']) < 11:
                    window.close()
                    configs['name']=values['nom']
                    configs['timing']=values[0]
                    configs['turn']=values[1]
                    configs['dificultad']='facil'if values[2] else 'medio' if values[3]else 'dificil'
                    return (event,configs)
                else:
                    window.FindElement('nom').Update('El nombre no debe superar los 10 caracteres')
            else:
                if (values['nom'] == msj[0]):
                    window.FindElement('nom').update(msj[1])
                elif (values['nom'] == msj[1]):
                    window.FindElement('nom').update(msj[2])
        if event == '-cantfichas-':
            window.hide()
            configs['modsBolsa'][0] = fichas.main()
            window.un_hide()
        if event == '-puntfichas-':
            window.hide()
            configs['modsBolsa'][1] = puntajes.main()
            window.un_hide()
        if event in (None,'Atrás'):
            break
    window.close()
    return (event,configs)