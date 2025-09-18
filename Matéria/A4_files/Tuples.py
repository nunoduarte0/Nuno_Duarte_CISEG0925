# Declaração
# Não podem mudar nem adicionar depois de criados.
# Podem ser criados enquanto o programa corre.
# Utilizar em dicionários dado que eles são indexados tal como as listas
# Aplicações String que nunca muda, extensões, parâmetros de db, keys de dicionários



my_tuple_extensions=(".exe",".mp3",".docs")
num1=0
num2=0

print(my_tuple_extensions[1])

for ext in my_tuple_extensions:
    print(ext)

num1=int(input("insert a number"))
num2=int(input("insert a number"))

#criar tuple in run time
my_tuple_create=(num1,num2)

for extcreate in my_tuple_create:
    print(extcreate)

numero1,numero2= my_tuple_create

print(numero1)
print(numero2)

