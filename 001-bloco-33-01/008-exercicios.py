# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.


def maior_numero(num_1, num_2):
    if num_1 > num_2:
        return num_1
    elif num_2 > num_1:
        return num_2


print(maior_numero(15, 8))

# Calcule a média aritmética dos valores contidos em uma lista.


def media(lista):
    media_lista = sum(lista) / len(lista)
    return media_lista


print(media([1, 8, 6, 9]))


# Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n.


def imprime_quadrados(numero):
    ast = "*"
    line = ""

    for _num in range(numero):
        line += ast

    for _num in range(numero):
        print(line)


print(imprime_quadrados(5))

#  Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres.
#  Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda".

print("################################################")


def maior_nome(nomes):
    return max(nomes, key=len)


print(maior_nome(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))


# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta 
# é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores
#  em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir 
# do tamanho de uma parede(em m²).