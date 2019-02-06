from flask import Flask, render_template, url_for, request, redirect
import mysql.connector
from dao import Dados

con = mysql.connector.connect(
        user='gustavo',
        password='',
        database='clientes')
db  = Dados(con)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET',])
def buscar():
	numero = str(request.args.get('numero'))
	if(numero == ''):
		return render_template('index.html')
	encontrado = db.buscar(numero)
	if(encontrado):
		return render_template('encontrado.html', dados=encontrado)
	else:
		return render_template('cadastro.html', numero=numero)

@app.route('/registrar', methods=['POST','GET',])
def registrar():
	numero     = str(request.form['contato'])
	nome       = str(request.form['nome'])
	rua        = str(request.form['rua'])
	lote       = str(request.form['lote'])
	quadra     = str(request.form['quadra'])
	referencia = str(request.form['referencia'])
	db.registrar(numero, nome, rua, lote, quadra, referencia)
	dados = db.buscar(numero)
	return render_template('encontrado.html', dados=dados)

@app.route('/edicao/<numero>')
def edicao(numero):
	dados  = db.buscar(str(numero))
	return render_template('alterar.html', dados=dados)

@app.route('/alterar', methods=['POST',])
def alterar():
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
	dados =	db.todos_clientes()
	tot   = db.contar()
	return render_template('clientes.html', dados=dados, total=tot)

@app.route('/remover/<numero>')
def remover(numero):
	db.remover(numero)
	return render_template('index.html')

