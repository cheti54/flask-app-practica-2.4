from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola desde la nube! 🌤️"

@app.route("/info")
def info():
    return "<h1>App Flask Desplegada en Render</h1><p>Esta es una aplicación de prueba para la práctica 2.4</p>"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"<h2>¡Hola {nombre}!</h2><p>Bienvenido a nuestra app en la nube</p>"

if __name__ == "__main__":
    app.run(debug=True)