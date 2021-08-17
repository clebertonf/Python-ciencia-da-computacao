import random
import sys


# entrada de dados

number = 0

while number < 60:
    number += int(input('Digite um numero'))

print('O a soma é maior que 62')


random_number = random.randint(1, 10)  # escolhe um número aleatório entre 1 e 10
guess = ""

while guess != random_number:  # enquanto não adivinhar o número
    guess = int(input("Qual o seu palpite? "))  # pergunte a pessoa usuária um número

print("O número sorteado era: ", guess)

# módulo sys

if __name__ == " __main__":
    for argument in sys.argv:
        print('Received:', argument)

# executando (python3 arquivo.py 2 4 "teste")


# Saida de dados Print

print("O resultado é", 42)  # saída: O resultado é 42
print("Os resultado são", 6, 23, 42)  # saída: Os resultados são 6 23 42

print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída: Maria, João, Miguel, Ana

# print na mesma lina
print("Na mesma ", end="")
print("linha.")

# Existe um parâmetro que nos permite modificar a saída padrão para a saída de erros:

import sys


err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)

#  Em Python , podemos fazer interpolação de variáveis e expressões utilizando f-string . 
# Adicionamos um f antes das aspas e o valor de saída entre chaves. Essa dica é importante,
#  pois é a maneira mais eficiente de formatar strings.

x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 2 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores, como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."
# . é o caractere utilizado para preencher
# ^ indica que o valor será centralizado
# 3 são o número de caracteres exibidos

# 