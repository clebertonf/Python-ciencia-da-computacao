# definição de funçoes

# parametros posicionais
def soma(a, b):
    return a + b


print(soma(10, 50))

# parametros nomeados

print(soma(b=40, a=120))

# Os parâmetros também podem ser variádicos. Ou seja, podem variar em sua quantidade.
# Parâmetros posicionais variádicos são acessados como tuplas no interior de uma função
# e parâmetros nomeados variádicos como dicionário.


def concat(*strings):
    # Equivalente a um ", ".join(strings), que concatena os elementos de um iterável em uma
    # string utilizando um separador
    # Nesse caso a string resultante estaria separada por vírgula
    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ", "
    return final_string


# pode ser chamado com 2 parâmetros
print(concat("Carlos", "João"))  # saída: "Carlos, João"

# pode ser chamado com um número n de parâmetros
concat("Carlos", "João", "Maria")  # saída: "Carlos, João, Maria"

# dict é uma função que já vem embutida no python
dict(
    nome="Felipe", sobrenome="Silva", idade=25
)  # cria um dicionário utilizando as chaves passadas

dict(
    nome="Ana", sobrenome="Souza", idade=21, turma=1
)  # o número de parâmetros passados para a função pode variar

print("Botaro", "Cássio", sep=", ")


def leet(word):
    word = list(word.upper())
    char_map = dict(zip('AEIO', '4310'))
    print(char_map)

    results = []

    for letter in word:
        if letter in char_map:
            results.append(char_map[letter])
        else:
            results.append(letter)

    return results


print(leet('cleber'))
