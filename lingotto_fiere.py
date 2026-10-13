from csv import reader
from standStandard import StandStandard
from standPreseElettriche import StandPreseElettriche
from standPremium import StandPremium
from espositore import Espositore

class LingottoFiere:

    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.listaStandStandard = []
        self.listaStandPreseElettriche = []
        self.listaStandPremium = []
        self.listaEspositori = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        file = open(file_path, "r")
        dati=reader(file)
        for dato in dati:
            if dato[0][0] == "S":
                codice = dato[0]
                superficie = int(dato[1])
                padiglione = dato[2]
                prezzo = int(dato[3])
                if dato[4] == "":
                    stand = [codice, superficie, padiglione, prezzo]
                    self.listaStandStandard.append(stand)

                elif dato[4].isdigit():
                    prese= int(dato[4])
                    prezzo = prezzo * (1 + 0.07*prese)
                    stand = [codice, superficie, padiglione, prezzo, prese]
                    self.listaStandPreseElettriche.append(stand)


                else:
                    posizione = dato[4]
                    prezzo =  1.30*prezzo
                    stand = [codice, superficie, padiglione, prezzo, posizione]
                    self.listaStandPremium.append(stand)

            elif dato[0][0] == "E":
                codice = dato[0]
                nome = dato[1]
                cognome = dato[2]
                espositore = [codice, nome, cognome]
                self.listaEspositori.append(espositore)



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
