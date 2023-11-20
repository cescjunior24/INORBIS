import random as rand

def main():
    aleatorio=rand.choice([1,2,3])
    print(aleatorio)
    #Escollir nombre aleatori i ho guarda a una variable
    num_maquina=rand.randint(1,3)
    num_persona=0
    while(num_persona<1 or num_persona>3):
        num_persona=int(input("Introduce a number 1 to 3: "))   
    #1: Scissors 2: Paper 3: Rock
    #Cuando Gana la maquina
    if(num_maquina==1 and num_persona==2 or num_maquina==2 and num_persona==3 or num_maquina==3 and num_persona==1) :
        print("The Machine wins")
    elif (num_persona==1 and num_maquina==2 or num_persona==2 and num_maquina==3 or num_persona==3 and num_maquina==1):
        print("The Person wins")
    elif(num_maquina==num_persona):
        print("TIE!")
        

    
    
main()


