# berekenings word gedoen met funksies, een vir plus, minus, deel en maal, en om die uitset skoon te maak.
def maal(num1, num2):
    answer = float(num1) * float(num2)
    return answer
def deel(num1, num2):
    answer = float(num1) / float(num2)
    return answer
def plus(num1, num2):
    answer = int(num1) + int(num2)
    return answer
def minus(num1, num2):
    answer = int(num1) - int(num2)
    return answer
def skoon():
    return None

# Die sentinal veranderlike word verklaar as 1, sodat 'n while loop kan hardloop totdat hierdie veranderlike 0 is
sent = 1

while sent != 0:
    print("Om die uitset te verwyder, sleutel 5 in.")
    print("Om die program enige tyd toe te maak, sleutel 6 in.")

# gebruiker word gevra om een van die volgende operators in te sleutel
    user_input = input("Kies een die volgende + - * /: ")

# as die gebruiker 6 kies, word die sentinal variable tot 0 gestel wat die while loop sal stop 
    if user_input == '6':
        print("Gebruiker het die program toegemaak")
        sent = 0
        # as die gebruiker 5 kies, word die skoon funksie geroep wat die uitset skoonmaak
    elif user_input == '5':
        skoon()
        print("Uitset is skoongemaak.\n\n")

# die gebruiker kan net een van die +-*/ operators kies, anders word 'n foutboodskap gegee
# as die gebruiker 'n korrekte operator kies, word hul gevra vir twee getalle wat gebruik gaan word in die berekening
    elif user_input in ['+', '-', '*', '/']:
        num1 = input("Tik die eerste nommer in: ")
        num2 = input("Tik die tweede nommer in: ")
    else:
            print('Toevoer is nie korrek nie. Asseblief sleutel + - * / in.')
# if stellings word gebruik om te bepaal watter operator die gebruiker ingetik het, en roep dieselfde funksie om die berekening te doen
    if user_input == '+':
        print(f"Antwoord: {plus(num1, num2)}")
    
    elif user_input == '-':
        print(f"Antwoord: {minus(num1, num2)}")

    elif user_input == '*':
        print(f"Antwoord: {maal(num1, num2)}")

    elif user_input == '/':
        print(f"Antwoord: {deel(num1, num2):.2f}")