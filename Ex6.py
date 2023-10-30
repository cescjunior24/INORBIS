


#crear funció que calculi l'area de un triangle si tens la base i l'altura, si un dels dos es 0 ha de donar 0 l'area
def Calcular_Area_Triangle(base,altura):
    area=0
    return area

def Corrector():
    if(Calcular_Area_Triangle(4,5)==10):
        print("TEST 1 OK")
    else: 
        print("TEST NOT OK")

    if(Calcular_Area_Triangle(0,0)==0):
        print("TEST 2 OK")
    else:
        print("TEST 2 NOT OK")

    if (Calcular_Area_Triangle(10, 2.5) == 12.5):
        print("TEST 3 OK")
    else:
        print("TEST 3 NOT OK")

    
    if (Calcular_Area_Triangle(7.5, 3.5) == 13.125):
        print("TEST 4 OK")
    else:
        print("TEST 4 NOT OK")


Corrector()
