from csv import reader
from operator import attrgetter
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
        self.espositoriStand = []

        """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r", encoding="utf-8") as file:
            dati=reader(file)
            for dato in dati:
                if dato[0][0] == "S":
                    codice = dato[0]
                    superficie = float(dato[1])
                    padiglione = dato[2]
                    prezzo = float(dato[3])

                    if len(dato) == 4:
                        stand = StandStandard(codice, superficie, padiglione, prezzo)
                        self.listaStandStandard.append(stand)

                    elif dato[4].isdigit():
                        prese = int(dato[4])
                        prezzo = prezzo * (1 + 0.07 * prese)
                        stand = StandPreseElettriche(codice, superficie, padiglione, prezzo, prese)
                        self.listaStandPreseElettriche.append(stand)

                    else:
                        posizione = dato[4]
                        prezzo = prezzo * 1.30
                        stand = StandPremium(codice, superficie, padiglione, prezzo, posizione)
                        self.listaStandPremium.append(stand)


                elif dato[0][0] == "E":
                    codice = dato[0]
                    nome = dato[1]
                    cognome = dato[2]
                    espositore = Espositore(codice, nome, cognome)
                    self.listaEspositori.append(espositore)



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""

        disponibile = True
        standTrovato = None
        espositoreTrovato = None

        for elemento in (self.listaStandStandard + self.listaStandPreseElettriche + self.listaStandPremium):
            if elemento.codice_stand == codice_stand.upper():
                standTrovato = elemento
                break

        if not standTrovato:
            disponibile = False
            raise Exception(f"{codice_stand} non è valido perchè non è presente nel database!")


        for espositore in self.listaEspositori:
            if espositore.codice == codice_espositore.upper():
                espositoreTrovato = espositore
                break

        if not espositoreTrovato:
            disponibile = False
            raise Exception(f"{codice_espositore} non è valido perchè non è presente nel database!")

        if not standTrovato.disponibile():
            raise Exception(f"{codice_stand} già associato a un espositore!")


        for elemento in self.espositoriStand:
           if elemento[1].codice == codice_espositore.upper() :
                disponibile = False
                raise Exception(f"{codice_espositore} già assegnato a uno stand!")


        if disponibile:
            standTrovato.espositore= espositoreTrovato
            self.espositoriStand.append((standTrovato, espositoreTrovato))




    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        for espositore in self.listaEspositori:
            assegnato = False
            for esp in self.espositoriStand:
                if esp[1].codice == espositore.codice:
                    print(f"Espositore: ({espositore}). ---> Codice stand associato: {esp[0].codice_stand}")
                    assegnato = True
                    break
            if not assegnato:
                print(f"Espositore: ({espositore}). ---> Non è associato a nessuno stand!")





    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""

        stand_ordinati = self.listaStandStandard + self.listaStandPreseElettriche + self.listaStandPremium
        stand_ordinati.sort(key=attrgetter('prezzo'))
        return stand_ordinati
