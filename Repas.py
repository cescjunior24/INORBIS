boy1=19
girl1=16
girl2=29

#Enter boy 1
if(boy1>=18):
    print("You can pass, have a nice day")
else:
    print("You can't pass, go away")

if(girl1>=18):
    print("You can pass, have a nice day")
else:
    print("You can't pass, go away")

if(girl2>=18):
    print("You can pass, have a nice day")
else:
    print("You can't pass, go away")


#loops
portatil_marc=0
for i in range(0,5):
    portatil_marc=portatil_marc+1

print(portatil_marc)

#Llistes
alumnes=["Cristina","Rayan","Oriol","Marc","Francesc","Carla"]

for i in range(0,len(alumnes)):
    print(alumnes[i])
print("""""""""""")
for alumne in alumnes:
    print(alumne)


def SumaNombres(numero1,numero2):
    resultat=numero1+numero2
    return resultat

num1=3
num2=4

num3=50
num4=25

resultat_funcio=SumaNombres(num1,num2)
resultat_funcio2=SumaNombres(num3,num4)

print(resultat_funcio)
print(resultat_funcio2)



