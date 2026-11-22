import math


def calcular(operacao, numero1, numero2):
    if not math.isfinite(numero1) or not math.isfinite(numero2):
        raise ValueError("Informe números finitos.")
    if operacao == "soma":
        resultado = numero1 + numero2
    elif operacao == "subtracao":
        resultado = numero1 - numero2
    elif operacao == "multiplicacao":
        resultado = numero1 * numero2
    elif operacao == "divisao":
        if numero2 == 0:
            raise ValueError("Não é possível dividir por zero.")
        resultado = numero1 / numero2
    else:
        raise ValueError("Operação inválida.")
    if not math.isfinite(resultado):
        raise ValueError("Resultado fora do intervalo permitido.")
    return resultado
