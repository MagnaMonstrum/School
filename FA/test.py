def standaardprijs(afstandKM):
    """
    Bepaal de prijs van een treinrit. Iedere treinrit kost 80 cent per kilometer,
    maar als de rit langer is dan 50 kilometer betaal je een vast bedrag van €15,-
    plus 60 cent per kilometer.
    Ga bij invoer van negatieve afstanden uit van een afstand van
    0 kilometer (prijs is dan dus 0 Euro).
    Args:
        afstandKM (int): De reisafstand in kilometers.
    Returns:
        float: De berekende standaardprijs.
    """
    afstandKM = int(input('Hoe veel kilometer wilt u reizen? '))
    if afstandKM <= 0:
        prijs = afstandKM = 0   
    if afstandKM > 50:
        prijs = (afstandKM * 0.6) + 15
    if afstandKM <= 50:
        prijs = afstandKM * 0.8

    return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    """
    Het eerste wat deze functie moet doen, is het aanroepen van
    functie standaardprijs, waarbij de afstand in kilometers doorgegeven
    moet worden om de standaardprijs voor de rit op te vragen.
    Aan de hand van de standaardprijs kan de actuele ritprijs worden berekend.
    De regels zijn als volgt:
     * Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting.
     * In het weekend reist deze groep met 35% korting.
     * Overige leeftijdsgroepen betalen de gewone prijs, behalve in het weekend. Dan reist
       deze leeftijdsgroep met 40% korting.
    Args:
        leeftijd (int): De leeftijd van de reiziger in gehele jaren.
        weekendrit (bool): True als het een rit in het weekend betreft, anders False.
        afstandKM (int): De reisafstand in kilometers.
    Returns:
        float: De berekende ritprijs.
    """
    leeftijd = int(input("Hoe oud bent u? "))
    weekendrit = str(input("Op welke dag wilt u gaan reizen? "))
    ritprijs = standaardprijs(afstandKM)

    # check of het weekend is
    if weekendrit == "zaterdag" or weekendrit == "zondag":
        weekendrit = True
    else:
        weekendrit = False 

    if leeftijd < 12 or leeftijd >= 65:
        newRitprijs = ritprijs * 0.7
        if weekendrit == True:
            newRitprijs = ritprijs * 0.65

    if leeftijd >= 12 or leeftijd < 65 and weekendrit == True:
        newRitprijs = ritprijs * 0.6

    return newRitprijs



ritprijs(int(input('leeftijd? ')), input('dag? '), standaardprijs(int(input('afstand? '))) )
