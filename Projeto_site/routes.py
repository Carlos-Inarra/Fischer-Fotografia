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
@Logado
def Home():       
    return render_template("Base.html")


@app.route('/Admin',methods=['POST','GET'])
@Logado
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
    import pandas as pd
    UF = [{'nome': 'Acre',
  'sigla': 'AC',
  'licenciados': [],
  'Long': -67.8249,
  'Lat': -9.9754},
 {'nome': 'Alagoas',
  'sigla': 'AL',
  'licenciados': [],
  'Long': -35.7196,
  'Lat': -9.6474},
 {'nome': 'Amapá',
  'sigla': 'AP',
  'licenciados': [],
  'Long': -51.0694,
  'Lat': 0.0349},
 {'nome': 'Amazonas',
  'sigla': 'AM',
  'licenciados': [],
  'Long': -60.0217,
  'Lat': -3.119},
 {'nome': 'Bahia',
  'sigla': 'BA',
  'licenciados': ['Império das Passagens',
   'Interact Group',
   'SB Travel',
   'VCA Viagens (App Viagens)'],
  'Long': -38.5014,
  'Lat': -12.9714},
 {'nome': 'Ceará',
  'sigla': 'CE',
  'licenciados': [],
  'Long': -38.5431,
  'Lat': -3.7172},
 {'nome': 'Brasília',
  'sigla': 'DF',
  'licenciados': ['AGM', 'RM Turismo (P&P)', 'SLC'],
  'Long': -47.9218,
  'Lat': -15.8267},
 {'nome': 'Espírito Santo',
  'sigla': 'ES',
  'licenciados': ['CHR (Flytte)'],
  'Long': -40.3128,
  'Lat': -20.3155},
 {'nome': 'Goiás',
  'sigla': 'GO',
  'licenciados': ['Universal Goiania (Uniglobe)'],
  'Long': -49.2643,
  'Lat': -16.6864},
 {'nome': 'Maranhão',
  'sigla': 'MA',
  'licenciados': [],
  'Long': -44.2826,
  'Lat': -2.5387},
 {'nome': 'Mato Grosso',
  'sigla': 'MT',
  'licenciados': [],
  'Long': -56.0949,
  'Lat': -15.5989},
 {'nome': 'Mato Grosso do Sul',
  'sigla': 'MS',
  'licenciados': [],
  'Long': -54.6466,
  'Lat': -20.4428},
 {'nome': 'Minas Gerais',
  'sigla': 'MG',
  'licenciados': ['PRS (Iinovi)', 'Trade'],
  'Long': -43.9333,
  'Lat': -19.9167},
 {'nome': 'Pará',
  'sigla': 'PA',
  'licenciados': [],
  'Long': -48.5044,
  'Lat': -1.4558},
 {'nome': 'Paraíba',
  'sigla': 'PB',
  'licenciados': [],
  'Long': -34.8631,
  'Lat': -7.115},
 {'nome': 'Paraná',
  'sigla': 'PR',
  'licenciados': ['Asia Tour', 'Travellog', 'Valentin Turismo'],
  'Long': -49.2719,
  'Lat': -25.4296},
 {'nome': 'Pernambuco',
  'sigla': 'PE',
  'licenciados': ['Casa Forte (Fortour)', 'Luck', 'Pontestur'],
  'Long': -34.877,
  'Lat': -8.0476},
 {'nome': 'Piauí',
  'sigla': 'PI',
  'licenciados': [],
  'Long': -42.8034,
  'Lat': -5.0919},
 {'nome': 'Rio de Janeiro',
  'sigla': 'RJ',
  'licenciados': ['CP Turismo',
   'Dynamo',
   'Fantasytour (Travel Place)',
   'Milessis',
   'Promotional',
   'Solid',
   'Tropical',
   'Vision Travel',
   'Wings'],
  'Long': -43.1729,
  'Lat': -22.9068},
 {'nome': 'Rio Grande do Norte',
  'sigla': 'RN',
  'licenciados': [],
  'Long': -35.211,
  'Lat': -5.7945},
 {'nome': 'Rio Grande do Sul',
  'sigla': 'RS',
  'licenciados': ['CH Turismo', 'Mercatur'],
  'Long': -51.2287,
  'Lat': -30.0277},
 {'nome': 'Rondônia',
  'sigla': 'RO',
  'licenciados': ['Cosmos'],
  'Long': -63.8999,
  'Lat': -8.7608},
 {'nome': 'Roraima',
  'sigla': 'RR',
  'licenciados': [],
  'Long': -60.6733,
  'Lat': 2.8198},
 {'nome': 'Santa Catarina',
  'sigla': 'SC',
  'licenciados': ['Cosmos', 'Global (T.W.S)', 'Go Inti'],
  'Long': -48.548,
  'Lat': -27.5954},
 {'nome': 'São Paulo',
  'sigla': 'SP',
  'licenciados': ['Addetur',
   'Alive',
   'Capolavoro',
   'Conextravel',
   'Copastur',
   'DIX',
   'Jet Stream',
   'LB Gate (Gate Tour)',
   'Maiorca',
   'NIX',
   'RB Viagens (Bird)',
   'Satguru',
   'SolFesta',
   'TC Operadora (The Cliente Operadora e Agência de Viagens LTDA)',
   'Tivoli',
   'Transoceanic (Sobratur)',
   'Trip Soul (R. C. dos Santos Pereira Ltda)',
   'Tristar',
   'Ypy Viagens (Postserv)'],
  'Long': -46.6333,
  'Lat': -23.5505},
 {'nome': 'Sergipe',
  'sigla': 'SE',
  'licenciados': [],
  'Long': -37.0731,
  'Lat': -10.9472},
 {'nome': 'Tocantins',
  'sigla': 'TO',
  'licenciados': [],
  'Long': -48.3603,
  'Lat': -10.2128}]
    tabela = pd.DataFrame(UF)
    tabela["Quant"] = tabela["licenciados"].apply(lambda x: len(x))

    import plotly.express as px
    df = tabela
    fig = px.scatter_geo(df,lon=df["Long"],lat=df["Lat"],color="sigla"
                    , size="Quant",hover_name="nome",
                     projection="natural earth",scope="south america")
    graph_html = fig.to_html(full_html=False)
    
    # Renderize o template passando o HTML do gráfico
    return render_template('index.html', graph_html=graph_html)
