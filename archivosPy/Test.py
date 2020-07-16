import PySimpleGUI as sg

sg.popup('Felicidades haz ganado la partida con un puntaje de '+str(player.get_puntaje())+' puntos \n ademas conseguiste un puntaje los suficientemente alto para entrar en el TOP10!',no_titlebar=True)