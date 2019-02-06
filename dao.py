class Dados:
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

    def buscar(self, numero):
        self.cursor.execute(f'SELECT * FROM dados where numero_contato={numero}')
        return self.cursor.fetchone()

    def registrar(self, numero, nome, rua, lote, quadra, referencia):
        self.cursor.execute(f"INSERT INTO dados(numero_contato, nome, rua, lote, quadra, referencia) values('{numero}', '{nome}', '{rua}', '{lote}', '{quadra}', '{referencia}')")
        self.db.commit()
        return True
    
    def alterar(self,numero_contato,nome,rua,lote,quadra,referencia):
        self.cursor.execute(f"UPDATE dados SET nome='{nome}', rua='{rua}', lote='{lote}', quadra='{quadra}', referencia='{referencia}' WHERE numero_contato='{numero_contato}'")
        self.db.commit()
        return True

    def todos_clientes(self):
        self.cursor.execute(f"SELECT * FROM dados ORDER BY nome")
        dados = self.cursor.fetchall()
        return dados
    
    def remover(self, numero):
        self.cursor.execute(f"delete from dados where numero_contato='{numero}'")
        self.db.commit()
        return True
    
    def contar(self):
        self.cursor.execute(f"SELECT COUNT(*) FROM dados")
        tot = str(self.cursor.fetchone())
        tot = tot.replace('(','').replace(',','').replace(')','')
        return tot 