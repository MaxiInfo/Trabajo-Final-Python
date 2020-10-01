import PySimpleGUI as sg
import archivosPy.top.actualizar_top as top

def End(player,IA,admin):
    player.mod_puntaje(admin.calcular_sobrante(player.get_fichas()))
    puntaje = player.get_puntaje()
    winner = 'Empate'
    if puntaje > IA.get_score():
        winner = 'Player'
    elif puntaje < IA.get_score():
        winner = 'IA'
    if winner == 'Player':
        if puntaje > top.get_ult_top10(admin.get_dificultad()):
            sg.popup('Felicidades haz ganado la partida conseguiste un puntaje los suficientemente alto para entrar en el TOP10!',keep_on_top=True)
            top.actualizar(player.get_name(),puntaje,admin.get_dificultad())
        else:
            sg.popup('Felicidades haz ganado la partida tu puntaje no alcanzo para entrar en el TOP!',keep_on_top=True)
    elif winner == 'IA':
        if puntaje > top.get_ult_top10(admin.get_dificultad()):
            sg.popup('Haz Perdido la Partida! pero tu puntaje fue lo suficientemente alto para entrar en el TOP10!',keep_on_top=True)
            top.actualizar(player.get_name(),puntaje,admin.get_dificultad())
        else:
            sg.popup('Haz Perdido la Partida! y tu puntaje no alcanzo para entrar en el TOP!',keep_on_top=True)

    else:
        if puntaje > top.get_ult_top10(admin.get_dificultad()):
            sg.popup('Haz empatado con la IA! y tu puntaje fue lo suficientemente alto para entrar en el TOP10!',keep_on_top=True)
            top.actualizar(player.get_name(),puntaje,admin.get_dificultad())
        else:
            sg.popup('Haz empatado con la IA! y tu puntaje no alcanzo para entrar en el TOP10!',keep_on_top=True)
    
