# Cria um programa que peça ao utilizador para introduzir o seu nome completo.
# O programa deve validar se o nome contém apenas letras e espaços, a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, usando os códigos ASCII de cada caractere.

#Exemplo: Pedro Pereira 

#Se o nome for válido, o programa deve exibir:
# "Nome válido!"
#Caso contrário, deve exibir:
# "Nome inválido: contém caracteres não permitidos."

#No caso de o programa encontrar um caractere invalido deve parar a execução.

#Exemplos Inválidos:
#Miguel PriMo
#Luis AnseLmo
#Guilherme ramos

listname=[]

i=0
it=0

name=input("Introduza o seu nome")

listname.append(name)
print(listname)



while i<len(listname):
    it=0
    
    while it<len(listname[i]):
        
      print(listname[i][it])
      it+=1
    i+=1
    
    

for i in name:
  char = ord(i)
  if char >= 65 and char <= 90:
        print("Maiscula encontrada" , char)
    

