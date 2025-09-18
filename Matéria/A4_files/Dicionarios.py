# Dicionários não são ordenados e não usam index mas sim mapping    
# Acesso a key: value em vez de index 0 1 2 3
# type struct
# mutáveis

meudicionario= { "nome": "João", "idade":30}

print("Construido" ,meudicionario)
# alterar valor
meudicionario["nome"]="Pedro"

print("Alterado valor de key nome: " ,meudicionario)


for key , value in meudicionario.items():
    print(f"Key do dicionario = {key} - valor dela = {value}")

#funções úteis

print("items ",meudicionario.items())
print("keys ",meudicionario.keys())
print("values ",meudicionario.values())
print("get ",meudicionario.get("nome"))


meudicionario.update({"nome": "Antonio" , "idade":45})
print("itens " ,meudicionario.items() )
meudicionario["nomeproprio"]=meudicionario["nome"]
print("itens " ,meudicionario.items() )
del meudicionario["nome"]
print("itens " ,meudicionario.items() )



