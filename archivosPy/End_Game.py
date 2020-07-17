import PySimpleGUI as sg
import Actualizar_top as top

def End(player,IA,admin):
    player.mod_puntaje(admin.calcular_sobrante(player.get_fichas()))
    puntaje = player.get_puntaje()
    winner = ''    
    if puntaje > IA.get_score():
        winner = 'Player'
    elif puntaje < IA.get_score():
        winner = 'IA'
    if winner == 'Player':
        if puntaje > top.get_ult_top10(admin.get_dificultad()):
            sg.popup('Felicidades haz ganado la partida \n conseguiste un puntaje los suficientemente alto para entrar en el TOP10!',no_titlebar=True)
            top.actualizar(player.get_name,puntaje,admin.get_dificultad)
        else:
            sg.popup('Felicidades haz ganado la partida /n tu puntaje no alcanzo para entrar en el TOP!)',no_titlebar=True)
    elif winner == 'IA':
        if puntaje > top.get_ult_top10(admin.get_dificultad()):
            sg.popup('Haz Perdido la Partida! /n tu puntaje fue lo suficientemente alto para entrar en el TOP10!',no_titlebar=True)
            top.actualizar(player.get_name,puntaje,admin.get_dificultad)
        else:
            sg.popup('Haz Perdido la Partida! /n tu puntaje no alcanzo para entrar en el TOP!)',no_titlebar=True)

    else:
        if puntaje > top.get_ult_top10(admin.get_dificultad()):
            sg.popup('Haz empatado con la IA! /n tu puntaje fue lo suficientemente alto para entrar en el TOP10!',no_titlebar=True)
            top.actualizar(player.get_name,puntaje,admin.get_dificultad)
        else:
            sg.popup('Haz empatado con la IA! /n tu puntaje no alcanzo para entrar en el TOP10!',no_titlebar=True)
    pass
