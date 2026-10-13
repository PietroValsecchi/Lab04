from standStandard import StandStandard

class StandPreseElettriche(StandStandard):
    def __init__(self,codice, superficie, padiglione, prezzo, prese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__prese= int(prese)


    def __str__(self):
        return f"{self.__codice}, {self.__superficie}, {self.__padiglione}, {self.__prezzo}, {self.__prese}"

