from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
from dao import Dados


#CONFIGURAÇÃO DA CONEXÃO COM O MYSQL
con = mysql.connector.connect(
        user='gustavo',
        password='',
        database='clientes')
db  = Dados(con)
#CLASSE DADOS RESPONSÁVEL PELOS CÓDIGOS SQL


app = Flask(__name__)

#ROTA INICIAL DA APP
@app.route('/')
def index():
	#AO ACESSAR ESTA ROTA A UNICA COISA QUE VAI ROLAR É A RENDERIZAÇÃO DO TEMPLATE INDEX
    return render_template('index.html')

@app.route('/buscar', methods=['GET',])
def buscar():
	#QUANDO O USUARIO DA O SUBMITE NO FORM DO INDEX, ELE É LANÇADO PARA ESTA ROTA
	#VARIAVEL ABAIXO É O CONTEUDO DIGITADO NO INDEX
	numero = str(request.args.get('numero'))
	if(numero == ''):
		#SE NÃO DIGITOU NADA VOLTA PARA O INDEX
		return render_template('index.html')
	
	#VARIAVEL ABAIXO É BOOLEANA
	encontrado = db.buscar(numero)
	if(encontrado):
		#SE TRUE VAI PARA O TEMPLATE ENCONTRADO, PARA SER FORNECIDOS OS DADOS
		return render_template('encontrado.html', dados=encontrado)
	else:
		#SE NÃO FOR ENCONTRADO MANDA PARA O FORM DE CRIAÇÃO DE UM NOVO CADASTRO
		#NESTE RENDER_TEMPLATE É PASSADO UMA VAR NUMERO, QUE LÁ NO ARQUIVO HTML EU POSSO ACESSA-LA
		#FIZ ISSO COM O OBJETIVO DE JÁ DEIXAR PREENCIDO O CAMPO DE NUMERO PARA CONTATO
		#PQ COMO ELE É O ID UNICO E O CLIENTE JÁ INFORMOU, NÃO TERIA NECESSIDADE DE PREENCHE-LO NOVAMENTE
		return render_template('cadastro.html', numero=numero)


@app.route('/registrar', methods=['POST','GET',])
def registrar():
	#O SISTEMA CHEGA AQUI QUANDO ROLA O SUBMIT NO FORM DO TEMPLATE CADASTRO
	#NA ROTA ACIMA QUANDO É INSERIDO UM NUMERO E ELE NÃO CONSTA COMO REGISTRADO
	numero     = str(request.form['contato'])
	nome       = str(request.form['nome'])
	rua        = str(request.form['rua'])
	lote       = str(request.form['lote'])
	quadra     = str(request.form['quadra'])
	referencia = str(request.form['referencia'])
	#VALORES DO FORM
	db.registrar(numero, nome, rua, lote, quadra, referencia)
	#REGISTRO DO CLIENTE
	dados = db.buscar(numero)
	#AQUI PEGA OS DADOS DESSE MESMO CLIENTE PARA MANDAR PARA O TEMPLATE DE ENCONTRADO
	#LÁ TEM CAMPOS DE EDIÇÃO E DELETE
	return render_template('encontrado.html', dados=dados)

@app.route('/edicao/<numero>')
def edicao(numero):
	#CAMPO DE EDIÇÃO
	#A SINTAXE DA ROTA É UM POUCO DIFERENTE, COM <> ISSO EM FLASK É PARA PASSAR UMA VARIÁVEL DENTRO DA URL
	dados  = db.buscar(str(numero))
	return render_template('alterar.html', dados=dados)

@app.route('/alterar', methods=['POST',])
def alterar():
	#AQUI SE CHEGA ATRAVES DO SUBMIT DO FORM DA ROTA EDICAO ACIMA
	numero     = str(request.form['gambiarra'])
	nome       = str(request.form['nome'])
	rua        = str(request.form['rua'])
	lote       = str(request.form['lote'])
	quadra     = str(request.form['quadra'])
	referencia = str(request.form['referencia'])
	db.alterar(numero,nome,rua,lote,quadra,referencia)
	dados = db.buscar(numero)
	return render_template('encontrado.html', dados=dados)

@app.route('/clientes')
def clientes():
	#LISTAGEM DE TODOS OS CLIENTES E O TOTAL DE CLIENTES
	dados =	db.todos_clientes()
	tot   = db.contar()
	return render_template('clientes.html', dados=dados, total=tot)

@app.route('/remover/<numero>')
def remover(numero):
	#AQUI SE CHEGA QUANDO VOCÊ ENCONTRA UM CLIENTES
	#E NAQUELE TEMPLATE VAI TER UM BUTTON REMOVER QUE MANDA PARA CA
	#A VAR NUMERO É O IDENTIFICADOR DESTE REGISTRO
	db.remover(numero)
	return render_template('index.html')

