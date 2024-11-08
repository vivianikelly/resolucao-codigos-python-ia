# Recebe a string do usuário
texto = input("Digite uma string: ")

# Recebe o número inteiro do usuário e converte para int
numero = int(input("Digite um número inteiro: "))

# Repete a string o número de vezes informado
#resultado = texto * numero
resultado = " ".join([texto] * numero)

# Exibe o resultado
print("Resultado da repetição:", resultado)