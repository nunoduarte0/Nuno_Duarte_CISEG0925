#Exercício 1: Criar um dicionário simples

#Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
#1-	Inserir
#2-	Listar
#O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
#Exemplo:
#nome: Maria
#idade: 20
#curso: Engenharia


alunos= {}



while True:
    print("1- Inserir")
    print("2- Listar")
    print("3- Sair")

    opcao=input("Escolha uma opção: ")

    if opcao=="1":
        nome=input("Digite o nome do aluno: ")
        idade=input("Digite a idade do aluno: ")
        curso=input("Digite o curso do aluno: ")

        alunos={ "nome" : nome, "idade": idade, "curso": curso}

    elif opcao=="2":
        print(alunos.items() )

    elif opcao=="3":
        print("A sair...")
        break

    else:
        print("Opção inválida, escolha uma das opções do Menu:")


    




