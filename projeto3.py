def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 == 0:
            return "Erro: divisão por zero"
        resultado = num1 / num2
    else:
        return "Operação inválida"
    
    return resultado

# Exemplos de uso:
resultado = calculadora(5, 3, 1)  # Soma
print("Resultado da soma:", resultado)

resultado = calculadora(5, 3, 2)  # Subtração
print("Resultado da subtração:", resultado)

resultado = calculadora(5, 3, 3)  # Multiplicação
print("Resultado da multiplicação:", resultado)

resultado = calculadora(5, 0, 4)  # Divisão por zero (erro)
print(resultado)

resultado = calculadora(5, 3, 5)  # Operação inválida
print(resultado)
