# Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar usando uma condicional
if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")