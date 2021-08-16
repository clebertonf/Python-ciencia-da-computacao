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


# Print


