class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"Codice: {self.codice} - Nome: {self.nome} - Cognome: {self.cognome}"

    def __eq__(self, other):
        return self.codice == other.codice