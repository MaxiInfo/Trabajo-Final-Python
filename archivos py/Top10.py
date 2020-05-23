import PySimpleGUI as sg

archivo_top = open('temp\top10.json','r+')

#diccionario = archivo_top.read()

#print(diccionario)

layout_top = [
    [sg.Text('TOP 10',size=(100,1),font=(None,15),justification='center')],
    [sg.Text('')],
    [sg.Text(' '*15),sg.Button('facil',size=(15,2))],
    [sg.Text(' '*15),sg.Button('normal',size=(15,2))],
    [sg.Text(' '*15),sg.Button('dificil',size=(15,2))],
    [sg.Text('')],
    [sg.Text(' '*15),sg.Button('atras',size=(15,2))],
    ]