""" Archivo de configuración de la aplicación """
from flask import Flask
from flask import request, redirect
import persistencia

app = Flask(__name__)

@app.route("/pizza", methods=["POST"])
def pizza():
    """ Método pizza """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print(nombre + " " + apellidos)
    persistencia.guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/M1-U1%20Marta%20Pelufo/solicita_pedido.html", code=302)
