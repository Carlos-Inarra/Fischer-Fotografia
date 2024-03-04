from flask import render_template,url_for,request,redirect
from Projeto_site import app

@app.route('/',methods=['GET'])
def Home():       
    return render_template("Base.html")
