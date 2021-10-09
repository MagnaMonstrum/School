lijst = ['a', 'b', 'c']


def wijzig(letterlijst):
    letterlijst.clear()
    for i in ['d', 'e', 'f']:
        letterlijst.append(i)
    

print(lijst)
wijzig(lijst)
print(lijst)