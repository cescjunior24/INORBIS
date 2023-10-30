



#Suspès, Aprovat, Bé, Notable, Excel·lent
def Notes(nota):
    
    return 0



def Corrector():
    array_resultats=[]
    array_notes=[2,3,4,10,8,5,1,7,6]
    array_correcio=["Suspès","Suspès","Suspès","Excel·lent","Notable","Aprovat","Suspès","Notable","Bé"]

    for i in range(0,len(array_notes)):
        resultat=Notes(array_notes[i])
        array_resultats=array_notes.append(resultat)
    
    if(array_resultats==array_notes):
        print("TEST OK")
    else:
        print("TEST NOT OK")

Corrector()
