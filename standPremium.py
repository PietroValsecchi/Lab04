from standStandard import StandStandard

class StandPremium(StandStandard):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    def __str__(self):
        if self.disponibile():
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return (f"Codice: {self.codice_stand} - " f"Superficie: {self.superficie:.2f}mq - " f"Padiglione: {self.padiglione} - " f"Prezzo: {self.prezzo:.2f}€ - " f"Posizione: {self.posizione} - "f"{stato}")

