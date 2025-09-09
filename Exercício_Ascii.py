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


name = input("Introduza o seu nome completo: ")

for i in name:
  ver=ord(i)
  
  if not ((ver >= 65 and ver <= 90) or (ver >=97 and ver <=122) or ver == 32):
    print("Nome inválido: contém caracteres não permitidos")
    
    
    
for it in range (len(name)):
  if it ==0:
    if (ord(name[it]) >= 65 and ord(name[it]) <=90):
      continue
    
    else:
      print("Primeira letra tem de ser maiuscula.")
      break
    
  elif ord(name[it]) == 32:
    it=it +1
       
    if ord(name[it]) >= 65 and ord(name[it])  <=90:
      continue
      
    else:
      print("Algum nome após espaço não foi inserido com maiuscula")
  
  elif it==len(name)-1:
    print("Nome válido")
    
      
      
      
      
  
    
    
      
    


    
    
    





