

def suma100primersnums():
    sumatori=0
    for i in range(0,101):
        sumatori=sumatori+i
    return sumatori




def Corrector():
    resultat=suma100primersnums()
    if(resultat==5050):
        print("TEST OK")
    else:
        print("TEST NOT OK")


Corrector()