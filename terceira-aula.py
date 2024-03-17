#TERCEIRA AULA DO CURSO DE FUNDAMENTOS DE BIG DATA E ANALYTICS COM PYTHON

#Tuplas
#São valores imutáveis
tupla = (1, 2, 3)
print(type(tupla))

#Transformando tupla em lista
lista = list(tupla)
print(type(lista))

#Transformando lista em tupla
tupla = tuple(lista)
print(type(tupla))


#Dicionário
#São itens que possuem uma chave e um valor
preco = {'Lápis' : 5.5, 'Borracha' : 7.0, 'Caneta' : 6.5}
print("\n", preco)

#Printando o valor de uma chave
print("\n valor = ", preco['Lápis'])

#Inserindo chave valor em um dicionário
preco['Lapiseira'] = 10.0
print("\n", preco)

#Removendo valor em um dicionário
del(preco['Borracha'])
print("\n", preco)


#Mostrando tamanho de uma lista
minha_lista = [1, 2, 3, 4, 5]
tamanho = len(minha_lista)
print("\nO tamanho da minha lista é: ", tamanho)

#Mostrando o maior valor de uma lista
maior_valor = max(minha_lista)
print("Maior valor: ", maior_valor)

#Mostrando o menor valor de uma lista
menor_valor = min(minha_lista)
print("Menor valor: ", menor_valor)

#Arredondando um valor
valor_float = 5.666
valor_int = round(valor_float)
print("\nValor arredondado: ", valor_int)


#Método sort() no Python, organizando a lista em ordem crescente
numeros = [6, 3, 7, 1, 0, 9, 5]
numeros.sort()
print("\nValores em ordem crescente: ", numeros)

#Método sort() no Python para ordem decrescente
numeros.sort(reverse=True)
print("Valores em ordem decrescente: ", numeros)


#Método count() no Python
frutas = ["Maça", "Banana", "Pera", "Banana", "Caju"]
contagem = frutas.count("Banana")
print("\nQuantidade de itens 'Banana' na lista = ", contagem)


#Moda, média e mediana em Python
import statistics
valores = [4, 6, 3, 7, 6, 2, 3, 5, 7, 8, 9, 8, 5, 7, 1]
print("\nModa: ", statistics.mode(valores))
print("Média: ", statistics.mean(valores))
print("Mediana: ", statistics.median(valores))


#Importando método math
import math
print("\nRaiz quadrada de 25 = ", math.sqrt(25))

#Importando uma classe expecífica de um método
from math import pow
print("\n3 ^ 2 = ", pow(3, 2))


#Funções em Python
#Calculadora:
def soma(n1, n2):
    calc = n1 + n2
    return print("\n", n1, " + ", n2, " = ", calc)

def subtracao(n1, n2):
    calc = n1 - n2
    return print("\n", n1, " - ", n2, " = ", calc)

def multiplicacao(n1, n2):
    calc = n1 * n2
    return print("\n", n1, " * ", n2, " = ", calc)

def divisao(n1, n2):
    calc = n1 / n2
    return print("\n", n1, " / ", n2, " = ", calc)

#While para permitir que o programa rode até que o usuário queria sair
while(True):
    controller = int(input("\nCALCULADORA\n1 - Soma \n2- Subtração \n3- Multiplicação \n4- Divisão \n9- Sair \n-> "))
    if(controller == 1):
        n1 = int(input("\nDigite um número: \n-> "))
        n2 = int(input("Digite outro número: \n-> "))
        soma(n1, n2)
    elif(controller == 2):
        n1 = int(input("\nDigite um número: \n-> "))
        n2 = int(input("Digite outro número: \n-> "))
        subtracao(n1, n2)
    elif(controller == 3):
        n1 = int(input("\nDigite um número: \n-> "))
        n2 = int(input("Digite outro número: \n-> "))
        multiplicacao(n1, n2)
    elif(controller == 4):
        n1 = int(input("\nDigite um número: \n-> "))
        n2 = int(input("Digite outro número: \n-> "))
        divisao(n1, n2)
    elif(controller != 1 and controller != 2 and controller != 3 and controller != 4 and controller != 9):
        print("\nComando inválido!")
    else:
        controller = 9
        print("\nPrograma finalizado.")
        break
    



