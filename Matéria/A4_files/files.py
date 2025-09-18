# Files txt, json, csv

# 1º passo - carregar conteudo do ficheiro // Open - r

# 2º passo - Acções no ficheiro "Modo" / 
# r (read) , lê
# w (write), reescreve
# a (append), adiciona
# b (binário), 
# x

#3º passo - fechar o ficheiro // close

'''
Open()
read
Close 

program


Open()
write // append
Close 

'''

filename="D:/Atec/asds.txt"
frase=""

manipfile=open(filename, 'r' , encoding='utf-8')
frase=manipfile.read()
manipfile.close()

print(frase)

frase=input("insert a frase")

print("input no programa" ,frase)

manipfile=open(filename, 'w' , encoding= 'utf-8')
manipfile.write(frase)
manipfile.close()
