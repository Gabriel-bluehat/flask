## o APP.PY é o arquivo de configuração principal do projeto flask

from flask import Flask,render_template,request,url_for,redirect
import sqlite3


app = Flask(__name__)

## routes ou rotas que são caminhos da aplicação web

#a página principal de uma aplicação é também conhecido como raiz

#@app.route('/')
#def hello():
    #return "Olá estou executando a página inicial com Flask"

#renderizando a pagina inicial com um template html

## vamos criar a função de conexão com o banco de dados

def get_db_connection():
    conn = sqlite3.connect('basedados.db')
    conn.row_factory = sqlite3.Row
    return conn




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return "Estou executando a página clientes"


## Para o front se comunicar e interagir com o backend ele usa os métodos get e post
#GET ele busca informação do backend e trás para o frontend ou para a telas
# POST ele leva a informação inserida no front pelo usuário e leva para o backend

## Rotas para as outras urls do frontend

@app.route('/listaclientes',methods=('GET',"POST"))
def listaclientes():
    conn = get_db_connection()
    clientesback = conn.execute("select * from cadastro_clientes").fetchall()
    conn.close()
    return render_template('listaclientes.html',clientes=clientesback) #interliga o front com o back



@app.route('/addclientes',methods=('GET',"POST"))
def addclientes():
    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        cpf = request.form['cpf']
        conn= get_db_connection()
        conn.execute('insert into cadastro_clientes (nome,sobrenome,cpf) values(?,?,?)',(nome,sobrenome,cpf))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('addclientes.html')
