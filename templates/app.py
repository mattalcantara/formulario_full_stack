import os
from flask import Flask, render_template, json, request, jsonify
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '0221'
app.config['MYSQL_DATABASE_DB'] = 'cadastro'
app.config['MYSQL_DATABASE_HOST'] = 'localhost' #172.17.0.1
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)

@app.route('/form', methods=['POST','GET'])
def form():
    title = 'Formulário de Cadastro'
    if request.method == "POST":
        usuario_form = request.form['usuario']
        email_form = request.form['email']
        senha_form = request.form['senha']
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            query = ("INSERT INTO cadastros (usuario, email, senha)" "VALUES (%s,%s,%s)")
            val = (usuario_form, email_form, senha_form)
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
    print(registros[0]);
    for x in range(len(registros)):
        print(registros[x])
    return render_template("home.html", registros=registros)

@app.route('/capa', methods=['POST', 'GET'])
def capa():
    title = "Seja bem vindo a Capa!"
    return render_template("capa.html", title = title)

@app.route('/sucesso', methods=['POST', 'GET'])
def sucesso():
    return render_template("sucesso.html")

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)
