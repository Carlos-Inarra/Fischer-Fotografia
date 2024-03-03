from flask import render_template,url_for,request,redirect
from Projeto_site import app

@app.route('/',methods=['POST','GET'])
def Home():
    # Carrossel = []
    # for i in range(5):
    #     url_for()

        
    return render_template("Base.html")
