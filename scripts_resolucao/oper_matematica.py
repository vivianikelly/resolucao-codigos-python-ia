# Solicita os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Escolha uma operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == '+':
    resultado = abs(numero1 + numero2)
elif operacao == '-':
    resultado = abs(numero1 - numero2)
elif operacao == '*':
    resultado = abs(numero1 * numero2)
elif operacao == '/':
    # Verifica se o divisor não é zero
    if numero2 != 0:
        resultado = abs(numero1 / numero2)
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)