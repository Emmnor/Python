# Dyrebutikk

#*  ---- Konstruerer klasser ----

class Dyr():
    def __init__(self, Navn:str, Art:str, Pris:float, Beskrivelse:str, ID:int) -> None:
        """
        Initialiserer atributter

        Args:
            Navn (str): Navnet på byret
            Art (str): Arten til dyret
            Pris (float): Prisen til dyret
            Beskrivelse (str): Kort beskrivelse om dyret
            ID (int): Unik ID til dyret
        """
        
        self.navn = Navn
        self.art = Art
        self.pris = Pris
        self.beskrivelse = Beskrivelse
        self.id = ID
    
    
    def info(self):
        """
        Printer alle atributtene til Dyret
        """
        
        print(f' -- Info om {self.Navn} --')
        print(f'Klasse:\t\t{self.__class__.__name__}')
        print(f'Art:\t\t{self.Art}')
        print(f'Pris:\t\t{self.Pris} kr')
        print(f'Beskrivelse\t{self.Beskrivelse}\n')
        



# 3 arveklasser
class Insekt(Dyr):
    def __init__(self, Navn:str, Art:str, Pris:float, Beskrivelse:str, ID:int) -> None:
        """
        Arver alle atributter fra Dyr
        """
        
        super().__init__(Navn, Art, Pris, Beskrivelse, ID)
    
    
    def info(self):
        """
        Arver info funksjonen til Dyr
        """
        
        return super().info()



class Pattedyr(Dyr):
    def __init__(self, Navn:str, Art:str, Pris:float, Beskrivelse:str, ID:int) -> None:
        """
        Arver alle atributter fra Dyr
        """
        
        super().__init__(Navn, Art, Pris, Beskrivelse, ID)
    
    
    def info(self):
        """
        Arver info funksjonen til Dyr
        """
        
        return super().info()



class Fisk(Dyr):
    """
        Arver alle atributter fra Dyr
    """
        
    def __init__(self, Navn:str, Art:str, Pris:float, Beskrivelse:str, ID:int, vanntype:str) -> None:
        super().__init__(Navn, Art, Pris, Beskrivelse, ID)
        self.vanntype = vanntype
    
    
    def info(self):
        """
        Arver info funksjonen til Dyr
        """
        
        return super().info()



class Butikk():
    def __init__(self, Navn:str) -> None:
        """
        Initialiserer atributtene til Butikken
        Lager en ordbok som skal inneholde alle dyrene butikken selger

        Args:
            Navn (str): Navnet på butikken
        """
        
        self.navn = Navn
        self.inventar = {}
        
    
    def RegistrerDyr(self, Dyr:object):
        """
        Registrering av dyr
        Ikke mulig å regisrere ett dyr 2 ganger
        Må ha en egen ID

        Args:
            Dyr (object): Dyre objekt
        """
        
        if any(e == Dyr for e in self.inventar.values()) == True:
            print("Dyret er allerede registrert i butikken")
            return
        else:
            if any(e == Dyr.id for e in self.inventar.keys()) == True:
                print("ID-en er allerede i bruk")
            else:
                self.inventar.update({Dyr.id: Dyr})
                print("Nytt dyr registrert i dyrebutikk")
                
    
    def Oversikt(self):
        """
        Printer ut en oversikt over alle dyrene samt tilleggsinformasjon
        """
        
        print(" -- Inventarliste -- ")
        for dyr in self.inventar.values():
            print(f'Artgruppe: \t{dyr.__class__.__name__}')
            print(f'Art: \t\t{dyr.art}')
            print(f'Navn: \t\t{dyr.navn}')
            print(f'Pris: \t\t{dyr.pris}kr\n')
    
    
    def OversiktArt(self, Art:str):
        """
        Printer ut alle dyrene som er av samme art

        Args:
            Art (str): Hvilken art skal vises
        """
        
        print(f' -- Inventarliste {Art} -- ')
        for dyr in self.inventar.values():
            if dyr.art == Art:
                print(f'Navn: \t\t{dyr.navn}')
                print(f'Pris: \t\t{dyr.pris}kr')
                print(f'Beskrivelse: \t{dyr.beskrivelse}\n')



class Kunde():
    def __init__(self, Navn:str) -> None:
        """
        Initialiserer atributtene til kunden
        Også en ordbok som funker som en handlekurv

        Args:
            Navn (str): Navnet til kunden
        """
        
        self.navn = Navn
        self.handlekurv = {}
    
    
    def LeggTilDyr(self, Dyr:object, Butikk:object):
        """
        Funksjon som legger til dyr i handlekurven til kunden

        Args:
            Dyr (object): Hvilket dyr skal legges til i handlekurven
            Butikk (object): Hvilken butikk skal dyret kjøpes fra
        """
        
        if Dyr in Butikk.inventar.values():
            self.handlekurv.update({Dyr.id:Dyr})
            del Butikk.inventar[Dyr.id]
            print("Dyret er lagt til i handlekurven")
        else:
            print("Dyret er ikke registrert i butikken")
    
    
    def FjernDyr(self, Dyr:object, Butikk:object):
        """
        Fjerner ett dyr fra handlekurven

        Args:
            Dyr (object): Dyret som skal fjernes
            Butikk (object): Hvilken butikk den skal legges tilbake i
        """
        
        if Dyr in self.handlekurv.values():
            Butikk.inventar.update({Dyr.id:Dyr})
            del self.handlekurv[Dyr.id]
            print("Dyret er fjernet fra handlekurven")
        else:
            print("Dyret er ikke i handlekurven")
    
    
    def visHandlekurv(self):
        """
        Funksjon som printer ut alle dyrene som er i handlekurven
        Beregnes totalt antall dyr i handlekurven 
        Beregnes totalpris på alle dyrene i handlekurven
        """
        
        Total = 0
        Pris = 0
        print(f' -- Handlekurv til {self.navn} -- ')
        for dyr in self.handlekurv.values():
            print(f'Artgruppe: \t{dyr.__class__.__name__}')
            print(f'Art: \t\t{dyr.art}')
            print(f'Navn: \t\t{dyr.navn}')
            print(f'Pris: \t\t{dyr.pris}kr')
            print(f'Beskrivelse\t {dyr.beskrivelse}\n')
            
            Total += 1
            Pris += dyr.pris
        
        print(f'Totalprisen er:\t{Pris} \nAntall dyr: \t{Total}\n')



#* --- Konstruering av objektene ---

Dyrebutikken = Butikk("Sarpsborg dyrebutikk")

Mygg = Insekt("Sondre", "Mygg", 10, "Liten irriterende mygg", 1)
Hund = Pattedyr("Sofie", "Hund", 5000, "Golden retreaver med brun pels", 2)
Hund2 = Pattedyr("Flekken", "Hund", 7999, "Liten pomeranien med lang lys pels", 2)
Abbor = Fisk("Kjetil", "Abbor", 500, "Aggresiv abbor, kan bite", 3, "ferskvann")
Katt = Pattedyr("Nøste", "Katt", 6999, "Svart katt med noe hvite flekker", 4)
Katt2 = Pattedyr("Bajas", "Katt", 6999, "Grå katt", 5)
Katt3 = Pattedyr("Rickart", "Katt", 6999, "Svart katt med tjukk pels", 6)
Gjedde = Fisk("Finn", "Gjedde", 500, "Grå gjedde", 9, "ferskvann")

kunde1 = Kunde("Emma")


#* --- Anvendelse av funksjonene ---

Dyrebutikken.RegistrerDyr(Mygg)
Dyrebutikken.RegistrerDyr(Hund)
Dyrebutikken.RegistrerDyr(Hund2)
Dyrebutikken.RegistrerDyr(Abbor)
Dyrebutikken.RegistrerDyr(Abbor)
Dyrebutikken.RegistrerDyr(Katt)
Dyrebutikken.RegistrerDyr(Katt2)
Dyrebutikken.RegistrerDyr(Katt3)

Dyrebutikken.Oversikt()
Dyrebutikken.OversiktArt("Katt")

kunde1.LeggTilDyr(Hund, Dyrebutikken)
kunde1.LeggTilDyr(Abbor, Dyrebutikken)
kunde1.LeggTilDyr(Gjedde, Dyrebutikken)



Dyrebutikken.Oversikt()
kunde1.visHandlekurv()

kunde1.FjernDyr(Abbor, Dyrebutikken)
kunde1.FjernDyr(Hund2, Dyrebutikken)

Dyrebutikken.Oversikt()

kunde1.visHandlekurv()

