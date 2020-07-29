import PySimpleGUI as sg
import json
from sys import platform 

from archivosPy.top import TopString

nombre_archivo = "archivosJSON/archivoTop.json"
archivo_top = open(nombre_archivo,'r')

diccionario = json.load(archivo_top)

#print(diccionario)

def set_layout():
    lista_facil = TopString.generar_string(diccionario['facil'])
    lista_medio = TopString.generar_string(diccionario['medio'])
    lista_dificil = TopString.generar_string(diccionario['dificil'])
    # lista[0] -> nombre.   lista[1] -> puntaje.    lista[2] -> fecha

    col_nombre_facil = [
        [sg.Text('NOMBRES',font= (None,11),text_color='black',background_color='green')],
        [sg.Multiline(default_text= lista_facil[0],disabled=True,size=(13,13))]
    ]
    col_puntaje_facil = [
        [sg.Text('PUNTAJES',font= (None,11),text_color='black',background_color='green')],
        [sg.Multiline(default_text= lista_facil[1],disabled=True,size=(13,13))]
    ]
    col_fecha_facil = [
        [sg.Text('FECHAS',font= (None,11),text_color='black',background_color='green')],
        [sg.Multiline(default_text= lista_facil[1],disabled=True,size=(13,13))]
    ]
    columna_facil = [
        [sg.Text('FACIL',size=(35,1),font=(None,15),justification='center',text_color='black',background_color='green')],
        [sg.Column(col_nombre_facil),sg.Column(col_puntaje_facil),sg.Column(col_fecha_facil)]
    ]

    col_nombre_medio = [
        [sg.Text('NOMBRES',font= (None,11),text_color='black',background_color='yellow')],
        [sg.Multiline(default_text= lista_medio[0],disabled=True,size=(13,13))]
    ]
    col_puntaje_medio = [
        [sg.Text('PUNTAJES',font= (None,11),text_color='black',background_color='yellow')],
        [sg.Multiline(default_text= lista_medio[1],disabled=True,size=(13,13))]
    ]
    col_fecha_medio = [
        [sg.Text('FECHAS',font= (None,11),text_color='black',background_color='yellow')],
        [sg.Multiline(default_text= lista_medio[1],disabled=True,size=(13,13))]
    ]
    columna_medio = [
        [sg.Text('MEDIO',size=(35,1),font=(None,15),justification='center',text_color='black',background_color='yellow')],
        [sg.Column(col_nombre_medio),sg.Column(col_puntaje_medio),sg.Column(col_fecha_medio)]
    ]

    col_nombre_dificil = [
        [sg.Text('NOMBRES',font= (None,11),text_color='black',background_color='red')],
        [sg.Multiline(default_text= lista_dificil[0],disabled=True,size=(13,13))]
    ]
    col_puntaje_dificil = [
        [sg.Text('PUNTAJES',font= (None,11),text_color='black',background_color='red')],
        [sg.Multiline(default_text= lista_dificil[1],disabled=True,size=(13,13))]
    ]
    col_fecha_dificil = [
        [sg.Text('FECHAS',font= (None,11),text_color='black',background_color='red')],
        [sg.Multiline(default_text= lista_dificil[1],disabled=True,size=(13,13))]
    ]
    columna_dificil = [
        [sg.Text('DIFICIL',size=(35,1),font=(None,15),justification='center',text_color='black',background_color='red')],
        [sg.Column(col_nombre_dificil),sg.Column(col_puntaje_dificil),sg.Column(col_fecha_dificil)]
    ]

    layout_top = [
        [sg.Text('TOP10',size=(75,1),font=(None,20),justification='center',text_color='black',background_color='#E6DECE')],
        [sg.Column(columna_facil,background_color='green'),sg.Column(columna_medio,background_color='yellow'),sg.Column(columna_dificil,background_color='red')],
        [sg.Button('Atrás',size=(15,2))]
    ]
    return layout_top

def main ():
    winSize = (1230,400) if platform.startswith('win32') else (1400,400)
    window = sg.Window('ScrabbleAR', set_layout(),size=winSize)
    event,values= window.read()
    window.close()
    return event
