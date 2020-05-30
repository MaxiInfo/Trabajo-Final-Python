class jugador ():
    def __init__(self,nombre,fichas):
        self._nom = nombre
        self._fichas = fichas
        self._puntaje = 0
        pass
    
    def set_fichas (self,fichas):
        self._fichas = fichas
        pass

    def get_fichas(self):
        return(self._fichas)

    def mod_puntaje (self):
        pass
    
    def get_puntaje (self):
        pass

    def get_single_ficha (self,pos):
        letter = self._fichas[pos]
        self._fichas[pos]=0
        return letter

    def set_single_ficha(self, letter, pos):
        self._fichas[pos]= letter
        pass

    def change_single_ficha(self,letter,pos):
        aux = self.get_single_ficha(pos)
        self.set_single_ficha(letter,pos)
        return aux

    def ficha_pos (self,pos):
        return self._fichas[pos]