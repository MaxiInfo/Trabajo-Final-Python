import PySimpleGUI as sg

window = sg.Window('Columns')                                   # blank window

# Column layout
col = [[sg.Text('DIFICULTAD', font= 'Arial 15')],
       [sg.Radio('Facil', "RADIO1", default=True, size=(10,1))],
       [sg.Radio('Medio', "RADIO2")],
       [sg.Radio('Difícil', "RADIO3")],
       [sg.Text(' ' * 30)],
       [sg.Exit('Atrás')]]

layout = [[sg.Text(' ' * 5), sg.Column(col)]]

# Display the window and get values

window = sg.Window('Compact 1-line window with column', layout)
event, values = window.read()
window.close()

sg.Popup(event, values, line_width=200)
