cijferPROJA = 7.5
CijferPROG = 7.5
CijferMOD = 7.5


gemiddelde = (cijferPROJA + CijferPROG + CijferMOD) / 3
beloning = gemiddelde * 90
overzicht = "Mijn cijfers (gemiddeld een " + str(gemiddelde) + ") " + "leveren een beloning op van €" + str(beloning) + " op!"


print(overzicht)

