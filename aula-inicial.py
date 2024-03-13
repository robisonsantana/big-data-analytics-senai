#AULA INICIAL DO CURSO DE FUNDAMENTOS DE BIG DATA E ANALYTICS COM PYTHON

#Comando para mostrar algo na tela
print("Hello World!")


#Comando para inserir algum valor em uma variável
a = input("\nDigite um número ou uma palavra: ")
print(a)


#Comando para atribuir um valor expecifico (inteiro) numa variável
b = int(input("\nDigite um número: "))


#Comando para mostrar o tipo da variável
print(type(a))
print(type(b))


#Recebendo números inteiros, somando e mostrando o resultado
print("\nSoma")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
s = x + y
print("A soma de ", x," + ", y, " é igual a ", s) 

#Recebendo números inteiros, subtraindo e mostrando o resultado
print("\nSubtração")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
s = x - y
print("A subtração de ", x," - ", y, " é igual a ", s) 

#Recebendo números inteiros, multiplicando e mostrando o resultado
print("\nMultiplicação")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
s = x * y
print("A multiplicação de ", x," * ", y, " é igual a ", s) 

#Recebendo números inteiros, dividindo e mostrando o resultado
print("\nDivisão")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
s = x / y
print("A divisão de ", x," / ", y, " é igual a ", s) 


#Convertendo uma String em um Inteiro
a = input("\nDigite um número: ")
print(type(a))

b = int(a)
print(type(b))


#Estrutura de decisão
n1 = int(input("\nDigite a média do aluno: "))
if(n1 >= 7): 
    print("Aprovado!")
else:
    print("Reprovado!")
    

#Exercício usando estrutura de decisão
#Calcule a média do aluno e mostre se ele foi aprovado, reprovado ou para o concelho:
n1 = float(input("\nDigite a nota da primeira prova do aluno: "))
n2 = float(input("Digite a nota da segunda prova do aluno: "))
n3 = float(input("Digite a nota da terceira prova do aluno: "))
media = (n1 + n2 + n3) / 3
if(media >= 7):
    print("Aprovado!")
elif(media >= 5 and media < 7):
    print("Conselho!")
else:
    print("Reprovado!")


#Estrutura de repetição (while)
count = 1
print("\nContador de 1 até 5:")
while(count <= 5):
    print(count)
    count += 1

#Estrutura de repetição (for)
print("\nContador de 0 até 9:")
for n in range(0, 10):
    print(n)

#Exercício "Classificar salário"
#Receba um salário e mostre de a pessoa está numa classe baixa, média ou alta
#Parâmetros:
#Abaixo do salário mínimo = baixa
#Até 5x o salário mínimo = média
#Acima de 10x o salário mínimo = alta
salarioMinimo = 1412
salario = int(input("\nDigite o seu salário: "))
if(salario >= (salarioMinimo * 10)):
    print("Classe alta")
elif(salario >= (salarioMinimo * 5)):
    print("Classe média")
else:
    print("Classe baixa")

