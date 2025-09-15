
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
    
listaNome=["Dario Quental","Dario Almeida","Bruno Carvalho"]
# index         0               1                 2
#length 6
 
i=0
FlagTroca=True
it=0
controloTroca=-1
il=1
 
 
while il<len(listaNome):       # Loop controla as voltas a lista
    i=0                # reposiçao do index da lista 1 dimensão ( Nome )
    print("Oi")
    print("IL - ",il)
    while i< len(listaNome):  # Loop controla a posiçao do nome
        print("index 1 pos - ",i)
        if i<=len(listaNome)-2:
            it=0  # reposiçao do index da lista 2 dimensão ( Letras )
            controloTroca=-1
            while it<len(listaNome[i]) and it< len(listaNome[i+1]): # Loop controla as letras no nome
               
                # print("Antes do if i    ", i  , "troca  it    ", it )
                if ord(listaNome[i][it]) > ord(listaNome[i+1][it]) and  controloTroca != i :
                    print("If que troca i", i ,"Depois da troca  it", it )
                    print (listaNome[i][it] , "   -   " , listaNome[i+1][it] )
                    controloTroca=i # controlar index da primeira dimençao ( quando acontece troca de nome ja nao é trocado nenhum nome)
                    listaNome.insert(i,listaNome[i+1])
                    print(listaNome)
                    listaNome.pop(i+2)
                    print(listaNome)
                it+=1                        
        i+=1
    il+=1