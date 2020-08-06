import PySimpleGUI as sg
import json
from sys import platform 
from archivosPy.top import top_string

NOMBRE_ARCHIVO = "archivosJSON/archivoTop.json"


def set_layout(diccionario):
    lista_facil = top_string.generar_string(diccionario['facil'])
    lista_medio = top_string.generar_string(diccionario['medio'])
    lista_dificil = top_string.generar_string(diccionario['dificil'])
    # lista[0] -> nombre.   lista[1] -> puntaje.    lista[2] -> fecha

    col_nombre_facil = [
        [sg.Text('NOMBRE',font= (None,11),text_color='black',background_color='green')],
        [sg.Multiline(default_text= lista_facil[0],disabled=True,size=(13,13))]
    ]
    col_puntaje_facil = [
        [sg.Text('PUNTAJE',font= (None,11),text_color='black',background_color='green')],
        [sg.Multiline(default_text= lista_facil[1],disabled=True,size=(13,13))]
    ]
    col_fecha_facil = [
        [sg.Text('FECHA',font= (None,11),text_color='black',background_color='green')],
        [sg.Multiline(default_text= lista_facil[2],disabled=True,size=(13,13))]
    ]
    columna_facil = [
        [sg.Text('FACIL',size=(35,1),font=(None,15),justification='center',text_color='black',background_color='green')],
        [sg.Column(col_nombre_facil),sg.Column(col_puntaje_facil),sg.Column(col_fecha_facil)]
    ]

    col_nombre_medio = [
        [sg.Text('NOMBRE',font= (None,11),text_color='black',background_color='yellow')],
        [sg.Multiline(default_text= lista_medio[0],disabled=True,size=(13,13))]
    ]
    col_puntaje_medio = [
        [sg.Text('PUNTAJE',font= (None,11),text_color='black',background_color='yellow')],
        [sg.Multiline(default_text= lista_medio[1],disabled=True,size=(13,13))]
    ]
    col_fecha_medio = [
        [sg.Text('FECHA',font= (None,11),text_color='black',background_color='yellow')],
        [sg.Multiline(default_text= lista_medio[2],disabled=True,size=(13,13))]
    ]
    columna_medio = [
        [sg.Text('MEDIO',size=(35,1),font=(None,15),justification='center',text_color='black',background_color='yellow')],
        [sg.Column(col_nombre_medio),sg.Column(col_puntaje_medio),sg.Column(col_fecha_medio)]
    ]

    col_nombre_dificil = [
        [sg.Text('NOMBRE',font= (None,11),text_color='black',background_color='red')],
        [sg.Multiline(default_text= lista_dificil[0],disabled=True,size=(13,13))]
    ]
    col_puntaje_dificil = [
        [sg.Text('PUNTAJE',font= (None,11),text_color='black',background_color='red')],
        [sg.Multiline(default_text= lista_dificil[1],disabled=True,size=(13,13))]
    ]
    col_fecha_dificil = [
        [sg.Text('FECHA',font= (None,11),text_color='black',background_color='red')],
        [sg.Multiline(default_text= lista_dificil[2],disabled=True,size=(13,13))]
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
    try:
        archivo_top = open(NOMBRE_ARCHIVO,'r')
    except FileNotFoundError:
        #Si se dá el caso que el usuario borra el archivoTop.json por que es un cliente desastroso, no estaría mal generarlo de nuevo.
        diccionario = {"facil": {"AAA": [50, "22/5"], "BBB": [45, "22/5"], "CCC": [40, "22/5"], "DDD": [35, "22/5"], "EEE": [30, "22/5"], "FFF": [25, "22/5"], "GGG": [20, "22/5"], "HHH": [15, "22/5"], "III": [10, "22/5"], "JJJ": [5, "22/5"]}, "medio": {"KKK": [70, "23/5"], "LLL": [65, "23/5"], "MMM": [60, "23/5"], "NNN": [55, "23/5"], "OOO": [50, "23/5"], "PPP": [45, "23/5"], "QQQ": [40, "23/5"], "RRR": [35, "23/5"], "SSS": [30, "23/5"], "TTT": [25, "23/5"]}, "dificil": {"j1": [45, "24/5"], "j2": [40, "24/5"], "j3": [35, "24/5"], "j4": [30, "24/5"], "j5": [25, "24/5"], "j6": [20, "24/5"], "j7": [15, "24/5"], "j8": [10, "24/5"], "j9": [5, "24/5"], "j10": [0, "24/5"]}}
        archivo_top = open(NOMBRE_ARCHIVO,'w')
        json.dump(diccionario,archivo_top)
        archivo_top.close()
    diccionario = json.load(archivo_top)
    winSize = (1230,400) if platform.startswith('win32') else (1400,400)
    window = sg.Window('ScrabbleAR', set_layout(diccionario),size=winSize)
    event,values= window.read()
    window.close()
    return event
