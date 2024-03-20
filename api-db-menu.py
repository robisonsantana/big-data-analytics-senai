#SEGUNDA AULA DE INTEGRAÇÃO DE BANCO DE DADOS COM O PYTHON
#CRIANDO MENU INTERATIVO

# Exemplos de comandos SQL:
# select * from clientes
# select clientes, sexo, status from clientes
# select cliente, sexo, status from clientes where status = 'Silver'
# select cliente, sexo, status from clientes where status = 'Silver' OR status = 'Platinum'
# select cliente, sexo, status from clientes where status IN ('Silver','Platinum')
# select cliente, sexo, status from clientes where cliente like '%Alb%'
# select * from vendas where total > 6000
# select cliente from clientes order by cliente
# select cliente from clientes order by cliente DESC
# select cliente, status from clientes order by cliente desc, status
# select * from vendas where total between 6000 and 8000
# select  * from VENDAS limit 10
# select distinct status from clientes
# select count(*) from vendas
# select count(*) from vendas where total > 6000
# select idvendedor, count(idvendedor) from vendas group by idvendedor
# select idvendedor, count(idvendedor) from vendas group by idvendedor having count(idvendedor) > 40
# select nome, total from vendas, vendedores where vendas.idvendedor = vendedores.idvendedor
# select count(*) from vendas inner join vendedores on(vendas.idvendedor = vendedores.idvendedor)
# select count(*)  from vendas left join vendedores on (vendas.idvendedor = vendedores.idvendedor)
# select count(*)  from vendas right join vendedores on( vendas.idvendedor = vendedores.idvendedor);
# select cliente, total from vendas v inner join clientes c on (v.idcliente = c.idcliente)
# INSERT INTO vendedores(nome) VALUES ('Fernando Amaral');


#Importando biblioteca "psycopg2" para permitir que o Python se comunique com o PostgreSQL 
import psycopg2

controller = 0
#While para criar menu de interação com o banco de dados
while(controller != 9):
    #Conexão com banco de dados do PostgreSQL e Cursor para executar consultas SQL no banco de dados, recuperar dados 
    #e realizar outras operações, como inserção, atualização ou exclusão de dados.
    connection = psycopg2.connect(host="127.0.0.1", database="senai", user="postgres", password="senai", port=5432)
    cursor = connection.cursor()
    #Menu
    controller = int(input("MENU PRINCIAL\n1- Select \n2- Insert \n9- Sair \n-> "))
    #If para executar comandos SQL SELECT
    if(controller == 1):
        query = input("\n-> ")
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print(row)
    #Elif para executar comandos SQL INSERT
    elif(controller == 2):
        insert = input("\n-> ")
        cursor.execute(insert)
        connection.commit()
    #Elif para caso a pessoa digite um termo inválido
    elif(controller != 1 and controller != 2 and controller != 9):
        print("Comando inválido!")
    #Else para exibir mensagem de programa finalizado
    else:
        print("Programa finalizado.")
        
cursor.close()
connection.close()