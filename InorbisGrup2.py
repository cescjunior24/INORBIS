import random as rand
numero_secreto=int(rand.randint(0,20))
print(numero_secreto)
num_persona=int(input("Adivina el número secreto: "))
while(num_persona!=numero_secreto):
    num_persona=int(input("Adivina el número secreto: "))


    