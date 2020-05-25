import PySimpleGUI as sg

def set_layout ():
    layout_configs = [
        [sg.Text('configuraciones',size=(100,1),font=(None,15),justification='center')],
        [sg.Text('nombre del jugador',size=(100,1),justification='center')],
        [sg.Text(' '*16),sg.InputText('',size=(30,1),key='nom')],
        [sg.Text('tiempo de juego',size=(100,1),justification='center')],
        [sg.Text(' '*23),sg.InputCombo(('1','5','10','20',),size=(5,1),default_value='10')],
        [sg.Text('dificultad',size=(100,1),justification='center')],
        [sg.Text(' '*24),sg.Radio('facil','Dificultad',default=False,size=(10,1))],
        [sg.Text(' '*23),sg.Radio('medio','Dificultad',default=True,size=(10,1))],
        [sg.Text(' '*23),sg.Radio('dificil','Dificultad',default=False,size=(10,1))],
        [sg.Button('guardar'),sg.Text(' '*30),sg.Button('atras')]
        ]
    return layout_configs

def main ():
    conf = []
    msj=('','Ingrese un nombre','Tiene que ingresar un nombre')
    window = sg.Window('ScrabbleAR', set_layout(),size=(300,300))
    while True:
        event, values = window.read()
        if event == 'guardar':
            if values['nom'] not in (msj):
                conf = {'name':values['nom'],'timing':values[0],'dificultad':'facil'if values[1] else 'medio' if values[2]else 'dificil'}
                window.close()
                return (event,conf)
            else:
                if (values['nom'] == msj[0]):
                    window.FindElement('nom').update(msj[1])
                elif (values['nom'] == msj[1]):
                    window.FindElement('nom').update(msj[2])
        else:
            window.close()
            return (event,conf)