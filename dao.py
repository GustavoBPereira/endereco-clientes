import sqlite3

class Dados:
    def __init__(self, db):
        self.db = db

    def buscar(self, numero):
        con = sqlite3.connect(self.db)
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM enderecos where numero_contato=?',(numero,))
        resultado = cursor.fetchone()
        con.close()
        return resultado

    def registrar(self, numero, nome, rua, lote, quadra, referencia):
        con = sqlite3.connect(self.db)
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO enderecos(numero_contato, nome, rua, lote, quadra, referencia) values('{numero}', '{nome}', '{rua}', '{lote}', '{quadra}', '{referencia}')")
        con.commit()
        con.close()
        return True
    
    def alterar(self,numero_contato,nome,rua,lote,quadra,referencia):
        con = sqlite3.connect(self.db)
        cursor = con.cursor()
        cursor.execute(f"UPDATE enderecos SET nome='{nome}', rua='{rua}', lote='{lote}', quadra='{quadra}', referencia='{referencia}' WHERE numero_contato='{numero_contato}'")
        con.commit()
        con.close()
        return True

    def todos_clientes(self):
        con = sqlite3.connect(self.db)
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM enderecos ORDER BY nome")
        dados = cursor.fetchall()
        con.close()
        return dados


        dados = self.cursor.fetchall()
    
    def remover(self, numero):
        con = sqlite3.connect(self.db)
        cursor = con.cursor()
        cursor.execute(f"delete from enderecos where numero_contato=?",(numero,))
        con.commit()
        con.close()
        return True
    
    def contar(self):
        con = sqlite3.connect(self.db)
        cursor = con.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM enderecos")
        tot = str(cursor.fetchone())
        tot = tot.replace('(','').replace(',','').replace(')','')
        con.close()
        return tot 
