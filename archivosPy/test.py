import PySimpleGUI as sg
'''palabra = 'lldwajhdksndrrakdjhwjkallal'
cant = 0
letras = []
while cant < len(palabra):
    if cant < len(palabra)-1 and palabra[cant]+palabra[cant+1] in ('rr','ll'):
        letras += [palabra[cant]+palabra[cant+1]]
        cant+=2
    else:
        letras += palabra[cant]
        cant += 1

print(letras)
'''
layout = [
    [sg.Text('',key = 'Text')],
    [sg.Button('Salir'),sg.Button('Sigue')]
]

window = sg.Window('Prueba',layout)

while True:
    event,values = window.read()

    if event in ('Salir',None):
        break
    if event in 'Sigue':
        pass
    window['Text'].Update([sg.Image(filename='Imagenes/tablero/letras/A.png')])
