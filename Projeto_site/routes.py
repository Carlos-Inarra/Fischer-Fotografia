from flask import render_template,url_for,request,redirect,make_response,session
from Projeto_site import app
from functools import wraps


def Logado(funcao_original):
    @wraps(funcao_original)
    def wrapper(*args, **kwargs):
        try:
            a = session["usuario"]
        except:
            a = ""
        if a:
            resultado = funcao_original(*args, **kwargs)
        else:
            return redirect(url_for("login"))
        return resultado
    return wrapper

@app.route('/login', methods=['GET'])
def login():
    resp = make_response("Sucess")
    resp.set_cookie('Usuario', 'Carlos Inarra')
    return render_template("Cadastro.html")


@app.route('/',methods=['GET'])
# @Logado
def Home():       
    return render_template("Base.html")


@app.route('/Admin',methods=['POST','GET'])
# @Logado
def Admin(): 
    alteracao = []
    a = ""  
    if request.method == "GET":
        return render_template("Admin.html", a=a)   
    elif request.method == "POST":
        for i in range(1, 5):
            if request.files[f"Carrossel{i}"].filename != "":
                request.files[f"Carrossel{i}"].save(rf"C:\Users\CarlosInarra\Documents\Sites-modelos\Projeto_site\static\Imagens\img{i}.jpg")
                alteracao.append(1)
            else:
                pass    
        a = "Alterações Feitas" if len(alteracao) >= 1 else ""  
        return render_template("Admin.html",a =a)
    
@app.route('/Mapatestando',methods=['GET'])
def MapaTestando():
    return render_template('index.html' )
