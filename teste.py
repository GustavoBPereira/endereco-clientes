# import mysql.connector

# con = mysql.connector.connect(
#         user='gustavo',
#         password='',
#         database='pedidos')
# cursor = con.cursor()
# cursor.execute('SELECT * FROM clientes where numero_contato=145')
# print(cursor.fetchone())

INSERT INTO clientes (numero_contato,nome,rua,lote,quadra,referencia) VALUES ('993587250','Gustavo','85','14','454','Entre 35 e 34'),
('993107722','Angela','87','13','414','Entre 35 e 34'),
('400228922','Yudi','90','22','422','Entre 70 e 71');