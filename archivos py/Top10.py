import PySimpleGUI as sg
import TopString
import json

nombre_archivo = "archivoTop.json"
archivo_top = open(nombre_archivo,'r')

diccionario = json.load(archivo_top)

#print(diccionario)

layout_top = [
    [sg.Text('TOP 10',size=(100,1),font=(None,15),justification='center')],
    [sg.Text('')],
    [sg.Text('  FACIL'),sg.Text(' ' * 35),sg.Text('MEDIO'),sg.Text(' ' * 35),sg.Text('DIFICIL')],
    [sg.Multiline(default_text= TopString.generar_string(diccionario['facil']),size=(22,12)),
    sg.Multiline(default_text= TopString.generar_string(diccionario['medio']),size=(22,12)),
    sg.Multiline(default_text= TopString.generar_string(diccionario['dificil']),size=(22,12))
     ]
]

window = sg.Window('TOP',layout_top,size = (600,300))

x = window.read()