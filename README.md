# Resolução Códigos em Python utilizando IA - Github Copilot

Como não tenho acesso ao Github Copilot, será utilizado [chatgpt](https://chatgpt.com/) para auxiliar na resolução dos códigos propostos.

1 - Concatenando Dados 🎲
---
**Descrição:** Vamos receber dois dados diferentes do usuário e concatena-los em uma única string.

**Nome função:** *concat_dados.py*

**Explicação resolução:**

- Recebendo as entradas: será utilizado comando input(), o qual é usado para capturar as entradas do usuário.

- Concatenando: As duas entradas são concatenadas com um espaço entre elas (+ " " +). Existe uma alternativa usando f-string.

- Exibindo o resultado: A string concatenada é exibida com print().

2 - Repetindo Textos 📝
---
**Descrição:** Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

**Nome função:** *repete_texto.py*

**Explicação resolução:**

- Recebendo a string e o número:
    - Variável *texto* armazena a string fornecida pelo usuário.
    - Variável *numero* armazena o número inteiro digitado, e int() é usado para garantir que seja convertido para o tipo correto.

- Repetindo a string: O operador * multiplica a string pelo número, o que faz com que ela seja repetida a quantidade de vezes indicada.

- Exibindo o resultado: O print() exibe a string repetida.

3 - Operações Matemáticas Simples ➕ ➖ ✖️ ➗
---

**Descrição:**  Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

**Nome função:** *oper_matematica.py*

**Explicação resolução:**

- Solicitando as Entradas:

    - As variáveis numero1 e numero2 são lidas como int.
    - A variável operacao armazena a operação desejada como string (+, -, * ou /).

- Estrutura Condicional para a Operação: 
    - Dependendo do operador digitado pelo usuário, o programa realiza a operação correspondente.
    - No caso de divisão, verifica-se se o divisor (numero2) é zero para evitar erro de divisão por zero.
    - O abs() é aplicado ao resultado de cada operação. Isso garante que o valor seja sempre positivo, independentemente do sinal do cálculo inicial.

- Exibindo o Resultado: O print() exibe o resultado da operação ou uma mensagem de erro se o usuário inseriu um operador inválido ou tentou dividir por zero.

4 - Verificando Números Pares e Ímpares 🧮
---

**Descrição:** Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

**Nome função:** *par_impar.py*

**Explicação resolução:**

- Entrada do Usuário: input() lê a entrada e int() converte para um número inteiro.

- Estrutura Condicional:

    - A condicional if verifica o valor de numero % 2.
    - Se o resultado for 0, significa que numero é par.
    - Se o resultado não for 0, ele cai no else e é considerado ímpar.

- Exibindo o Resultado: O print() usa uma f-string para exibir o número e indicar se ele é par ou ímpar.

5 - Calculando Média de Notas 📚
---

**Descrição:** Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

**Nome função:** *media_notas.py*

**Explicação resolução:**

- Entrada das Notas: As três notas são lidas como float, permitindo a entrada de números com casas decimais.

- Cálculo da Média: A média é calculada somando nota1, nota2, e nota3 e dividindo por 3.

- Exibindo o Resultado: print() com f-string exibe a média com duas casas decimais usando {media:.2f}, o que é comum para notas.

6 - Verificando Palíndromos 🔄
---

**Descrição:** Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

**Nome função:** *palindromo.py*

**Explicação resolução:**

- Entrada do Usuário:

    - input() captura a palavra e strip() remove espaços ao redor.
    - lower() converte a palavra para minúsculas, para que a comparação seja insensível a maiúsculas e minúsculas.

- Inversão da Palavra: palavra[::-1] inverte a palavra, usando o conceito de fatiamento de strings com [::-1].

- Comparação: O código verifica se a palavra é igual à sua versão invertida. Se sim, é um palíndromo; caso contrário, não é.




