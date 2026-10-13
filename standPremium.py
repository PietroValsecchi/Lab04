from standStandard import StandStandard

class StandPremium(StandStandard):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__posizione = posizione

    def __str__(self):
        return f"{self.__codice}, {self.__superficie}, {self.__padiglione}, {self.__prezzo}, {self.__posizione}"