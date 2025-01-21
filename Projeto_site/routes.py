from flask import render_template,url_for,request,redirect,make_response,session
from Projeto_site import app
from functools import wraps
import requests

def Enviar_mensagem(*args: str | None,
                     MSG: str,
                     Teclado: bool = False,
                     ChatId: int = 5127620212,
                     Token: str = '7362106366:AAHf_K89aRbR0YlEshh194FSj468DB_qeHE') -> None:
    from requests import post

    url = f'https://api.telegram.org/bot{Token}/sendMessage'

    Teclado = {'keyboard': [[{'text': i}] for i in args],
               'is_persistent': True,
               'resize_keyboard': True} if Teclado else {'remove_keyboard': True}

    data = {
        'chat_id': ChatId,
        'text': MSG,
        'allow_sending_without_reply': True,
        'reply_markup': Teclado
    }

    try:
        post(url, json=data, timeout=30, verify=False)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")
        post(url, json=data, timeout=30, verify=False)


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

def Enviar_mensagem(*args: str | None, MSG: str, Teclado: bool = False, ChatId: int = 5127620212):
    """Envia uma mensagem para a minha conta utilizando a API oficial do Telegram.
    Caso queira trocar para enviar para outra conta preencha o ChatId."""
    
    url = f'https://api.telegram.org/bot7362106366:AAHf_K89aRbR0YlEshh194FSj468DB_qeHE/SendMessage'
    
    if Teclado:  # Se for utilizar o teclado padrão
        TextosTeclado = [[{'text': i}] for i in args]
        reply_markup = {
            'keyboard': TextosTeclado,
            'resize_keyboard': True,
            'is_persistent': True
        }
    else:  # Caso contrário, utilizar o teclado inline
        TextosInline = [[{'text': i, 'callback_data': i}] for i in args]
        reply_markup = {
            'inline_keyboard': TextosInline
        }
    
    data = {
        'chat_id': ChatId,
        'text': MSG,
        'allow_sending_without_reply': True,
        'reply_markup': reply_markup
    }
    
    try:
        a = requests.post(url, json=data, timeout=30)
        print(a.content)
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")
    
from flask import Flask, request

app = Flask(__name__)

@app.route('/EnviarMensagem', methods=['POST'])
def MapaTestando():
    # Obtém os dados da requisição
    data = request.json
    
    # Verifica se todos os campos necessários estão presentes
    if not data or 'MSG' not in data or 'Teclado' not in data:
        return {"error": "Campos obrigatórios ausentes. Inclua 'MSG' e 'Teclado'."}, 400
    
    # Extrai os dados da requisição
    mensagem = data.get('MSG', "Mensagem padrão")
    teclado = data.get('Teclado', False)
    opcoes = data.get('args', [])
    chat_id = data.get('ChatId', 5127620212)  # Valor padrão
    token = data.get('Token', '7362106366:AAHf_K89aRbR0YlEshh194FSj468DB_qeHE')  # Valor padrão

    # Chama a função para enviar a mensagem
    Enviar_mensagem(*opcoes, MSG=mensagem, Teclado=teclado, ChatId=chat_id, Token=token)
    return {"message": "Mensagem enviada com sucesso."}





    
    
