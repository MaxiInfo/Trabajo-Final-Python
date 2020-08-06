class jugador ():
    def __init__(self,nombre):
        self._nom = nombre
        self._fichas = []
        self._puntaje = 0
        self._cambios = 0
        
    
    def set_fichas (self,fichas):
        self._fichas = fichas
        

    def get_fichas(self):
        return(self._fichas)

    def get_name(self):
        return self._nom

    def get_cambios(self):
        return self._cambios
    def add_cambio(self):
        self._cambios += 1

    def get_puntaje(self):
        return self._puntaje

    def mod_puntaje (self, add_score):
        self._puntaje += add_score
        
    
    def get_single_ficha (self,pos):
        letter = self._fichas[pos]
        self._fichas[pos]= 0
        return letter

    def set_single_ficha(self, letter, pos):
        self._fichas[pos]= letter
        

    def change_single_ficha(self,letter,pos):
        aux = self.get_single_ficha(pos)
        self.set_single_ficha(letter,pos)
        return aux

    def pos_libre(self):
        pos = self._fichas.index(0)
        return pos

    def ficha_pos (self,pos):
        return self._fichas[pos]