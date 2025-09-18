#Exercicio 4 Ordena as Letras de Z-A de em uma lista com uma unica string.
#       EX: lista=[" EU GOSTO E DO VERAO"]
 

lista = ["EU GOSTO E DO VERAO"]

frase = lista[0]

lista_caracteres = list(frase)

tamanho = len(lista_caracteres)


for i in range(tamanho):
    for j in range(tamanho - 1):
       
        if lista_caracteres[j] < lista_caracteres[j+1]:

            lista_caracteres[j], lista_caracteres[j+1] = lista_caracteres[j+1], lista_caracteres[j]

novafrase = ""
for caractere in lista_caracteres:
    novafrase += caractere


print("Frase Original:", frase)
print("Frase Ordenada:", novafrase)

   
        



    





