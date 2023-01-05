""" Archivo de configuración de la aplicación """
from flask import Flask
from flask import request, redirect, Response
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

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    size = request.form.get("size")
    mensaje = "Disponible"
    if size == "S":
        mensaje = "No disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
