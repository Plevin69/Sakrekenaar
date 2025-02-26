import os
# maak 'n lys met 'n naam en prys veranderlike sodat nuwe produkte bygevoeg kan word
def add_produk(lys, naam, prys):
    lys.append({'naam': naam, 'prys': prys})
# vat die nommer van die produk op die lys en verwyder daardie nommer van die lys
def remove_produk(lys, nom):
    print(f"Produk verwyder: {lys[nom]['naam']}")
    lys.pop(nom)
# maak die terminal skoon vir die gebruiker
def skoon():
    os.system('cls')
# lys al die produkte met hul prys, en die totaal aan die onderkant
def wys_produkte(lys):
    totaal = 0
    for produk in lys:
        print(f"{produk['naam']}      R{produk['prys']}")
        totaal += produk['prys']
    print("*" * 10)
    print(f"Totaal: R{totaal}")
# sent veranderlike word gebruik om while loop te stop
def sisteem():
    sent = 1
    lys = []
# as die sent veranderlike nie nul is nie dan voer die program uit

    while sent != 0:
        print("\nTik een van die letters in:")
        print('a om produk by te voeg')
        print('b om produk te verwyder')
        print('c om produkte te vertoon')
        print('s om uitset skoon te vee')
        print('p om program toe te maak')
    # gebruiker kan net uit die lys van opsies kies, anders word 'n foutboodskap gegee
        toevoer = input('Kies \'n opsie: ')
        if toevoer in ['a','b','c','p','s']:
            if toevoer == 'p':
                sent = 0
                print('Gebruiker het program toegemaak.')
            elif toevoer == 'a':
                produk = input("Naam van nuwe produk: ")
                # die produk se prys moet 'n regte getal wees, anders word 'n foutboodskap gegee
                try:
                    prys = float(input("Prys van nuwe produk: R"))
                    add_produk(lys, produk, prys)
                    print(f"{produk} vir R{prys}, is by die lys gevoeg")
                except ValueError:
                    print('Tik asseblief \'n prys in vir die produk')
            elif toevoer == 'b':
                # die nommer wat moet verwyder word word gebruik om die funksie te roep, en 'n foutboodskap vertoon as die gebruiker se toever nie 'n nommer in die lys is nie 
                nom = int(input('Nommer van produk wat verwyder moet word: ')) - 1
                try:
                    remove_produk(lys, nom)
                except IndexError:
                    print('Het niks verwyder nie, tik die nommer van die produk op die lys in om hom te verwyder', nom)
            elif toevoer == 'c':
                wys_produkte(lys)
            elif toevoer == 's':
                skoon()
        else:
            print('Kies asseblief een van die opsies uit die lysie')

# die funksie met die program hardloop
sisteem()