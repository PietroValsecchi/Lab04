class StandStandard:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = float(superficie)
        self.__padiglione = padiglione
        self.__prezzo = float(prezzo)
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

    @property
    def superficie(self):
        return self.__superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzo(self):
        return self.__prezzo

    def __str__(self):
        if self.disponibile():
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return (f"Codice: {self.codice_stand} - " f"Superficie: {self.superficie:.2f}mq - " f"Padiglione: {self.padiglione} - " f"Prezzo: {self.prezzo:.2f}€ - " f"{stato}")







