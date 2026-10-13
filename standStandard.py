class StandStandard:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = int(superficie)
        self.__padiglione = padiglione
        self.__prezzo = int(prezzo)


    def __str__(self):
        return f"{self.__codice}, {self.__superficie}, {self.__padiglione}, {self.__prezzo}"




