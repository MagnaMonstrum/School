age = int(input("geef je leeftijd: "))
citizen = input("Nederlands paspoort: ")

if age >= 18 and citizen == "ja":
    print("Gefeliciteerd, je mag stemmen!")
if age < 18 or citizen == "nee": 
    print("Sorry, je mag niet stemmen")
    