#PRIMEIRA AULA DE INTEGRAÇÃO DE BANCO DE DADOS COM O PYTHON
#CONHECENDO COMANDOS

#Importando biblioteca "psycopg2" para permitir que o Python se comunique com o PostgreSQL 
import psycopg2

#Conexão com banco de dados do PostgreSQL
connection = psycopg2.connect(host="127.0.0.1", database="senai", user="postgres", password="senai", port=5432)

#Cursor para executar consultas SQL no banco de dados, recuperar dados e realizar outras operações, 
#como inserção, atualização ou exclusão de dados.
cursor = connection.cursor()

insert = "INSERT INTO clientes(cliente, estado, sexo, status) VALUES('Diana Meira', 'BA', 'F', 'Diamond')"
#Comando .execute para executar alguma ação no banco de dados
cursor.execute(insert)
#Comando .commit para salvar alterações no banco de dados
connection.commit()

query = "SELECT * FROM clientes"
#Cursor executa o comando SQL
cursor.execute(query)

#.fetchall é chamado para recuperar todos os dados lidos pelo cursor e armazenando eles numa tupla
records = cursor.fetchall()

#Mostrando as tuplas com os dados
for row in records :
    print("Nome = ", row[1])
    print("Estado = ", row[2])
    print("Status = ", row[4], "\n")
    
cursor.close()
connection.close()
