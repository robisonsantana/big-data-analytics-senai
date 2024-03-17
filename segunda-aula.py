#SEGUNDA AULA DO CURSO DE FUNDAMENTOS DE BIG DATA E ANALYTICS COM PYTHON

#Lista em Python
listaA = [] #Vazio
listaB = [1, 2, 3, 4, 5, "Robison", 5.666] #Lista com int, String e float
print(listaB)

#Adicionando elementos à lista com o comando .append
listaB.append("Brenda")
print("\n", listaB)

#Subscrevendo e mostrando elemento de uma posição expecifica de uma lista
listaB.insert(4, "Gabriel")
print("\n", listaB[4])

#Removendo elementos de uma lista com o comando .remove
listaB.remove("Robison")
print("\n", listaB)


#Exercício:
#Desenvolva um cadastro comtendo os campos "nome", "sobrenome", "telefone", "idade" e "estado"
#
#Execute: Pesquisa
#         Insere mais nome
#         Excluir o nome mencionado
#lista_cadastro = ["Robison", "Santana", 77098765432, 20, "BA", "Brenda", "Santos", 11567895434, 19, "SP"]
lista_cadastro = [[], [], [], [], []]
lista_cadastro[0] = ["Robison", "Brenda"]
lista_cadastro[1] = ["Santana", "Santos"]
lista_cadastro[2] = [77927354619, 11097483647]
lista_cadastro[3] = [20, 19]
lista_cadastro[4] = ["BA", "SP"]
controller = 0
while(controller != 9):
    controller = int(input("\nMENU PRINCIPAL\n\n1- Pesquisar Nome \n2- Fazer Cadastro \n3- Excluir Nome\n9- Sair \n-> "))
    if(controller == 1):
        nome = input("\nDigite o nome que deseja pesquisa:\n-> ")
        if(nome in lista_cadastro[0]):
            print("Existe na lista")
        else:
            print("Não existe na lista")
    elif(controller == 2):
        nome = input("\nQual nome deseja adicionar à lista?\n-> ")
        lista_cadastro[0].append(nome)
        sobrenome = input("\nAgora digite o sobrenome:\n-> ")
        lista_cadastro[1].append(sobrenome)
        telefone = int(input("\nDigite o telefone da pessoa:\n-> "))
        lista_cadastro[2].append(telefone)
        idade = int(input("\nDigite a idade da pessoa:\n-> "))
        lista_cadastro[3].append(idade)
        estado = input("\nDigete o estado da pessoa:\n-> ")
        lista_cadastro[4].append(estado)
        print(lista_cadastro)
    elif(controller == 3):
        remover_nome = input("\nDigite o nome que deseja remover:\n-> ")
        if(remover_nome in lista_cadastro[0]):
            indice = lista_cadastro[0].index(remover_nome)
            lista_cadastro[0].remove(lista_cadastro[0][indice])
            lista_cadastro[1].remove(lista_cadastro[1][indice])
            lista_cadastro[2].remove(lista_cadastro[2][indice])
            lista_cadastro[3].remove(lista_cadastro[3][indice])
            lista_cadastro[4].remove(lista_cadastro[4][indice])
            print(lista_cadastro)
        else:
            print("Nome não encontrado")
    elif(controller != 1 and controller != 2 and controller != 3 and controller != 9):
        print("Comando Inválido!")
    else:
        print("Programa finalizado!")
        controller == 9

