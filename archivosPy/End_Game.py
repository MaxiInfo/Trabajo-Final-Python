import PySimpleGUI as sg

def main(player,IA,admin):
    player.mod_puntaje(admin.calc_sobrante(player.get_fichas()))
    winner = 'Player' if player.get_puntaje() > IA.get_score() elif 'IA' if player.get_puntaje() < IA.get_score()
    if winner == 'Player':
        if player.get_puntaje() > admin.get_ult_top10():
            sg.popup('Felicidades haz ganado la partida con un puntaje de '+str(player.get_puntaje())+' puntos \n ademas conseguiste un puntaje los suficientemente alto para entrar en el TOP10!',no_titlebar=True)
        else:
            sg.popup()
    elif winner == 'IA':
        pass
    else:
        pass
    pass