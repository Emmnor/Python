# --- Låne-system Bibliotek ----

#* Klasser
class Bibliotek():
    def __init__(self, Navn:str) -> None:
        """
        Hva slags atributter som Biblioteket skal ha

        Args:
            Navn (str): Navnet på biblioteket
        """
        
        self.navn = Navn
        self.bøker = {}
        self.kunder = {}
    
    def RegistrerKunde(self, Kunde:object):
        """
        Funksjon som legger et kundeobjet inn i en ordbok.
        Kan ikke registrere kunden mer enn en gang

        Args:
            Kunde (object): Et kundeobjekt
        """
        
        
        if any(e == Kunde for e in self.kunder.values()) == True:
            print("Kunden er allerede registrert")
            return
        else:
            """
            if any(e == Kunde.Lånenummer for e in self.kunder.values().Lånenummer) == True:
                print("Du kan ikke registrere en kunde med samme lånenummer")
            """
            
            for ob in self.kunder.values():
                if getattr(Kunde, "lånenummer") == getattr(ob, "lånenummer"):
                    print("Du kan ikke registrere en kunde med samme lånenummer")
                    return
            
            self.kunder.update({ Kunde.lånenummer: Kunde })
            print("Kunde registrert")

    def RegistrerBok(self, Bok:object):
        """
        Registrerer et bok objekt i en ordbok
        Kan ikke registreres flere ganger

        Args:
            Bok (object): Et bokobjekt
        """
        
        if any(e == Bok for e in self.bøker.values()) == True:
            print("Boka er allerede registrert")
        else:
            
            for ob in self.bøker.values():
                if getattr(Bok, "ISBN") == getattr(ob, "ISBN"):
                    print("Du kan ikke registrere en Bok med samme ISBN-Nummer")
                    return
            
            self.bøker.update({ Bok.titel: Bok })
            print("Bok registrert")
       
    def OversiktKunder(self):
        """
        Viser en oversikt over alle registrerte kunder
        """
        
        print("\n --- Oversikt over Kunder --- \n")
        for kunde in self.kunder:
            print(f'Navn:\t\t{self.kunder[kunde].navn}')
            print(f'Lånenummer:\t{self.kunder[kunde].lånenummer}')
            print(f'Aktive lån: \t{len(self.kunder[kunde].låner)}\n')

    def OversiktBøker(self):
        """
        Viser en oversikt over alle registrerte bøker
        """
        
        print("\n --- Oversikt over Bøker --- \n")
        for bok in self.bøker:
            print(f'Navn:\t\t{self.bøker[bok].titel}')
            print(f'Forfatter: \t{self.bøker[bok].forfatter}')
            print(f'Utgivelsesår: \t{self.bøker[bok].utgivelsesår}')
            print(f'Forlag:\t\t{self.bøker[bok].forlag}')
            try:
                print(f'Sjanger:\t{self.bøker[bok].sjanger}\n')
            except AttributeError:
                print(f'Fagfelt:\t{self.bøker[bok].fagfelt}\n')

    def Søk(self, Lånenummer:int):
        """
        Søker i Kunde ordboken og finner korespinderende lånenummer.
        Viser info om denne kunden hvis den finnes
        """
        
        
        if any(e == Lånenummer for e in self.kunder.keys()) == True:
            print(f'\n--- Info om lånenummer {Lånenummer} --- ')
            for kunde in self.kunder:
                if self.kunder[kunde].lånenummer == Lånenummer:
                    bøker =[]
                    for bok in self.kunder[kunde].låner:
                        bøker.append(bok.titel)
                    print(f'Navn:\t\t{self.kunder[kunde].navn}')
                    print(f'Lån:\t\t{bøker}\n')
        else:
            print(f'Lånenummeret {Lånenummer} er ikke registrert til noen kunde')
        
    def LånBok(self, Kunde:object, Bok:object):
        """
        Legger et bokobjekt inn i låner listen til kunden
        """
        
        if Kunde not in self.kunder.values():
            print("Kunden er ikke registret i biblioteket")
            return
        
        if len(Kunde.låner) >= 3:
            print("Du kan ikke låne flere bøker")
            return
        
        if any(e == Bok.titel for e in self.bøker.keys()):
            Kunde.låner.append(Bok)
            del self.bøker[Bok.titel]
            print("Boka ble lånt")
        else:
            print("Boka du prøver å låne finnes ikke i biblioteket")
    
    def LeverBok(self, Kunde:object, Bok:object):
        """
        Leverer inn boka til bibioteket igjen
        """

        
        if any(e == Kunde for e in self.kunder.values()) == True:
            if Bok in Kunde.låner:
                Kunde.låner.remove(Bok)
                self.bøker.update({ Bok.titel: Bok })
                print("Levering fullført")
            elif Bok not in Kunde.låner:
                print("Boka du prøver å levere har ikke kunden lånt")
            else:
                print("Levering feilet")
        else:
            print("Kunden som prøver å levere tilbake boka er ikke registret i biblioteket")

class Bok():
    def __init__(self, Titel:str, Forfatter:str, Utgivelsesår:int, Forlag:str, ISBNnummer:int) -> None:
        """
        Initialiserer atributter til bok-objektet

        Args:
            Titel (str): Tittel på boka
            Forfatter (str): Forfatteren til boka
            Utgivelseår (int): Året boka ble utgitt
            Forlag (str): Forlaget til boka
            ISBNnummer (int): Unikt nummer til boka
        """
        
        self.titel = Titel
        self.forfatter = Forfatter
        self.utgivelsesår = Utgivelsesår
        self.forlag = Forlag
        self.ISBN = ISBNnummer

class Skjønnlitterær(Bok):
    def __init__(self, Titel: str, Forfatter: str, Utgivelsesår: int, Forlag: str, ISBNnummer: int, Sjanger:str) -> None:
        """
        Arver fra bok klassen. har igså sjanger som atributt

        Args:
            Titel (str): Tittel på boka
            Forfatter (str): Forfatteren til boka
            Utgivelseår (int): Året boka ble utgitt
            Forlag (str): Forlaget til boka
            ISBNnummer (int): Unikt nummer til boka
            Sjanger (str): Sjangeren til boka
        """
        
        super().__init__(Titel, Forfatter, Utgivelsesår, Forlag, ISBNnummer)
        self.sjanger = Sjanger

class Fag(Bok):
    def __init__(self, Titel: str, Forfatter: str, Utgivelsesår: int, Forlag: str, ISBNnummer: int, Fagfelt:str) -> None:
        """
        Arver fra bok klassen. har igså fagfelt som atributt

        Args:
            Titel (str): Tittel på boka
            Forfatter (str): Forfatteren til boka
            Utgivelseår (int): Året boka ble utgitt
            Forlag (str): Forlaget til boka
            ISBNnummer (int): Unikt nummer til boka
            Fagfelt (str): Fagfeltet til boka
        """
        
        super().__init__(Titel, Forfatter, Utgivelsesår, Forlag, ISBNnummer)
        self.fagfelt = Fagfelt

class Kunde():
    def __init__(self, Navn:str, Lånenummer:int) -> None:
        """
        Kundeobjekt som representerer en kunde
        Har også en liste med bøker som den låner

        Args:
            Navn (str): Navnet til kunden
            Lånenummer (int): Unikt lånenummer for en kunde
        """
        
        self.navn = Navn
        self.lånenummer = Lånenummer
        self.låner = []




#* Lager objekter

biblio = Bibliotek("Tune Bibliotek")
kunde1 = Kunde("Emma", 1)
kunde2 = Kunde("Rashmi", 2)
kunde3 = Kunde("Lineve", 1)
kunde4 = Kunde("Anders",3 )
bok1 = Fag("Dinosaurer", "Einstein", 1960, "Capelen Dam", 9856712519472, "Dyr")
bok2 = Skjønnlitterær("Harry Potter", "JK rolling", 2005, "Capelen Dam", 3851048210462, "Fantasy")
bok3 = Fag("The Great Design ", "Steven Hawking", 2015, "Capelen Dam", 230498239487, "Verdensrommet")
bok4 = Fag("Arv og Miljø", "Charles Darwin", 1934, "Capelen Dam", 23748, "Biologi")
bok5 = Skjønnlitterær("Ringenes herre", "Tolken", 1980, "Capelen Dam", 3851048210462, "Fantasy")



biblio.RegistrerKunde(kunde1)
biblio.RegistrerKunde(kunde2)
biblio.RegistrerKunde(kunde2)
biblio.RegistrerKunde(kunde3)
biblio.OversiktKunder()


biblio.RegistrerBok(bok1)
biblio.RegistrerBok(bok2)
biblio.RegistrerBok(bok2)
biblio.RegistrerBok(bok3)
biblio.RegistrerBok(bok4)
biblio.RegistrerBok(bok5)
biblio.OversiktBøker()

biblio.LånBok(kunde1, bok1)
biblio.LånBok(kunde1, bok1)
biblio.LånBok(kunde1, bok2)
biblio.LånBok(kunde1, bok3)
biblio.LånBok(kunde1, bok4)
biblio.LånBok(kunde4, bok1)

biblio.OversiktBøker()
biblio.OversiktKunder()

biblio.Søk(1)
biblio.Søk(3)

biblio.LeverBok(kunde1, bok2)
biblio.LeverBok(kunde1, bok5)
biblio.LeverBok(kunde4, bok1)
biblio.OversiktBøker()
biblio.Søk(1)