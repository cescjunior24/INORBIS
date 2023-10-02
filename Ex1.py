


from array import array


def MajoroMenor(edat):
    if(edat>=18):
        return True
    else:
        return False



def Corrector():
    edades=[18,32,16,43,8,82,2,4]
    array_booleanos_comprovacion=[True,True,False,True,False,True,False,False]
    array_booleanos=[]
    for i in edades:
        resultat=MajoroMenor(i)
        array_booleanos.append(resultat)
    if(array_booleanos_comprovacion==array_booleanos):
        print("TEST OK")
    else:
        print("TEST NOT OK")

    

    



