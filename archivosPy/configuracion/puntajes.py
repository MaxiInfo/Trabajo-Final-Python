import PySimpleGUI as sg
def set_layout():
    '''
        Paso a explicar, tupla contiene los valores que voy a poder seleccionar en mi inputcombo.
            InputCombo -> tupla -> valor por defecto siempre es 5. La llave permite que mi diccionario values tenga dicha clave.
            Readonly, sirve para que la casilla del inputcombo NO SEA ESCRITA, por lo tanto, sólo permite que elijas entre 5-15.
            El método devuelve la Layout ya armada
    '''
    tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    col1 = [
        [sg.Text('A',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[12],size=(3,1),key='A',readonly=True)],
        [sg.Text('B',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[4],size=(3,1),key='B',readonly=True)],
        [sg.Text('C',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[4],size=(3,1),key='C',readonly=True)],
        [sg.Text('D',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[5],size=(3,1),key='D',readonly=True)],
        [sg.Text('E',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[12],size=(3,1),key='E',readonly=True)],
        [sg.Text('F',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[3],size=(3,1),key='F',readonly=True)]
    ]
    col2 = [
        [sg.Text('G',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[3],size=(3,1),key='G',readonly=True)],
        [sg.Text('H',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[2],size=(3,1),key='H',readonly=True)],
        [sg.Text('I',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[6],size=(3,1),key='I',readonly=True)],
        [sg.Text('J',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[3],size=(3,1),key='J',readonly=True)],
        [sg.Text('K',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[3],size=(3,1),key='K',readonly=True)],
        [sg.Text('L',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[4],size=(3,1),key='L',readonly=True)]
    ]
    col3 = [
        [sg.Text('LL',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[2],size=(3,1),key='LL',readonly=True)],
        [sg.Text('M',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[3],size=(3,1),key='M',readonly=True)],
        [sg.Text('N',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[5],size=(3,1),key='N',readonly=True)],
        [sg.Text('Ñ',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[2],size=(3,1),key='Ñ',readonly=True)],
        [sg.Text('O',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[9],size=(3,1),key='O',readonly=True)],
        [sg.Text('P',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[3],size=(3,1),key='P',readonly=True)]
    ]
    col4 = [
        [sg.Text('Q',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[2],size=(3,1),key='Q',readonly=True)],
        [sg.Text('R',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[5],size=(3,1),key='R',readonly=True)],
        [sg.Text('RR',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[1],size=(3,1),key='RR',readonly=True)],
        [sg.Text('S',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[6],size=(3,1),key='S',readonly=True)],
        [sg.Text('T',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[4],size=(3,1),key='T',readonly=True)],
        [sg.Text('U',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[5],size=(3,1),key='U',readonly=True)]
    ]
    col5 = [
        [sg.Text('V',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[2],size=(3,1),key='V',readonly=True)],
        [sg.Text('W',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[1],size=(3,1),key='W',readonly=True)],
        [sg.Text('X',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[2],size=(3,1),key='X',readonly=True)],
        [sg.Text('Y',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[3],size=(3,1),key='Y',readonly=True)],
        [sg.Text('Z',size=(2,1),justification='center'),sg.InputCombo(tupla,default_value=tupla[2],size=(3,1),key='Z',readonly=True)]
    ]

    layout = [
        [sg.Text('Configuración puntaje de las fichas',size=(38,1),font=(None,15),justification='center',text_color='white',background_color='purple')],
        [sg.Text('')],
        [sg.Column(col1,background_color='black'),sg.Column(col2,background_color='red'),sg.Column(col3,background_color='green'),sg.Column(col4,background_color='blue'),sg.Column(col5,background_color='white')],
        [sg.Button('Guardar',size=(25,1)),sg.Button('Atrás',size=(25,1))]
    ]
    
    return layout

def main():
    '''
        Sí cambio es True, es por que el usuario tocó en guardar, por lo tanto quiere usar la bolsa que modificó -> la devuelvo
        Sí cambio es False, es por que el usuario tocó Atrás, por lo tanto NO quiere usar la bolsa que modificó -> no la devuelvo
    '''
    window = sg.Window('Puntaje de las fichas',set_layout())
    while True:
        event,values = window.read()
        window.close()
        if event in (None,'Atrás'):
            return None
        if event in ('Guardar'):
            return values

#bolsa = configuracion_bolsa()
#print(bolsa)