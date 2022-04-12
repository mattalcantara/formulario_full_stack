import os
from flask import Flask, render_template, json, request, jsonify
from flaskext.mysql import MySQL
#from flask.ext.mysql import MySQL
#from flask_mysql import MySQL
#from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '0221'
app.config['MYSQL_DATABASE_DB'] = 'cadastro'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2' #172.17.0.1
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)

@app.route('/form', methods=['POST','GET'])
def form():
    title = 'Formulário de Cadastro'
    if request.method == "POST":
        nome_form = request.form['nome']
        email_form = request.form['email']
        endereco_form = request.form['endereco']
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            query = ("INSERT INTO cadastros (nome, email, endereco)" "VALUES (%s,%s,%s)")
            val = (nome_form, email_form, endereco_form)
            cursor.execute(query, val)
            conn.commit()
            return render_template("sucesso.html", code=200)
        except:
            return "Erro ao adicionar"
    else:
        return render_template("form.html", title = title)

@app.route('/home', methods=['POST', 'GET'])
def home():
    conn = mysql.connect()
    cursor = conn.cursor()
    print(cursor.execute("SELECT * FROM cadastros"))
    registros = cursor.fetchall()
    print(registros[0])
    for x in range(len(registros)):
        print(registros[x])
    return render_template("home.html", registros=registros)

@app.route('/', methods=['POST', 'GET'])
def capa():
    title = "Seja bem vindo a Capa!"
    return render_template("capa.html", title = title)

@app.route('/sucesso', methods=['POST', 'GET'])
def sucesso():
    return render_template("sucesso.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
