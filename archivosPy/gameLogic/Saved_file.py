import json
import PySimpleGUI as sg
'''
def main():
    try:
        archivo = open('saved_game.json', 'r')
        diccionario = json.load(archivo)
    except FileNotFoundError:
        sg.Popup('No hay archivo de juego guardado')
        return 0
    else:
        archivo.close()
        return diccionario
'''

def load_saved(configs, diccionario):
    '''
    Guarda los datos del diccionario del juego guardado en configs para usarlos al cargar el juego.
    '''
    configs['name'] = diccionario['name']
    configs['turn'] = diccionario['turn']
    configs['timing'] = diccionario['tiempo_restante']
    configs['dificultad'] = diccionario['dificultad']
    configs['atril_player'] = diccionario['atril_player']
    configs['atril_compu'] = diccionario['atril_compu']
    configs['punt_player'] = diccionario['punt_player']
    configs['punt_compu'] = diccionario['punt_compu']
    configs['modsBolsa'][0] = diccionario['bolsa_fichas']
    configs['modsBolsa'][1] = diccionario['puntaje_fichas']
    configs['tablero'] = diccionario['tablero']
    return configs


def main():
    archivo = open('saved_game.json', 'r')
    diccionario = json.load(archivo)
    archivo.close()
    return diccionario

    