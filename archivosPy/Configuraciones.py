import PySimpleGUI as sg
import Fichas
import Puntajes

def set_layout ():
    layout_configs = [
        [sg.Text('Configuraciones',size=(100,1),font=(None,15),justification='center')],
        [sg.Text('Nombre del jugador',size=(100,1),justification='center')],
        [sg.Text(' '*16),sg.InputText('',size=(15,1),key='nom')],
        [sg.Text('Tiempo de juego (minutos)',size=(100,1),justification='center')],
        [sg.Text(' '*23),sg.InputCombo(('30','60','90','120',),size=(5,1),default_value='120')],
        [sg.Text('Tiempo de turno (segundos)',size=(100,1),justification='center')],
        [sg.Text(' '*23),sg.InputCombo(('20','30','40','60',),size=(5,1),default_value='60')],
        [sg.Text('Dificultad',size=(100,1),justification='center')],
        [sg.Text(' '*23),sg.Radio('Fácil','Dificultad',default=False,size=(10,1))],
        [sg.Text(' '*23),sg.Radio('Medio','Dificultad',default=True,size=(10,1))],
        [sg.Text(' '*23),sg.Radio('Difícil','Dificultad',default=False,size=(10,1))],
        [sg.Text(' '*5),sg.Text('Modificar fichas:'),sg.Button('Cantidad',key='-cantfichas-'),sg.Button('Puntaje',key='-puntfichas-')],
        [sg.Button('Guardar'),sg.Text(' '*30),sg.Button('Atrás')]
        ]
    return layout_configs

def main (configs):
    msj=('','Ingrese un nombre','Tiene que ingresar un nombre')
    window = sg.Window('ScrabbleAR', set_layout(),size=(300,380))
    while True:
        event, values = window.read()
        if event == 'Guardar':
            if values['nom'] not in (msj):
                window.close()
                configs['name']=values['nom']
                configs['timing']=values[0]
                configs['turn']=values[1]
                configs['dificultad']='facil'if values[2] else 'medio' if values[3]else 'dificil'
                return (event,configs)
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