from flask import Flask, render_template, abort,request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def inicio():
    return render_template("login.html")

@app.route('/validar', methods=["get","post"])
def validar():
    usuarioDB="cuadrado"
    claveDB="goleador"
    if request.method=="POST":
      usuario=request.form.get("usuario")
      clave=request.form.get("clave")
      if usuario==usuarioDB and clave==claveDB:
          return render_template("inicio2.html")

      else: 
          mensaje="Usuario o clave incorrecto"
          return render_template("login.html",mensaje=mensaje)


    #return "El usuario es: {} y la clave es: {}".format(usuario,clave)

app.run(host='0.0.0.0', port=5000, debug=True)