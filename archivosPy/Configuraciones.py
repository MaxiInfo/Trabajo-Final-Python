import PySimpleGUI as sg
import Fichas
import Puntajes

def set_layout ():
    layout_configs = [
        [sg.Text('Configuraciones',size=(100,1),font=(None,15),text_color='black',justification='center')],
        [sg.Text('Nombre del jugador',size=(100,1),font=(None,11),justification='center')],
        [sg.Text(' '*8),sg.InputText('',size=(40,1),key='nom',justification='center')],
        [sg.Text(' '*12),sg.Text('Tiempo de juego',font=(None,11)),sg.Text(' '*2),sg.Text('Tiempo de turno',font=(None,11))],
        [sg.Text(' '*14),sg.InputCombo((30,60,90,120,),size=(4,1),default_value='120',readonly=True,pad=(0,0)),sg.Text('minutos'),sg.Text(' '*6),sg.InputCombo((20,30,40,60,),size=(3,1),default_value='60',readonly=True,pad=(0,0)),sg.Text('segundos')],
        [sg.Text('Dificultad',size=(100,1),font=(None,11),justification='center')],
        [sg.Text(' '*35),sg.Radio('Fácil','Dificultad',default=False,size=(10,1))],
        [sg.Text(' '*35),sg.Radio('Medio','Dificultad',default=True,size=(10,1))],
        [sg.Text(' '*35),sg.Radio('Difícil','Dificultad',default=False,size=(10,1))],
        [sg.Text(' '*5),sg.Text('Modificar fichas:',font=(None,11)),sg.Button(' ',image_filename='Cantidad.png',image_size=(105,28),size=(15,2),key='-cantfichas-'),sg.Button(' ',image_filename='Puntaje.png',image_size=(105,28),size=(15,2),key='-puntfichas-')],
        [sg.Text('')],
        [sg.Text(' '*4),sg.Button(' ',image_filename='Guardar.png',image_size=(120,28),size=(15,2),key='Guardar'),sg.Text(' '*10),sg.Button(' ',image_filename='Atras.png',image_size=(120,28),size=(15,2),key='Atrás')]
        ]
    return layout_configs

def main (configs):
    msj=('','Ingrese un nombre','Tiene que ingresar un nombre')
    window = sg.Window('ScrabbleAR', set_layout(),size=(400,360))
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
            configs['modsBolsa'][0] = Fichas.main()
            window.un_hide()
        if event == '-puntfichas-':
            window.hide()
            configs['modsBolsa'][1] = Puntajes.main()
            window.un_hide()
        if event in (None,'Atrás'):
            break
    window.close()
    return (event,configs)

    ''' en 4 filas
    [sg.Text('Tiempo de juego (minutos)',size=(100,1),justification='center')],
    [sg.Text(' '*23),sg.InputCombo(('30','60','90','120',),size=(5,1),default_value='120')],
    [sg.Text('Tiempo de turno (segundos)',size=(100,1),justification='center')],
    [sg.Text(' '*23),sg.InputCombo(('20','30','40','60',),size=(5,1),default_value='60')],

    tiempo y valor en dos filas
    [sg.Text(' ' * 5),sg.Text('Tiempo de juego:'),sg.InputCombo(('30','60','90','120',),size=(5,1),default_value='120'),sg.Text('minutos')],
    [sg.Text(' ' * 5),sg.Text('Tiempo de turno:'),sg.InputCombo(('20','30','40','60',),size=(5,1),default_value='60'),sg.Text('segundos')],
    '''