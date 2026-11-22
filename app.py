from flask import Flask, jsonify, render_template, request
from operacoes import calcular

app = Flask(__name__)

PAGINAS = {"soma": "Soma", "subtracao": "Subtração", "multiplicacao": "Multiplicação", "divisao": "Divisão"}


@app.get("/")
def inicio():
    return render_template("index.html")


@app.get("/<operacao>")
def pagina_operacao(operacao):
    if operacao not in PAGINAS:
        return "Página não encontrada", 404
    return render_template("operacao.html", operacao=operacao, titulo=PAGINAS[operacao])


@app.post("/calcular/<operacao>")
def calcular_operacao(operacao):
    if operacao not in PAGINAS:
        return jsonify(erro="Operação inválida."), 404
    dados = request.get_json(silent=True) or {}
    try:
        numero1 = float(str(dados["numero1"]).replace(",", "."))
        numero2 = float(str(dados["numero2"]).replace(",", "."))
        resultado = calcular(operacao, numero1, numero2)
        return jsonify(resultado=resultado)
    except (KeyError, ValueError, TypeError, OverflowError) as erro:
        return jsonify(erro=str(erro) if isinstance(erro, ValueError) else "Informe dois números válidos."), 400


if __name__ == "__main__":
    app.run(debug=True)
