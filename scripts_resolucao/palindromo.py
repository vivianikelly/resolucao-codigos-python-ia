# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ").strip().lower()

# Verifica se a palavra é igual à sua versão invertida
if palavra == palavra[::-1]:
    print(f"'{palavra}' é um palíndromo!")
else:
    print(f"'{palavra}' não é um palíndromo.")