


def CalcularMitjana(notes):
    mitjana=0

    return mitjana

def Corrector():
    if(CalcularMitjana([3, 7, 5]) == 5.0):
        print("TEST 1 OK")
    else:
        print("TEST 1 NOT OK")
        
    if(CalcularMitjana([30, 0]) == 15.0):
        print("TEST 2 OK")
    else:
        print("TEST 2 NOT OK")

    if (CalcularMitjana([3, 7, 5]) == 5.0):
        print("TEST 3 OK")
    else:
        print("TEST 3 NOT OK")

    if (CalcularMitjana([]) == 0.0):
        print("TEST 4 OK")
    else:
        print("TEST 4 NOT OK")

    if (CalcularMitjana([10, 20, 30, 40, 50]) == 30.0):
        print("TEST 5 OK")
    else:
        print("TEST 5 NOT OK")

    if (CalcularMitjana([1, 2, 3, 4, 5]) == 3.0):
        print("TEST 6 OK")
    else:
        print("TEST 6 NOT OK")

    if (CalcularMitjana([10]) == 10.0):
        print("TEST 7 OK")
    else:
        print("TEST 7 NOT OK")

Corrector()