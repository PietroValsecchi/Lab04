from standStandard import StandStandard

class StandPreseElettriche(StandStandard):
    def __init__(self,codice, superficie, padiglione, prezzo, prese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__prese= int(prese)


    @property
    def prese(self):
        return self.__prese

    def __str__(self):
        if self.disponibile():
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return (f"Codice: {self.codice_stand} - " f"Superficie: {self.superficie:.2f}mq - " f"Padiglione: {self.padiglione} - " f"Prezzo: {self.prezzo:.2f}€ - " f"Numero prese: {self.prese} - " f"{stato}")

