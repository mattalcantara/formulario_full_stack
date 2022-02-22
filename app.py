from flask import Flask, jsonify, request, abort, redirect, url_for, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro'

#Inicializar BD
db = SQLAlchemy(app)

#Criar Model
class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200))
    senha = db.Column(db.String(200), nullable=False)

@app.route('/form', methods=['POST','GET'])
def form():
    title = 'Formulário de Cadastro'
    if request.method == "POST":
        usuario_form = request.form['usuario']
        email_form = request.form['email']
        senha_form = request.form['senha']
        print(usuario_form, email_form)
        post_usuario = Cadastro(usuario=usuario_form)
        post_email = Cadastro(email=email_form)
        post_senha = Cadastro(senha=senha_form)
        try:
            db.session.add(post_usuario)
            db.session.add(post_email)
            db.session.add(post_senha)
            db.session.commit()
        except:
            return "Erro ao adicionar"
    else:
        return render_template("form.html", title = title)

@app.route('/home')
def home():
    return render_template("home.html")

