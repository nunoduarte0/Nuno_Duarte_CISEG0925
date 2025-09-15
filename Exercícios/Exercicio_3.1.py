#Exercicio 3.1 Corrigir o problema com a troca Extra.


listaNome=["Dario Quental","Dario Almeida","Bruno Carvalho"]
# index         0               1                 2
#length 6
 

il=1
 
 
while il<len(listaNome):       # Loop controla as voltas a lista
    i=0                # reposiçao do index da lista 1 dimensão ( Nome )
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

                elif ord(listaNome[i][it]) < ord(listaNome[i+1][it]):
                    break
                it+=1                       
        i+=1
    il+=1

print("Lista Ordenada: " ,listaNome)
 
        