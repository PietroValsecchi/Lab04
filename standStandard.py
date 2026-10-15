class StandStandard:
    def __init__(self, codice, superficie, padiglione, prezzo, espositore):
        self.__codice = codice
        self.__superficie = int(superficie)
        self.__padiglione = padiglione
        self.__prezzo = int(prezzo)
        self.__espositore = None

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore

    @property
    def codice_stand(self):
        return self.__codice

    def disponibile(self):
         return self.__espositore is None


    def __str__(self):
        return f"{self.__codice}, {self.__superficie}, {self.__padiglione}, {self.__prezzo}"




