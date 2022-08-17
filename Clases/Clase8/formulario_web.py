
from flask import Flask,request


formulario_html = """ 
<!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"></head>
    <body>
        <form method="POST">
            Nombre:<br>
            <input type="text" name="name">
                <br>
                Email:<br>
                <input type="text" name="email">
                <br>
                Mensaje:<br>
                <textarea name="message"></textarea>
                <br><br>
                <input type="submit" value="Enviar">
         </form> 
    </body>
</html>
"""

enviado_html = """
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Enviado</title>
        <meta http-equiv="refresh" content="3";URL="http://localhost:8880/form">
    </head>
    <body>
        Mensaje enviado
    </body>
</html>
"""

vacios_error_html = """
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Vacios</title>
        <meta http-equiv="refresh" content="3";URL="http://localhost:8880/form">
    </head>
    <body>
        Campos Vacios, o hay un error
    </body>
</html>
"""



app = Flask(__name__)

@app.route("/")
def home():
    return 'Formulario en <a href="http://localhost:8880/form">localhost:8880/form</a>'


@app.route("/form",  methods=["GET","POST"])
def tomar_formulario():
    if request.method == "GET":
        return formulario_html.encode("utf-8")
    elif request.method == "POST":
        try:
            body = dict(request.form)
            if body["name"] and body["email"] and body["message"]:
                print("-"*20,"\n"*2)
                print("Nombre:",body["name"],"\nEmail:",body["email"],"\nMensaje:",body["message"])
                print("\n"*2,"-"*20)
                return enviado_html.encode("utf-8")
            else:
                return vacios_error_html.encode("utf-8")
        except Exception:
            return vacios_error_html.encode("utf-8")
    else:
        return vacios_error_html.encode("utf-8")


app.run("localhost",port=8880)
