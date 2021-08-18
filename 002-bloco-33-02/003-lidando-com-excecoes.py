# https://docs.python.org/pt-br/3/library/exceptions.html#bltin-exceptions
# referencia para exceções já embutidas na linguagem Python


# Observe que, apenas no exemplo abaixo, podemos observar três exceções:
# ZeroDivisionError , NameError e TypeError

"""
print(10 * (1 / 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
print(4 + spam * 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
print('2' + 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
"""

# Para tratarmos exceções, utilizamos o conjunto de instruções try , com as palavras reservadas try e except
# Vamos agora ver um exemplo de tratamento de exceções:

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# Lidando com exceções enquanto manipulamos arquivos

"""
    Sempre devemos fechar um arquivo e podemos, em um bloco try , fazer isso utilizando a instrução 
    finally ou else . O finally é uma outra cláusula do conjunto try , cuja finalidade é permitir a 
    implementação de ações de limpeza, que sempre devem ser executadas independentemente da ocorrência 
    de ações. Já o else ocorre sempre que todo o try for bem sucedido.
"""

try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")

"""
O with é a palavra reservada para gerenciamento de contexto. Este gerenciamento ( with ) 
é utilizado para encapsular a utilização de um recurso, garantindo que certas ações sejam 
tomadas independentemente se ocorreu ou não um erro naquele contexto.
A função open retorna um objeto que se comporta como um gerenciador de contexto de arquivo que 
será responsável por abrir e fechar o mesmo. Isto significa que o arquivo possui mecanismos 
especiais que, quando invocados, utilizando with , alocam um determinado recurso, no caso um 
arquivo, e, quando o bloco for terminado, este recurso será liberado.

"""

# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    file.write("Michelle 27\n")
# como estamos fora do contexto, o arquivo foi fechado
print(file.closed)


# Já vimos a utilização de gerenciadores de contexto em testes. Lá, capturamos exceções que ocorrem
# e verificamos se naquele contexto a exceção lançada era a esperada. Não há um recurso a ser liberado,
# mas estamos garantindo que uma asserção será feita naquele contexto.

# Exercicios
# Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que lê todas
# essas informações e filtre mantendo somente as pessoas que estão reprovadas, e escreva seus
# nomes em outro arquivo. A nota miníma para aprovação é 6.


def filter_aprove():
    try:
        file = open("alunos.txt", mode='r')
        notas = []
        final_notas = []
        for line in file:
            notas.append(line.split())
        for nota in notas:
            if int(nota[1]) < 6:
                final_notas.extend(nota)

                file_list = open('alunos_reprovados.txt', mode='w')
                file_list.writelines(final_notas)
                file_list.close()
    except OSError:
        print("Erro, arquivo não existe")
    else:
        print("arquivo manipulado e fechado com sucesso")
        file.close()


filter_aprove()

# função incompelta falta manipular string