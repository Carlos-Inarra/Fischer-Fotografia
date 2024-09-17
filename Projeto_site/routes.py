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

def Enviar_mensagem(*args: str | None, MSG: str, Teclado: bool = False, ChatId: int = 5127620212):
    """Envia uma mensagem para a minha conta utilizando a API oficial do Telegram.
    Caso queira trocar para enviar para outra conta preencha o ChatId."""
    
    url = f'https://api.telegram.org/bot<YOUR_BOT_TOKEN>/SendMessage'
    
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
    
@app.route('/Mapatestando',methods=['GET'])
def MapaTestando():
    Enviar_mensagem("Opção 1", "Opção 2", MSG="Escolha uma opção:", Teclado=False)


    
    
