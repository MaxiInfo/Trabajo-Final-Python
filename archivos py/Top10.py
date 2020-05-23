import PySimpleGUI as sg
import TopString
import json

nombre_archivo = "top10.json"
archivo_top = open(nombre_archivo,'r')

diccionario = json.load(archivo_top)

print(diccionario)

layout_top = [
    [sg.Text('TOP 10',size=(100,1),font=(None,15),justification='center')],
    [sg.Text('')],
    [sg.Text(' '*15),sg.Button('facil',size=(15,2))],
    [sg.Text(' '*15),sg.Button('normal',size=(15,2))],
    [sg.Text(' '*15),sg.Button('dificil',size=(15,2))],
    [sg.Text('')],
    [sg.Text(' '*15),sg.Button('atras',size=(15,2))],
    ]