import random

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