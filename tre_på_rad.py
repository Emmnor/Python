"""
Lag et «Tre på rad»-spill som bruker en 2D-liste med tre rader og tre kolonner. 
Du kan fylle lista med mellomrom « » eller en annen verdi. For spillere, kan du bruke x og o. 
Deretter skal du lage en løkke som gjentas helt til spillet er ferdig. 
Løkken skal be bruker skrive inn en rad, kolonne og symbol, og legge til angitt 
symbol i 2D-lista. Her bør du legge inn en test som sjekker om feltet er opptatt fra før.
Når er bruker har lagt til et symbol, skal spillbrettet skrives ut som en tabell, 
eller en annen ryddig måte, og spillet avsluttes når én av spillerne har vunnet, 
eller om alle plassene på brettet er opptatt 
"""

Spillebrett = [
    [" ", "", ""],
    ["", " ", " "],
    [" ", "", ""]
]

game = False
runder = 0

def run_game():
    global game
    global runder
    
    rad = int(input("Hvilken rad? "))
    kolonne = int(input("Hvilken kolonne? "))
    symbol = str(input("Hvilket symbol? x/o "))

    if symbol == "x" or symbol == "o":
        print(Spillebrett[rad-1][kolonne-1])
        if Spillebrett[rad-1][kolonne-1] == "o" or Spillebrett[rad-1][kolonne-1] == "x":
            print("Dette feltet er opptatt ")
        else:
            Spillebrett[rad-1][kolonne-1] = symbol    
    else:
        print("Ugjyldig inputt")
    
    for i in range (len(Spillebrett)):
        print(Spillebrett[i])


    if(symbol == "x" or symbol == "o"): #? Den her gjør vel egt ingenting
        for i in range(len(Spillebrett)):
            if(Spillebrett[i][0] == Spillebrett[i][1] and Spillebrett[i][0] == Spillebrett[i][2]):
                print("Spiller " + Spillebrett[i][0] + " vant!")
                print("")
                game = False

            if (Spillebrett[0][i] == Spillebrett[1][i] and Spillebrett[0][i] == Spillebrett[2][i]):
                print("Spiller " + Spillebrett[0][i] + " vant!")
                print("")
                game = False

        if(Spillebrett[0][0] == Spillebrett[1][1] and Spillebrett[0][0] == Spillebrett[2][2]):
            print("Spiller " + Spillebrett[0][0] + " vant!")
            print("")
            game = False
            
        if(Spillebrett[0][2] == Spillebrett[1][1] and Spillebrett[0][0] == Spillebrett[0][2]):
            print("Spiller " + Spillebrett[0][2] + " vant!")
            print("")
            game = False
    
    runder += 1
    
    if runder == 9:
        print("Ingen spillere fikk 3 på rad.")
        game = False



def pre_game():
    global game
    
    for i in range (len(Spillebrett)):
        print(Spillebrett[i])
    
    game = True

    while game == True:
        run_game()
    
    a = str(input("Ønsker du å spille igjen? j/n  "))
    
    if a.upper() == "J":
        pre_game()
    else:
        print("Ok. ")

pre_game()
