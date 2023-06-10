from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/executar", methods=["POST"])
def executar():
    codigo = request.form.get("codigo")
    exec(codigo)
    return "Código executado com sucesso!"

if __name__ == "__main__":
    app.run()