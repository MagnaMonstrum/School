def uurloonBerekenen():
    uurloon = input("Wat verdien je per uur: ")
    aantalUur = input("Hoeveel uur heb je gewerkt: ")

    uurloonFloat = float(uurloon)
    aantalUurInt = int(aantalUur)
    salaris = uurloonFloat * aantalUurInt

    print(str(aantalUurInt) + " uur werken levert €" + str(salaris) + " op")
    
try:
   uurloonBerekenen()
except ValueError:
    print('voer een getal in!')
    uurloonBerekenen()
