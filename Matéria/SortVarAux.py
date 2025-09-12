
'''

listaNum=[2,4,6,3,9,2]
#index


i=0
VauAux=0
FlagTroca=True

while FlagTroca:
    FlagTroca=False
    i=0
    while i<len(listaNum):
        if i<len(listaNum)-1:
            print("Valor I actual" , listaNum[i], "Valor I seguinte", listaNum[i+1])
            if listaNum[i]>listaNum[i+1] and i<len(listaNum):
                FlagTroca=True
                print(i, "Index maior", i+1)
                VarAux=listaNum[i] #primeiro guardar a prosição "destruída"

                listaNum[i]=listaNum[i+1] # Copia valor da pos. á frente

                listaNum[i+1]= VarAux # Faz o swap final com o valor guardado
        
        i+=1

    print(listaNum)


'''
    
    
    
listaNome=["Dario Quental", "Dario Almeida" , "Bruno Carvalho"]
#index


i=0
VauAux=""
FlagTroca=True
it=0

while FlagTroca:
    FlagTroca=False
    i=0
    while i<len(listaNome):

        FlagTroca=False       
        if i<=len(listaNome)-2:
            it+=1
            print(len(listaNome[i]), "   -  " ,len(listaNome[i+1]))
            while it< len(listaNome[i]):
                print("Antes do if i" , i , "it" , it)
                if ord(listaNome[i][it]) > ord(listaNome[i+1][it]):
                    print("troca i" , i , "it" , it)
                    print(listaNome[i][it], "   -  "  ,listaNome[i+1][it])
                    FlagTroca=True               
                    listaNome.insert(i,listaNome[i+1])
                    print(listaNome)
                    listaNome.pop(i+2)
                    print(listaNome)
                    break
                it+=1
        
        i+=1
    

print(listaNome)