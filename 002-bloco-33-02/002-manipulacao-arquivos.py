from os import write


file = open('meu_arquivo.txt', mode='w') #  mode="w" , ou seja, estamos abrindo o arquivo para escrita

file.write('Cleberton\n')
file.write('Katrine\n')
file.write('Francisco\n')

print(file=file)  # Print tambem pode ser usado pa ler arquivos, passando parametro.


# passadno uma lista para ser escrita no arquivo

file_list = open('minha_lista.txt', mode='w')

list = ['Segunda\n', 'Terça\n', 'Quarta\n', 'Quinta\n', 'Sexta\n']

file_list.writelines(list)

file.close()  # sempre fechar o arquivo apos a manipulação
file_list.close()

# A leitura do conteúdo de um arquivo pode ser feita utilizando a função read.
#  Para experimentar, vamos escrever em um arquivo e lê-lo logo em seguida!

# Escrita

file_3 = open('meu_arquivo_03.txt', mode='w')
file_3.write('Ola mundo!')
file_3.close()

# Leitura

file_3 = open('meu_arquivo_03.txt', mode='r')
content = file_3.read()
print(content)
file_3.close()

# Um arquivo é também um iterável, ou seja, pode ser percorrido em um laço de repetição. A cada iteração, uma nova linha é retornada.

# Escrita
file_4 = open('meu_arquivo_04.txt', mode='w')
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file_4.writelines(LINES)
file_4.close()

# Leitura
file_4 = open('meu_arquivo_04.txt', mode='r')

for line in file_4:
    print(line)
file_4.close()


# Além de arquivos textuais como os que manipulamos até agora, temos também arquivos binários.
#  Eles são arquivos que contêm uma série de bytes e a sua leitura pode variar de acordo com o arquivo.
#  Nesse caso, devemos acrescentar um b ao parâmetro mode , indicando que será utilizado o modo binário.

# escrita
file = open("arquivo.dat", mode="wb")
file.write(b"C\xc3\xa1ssio 30")  # o prefixo b em uma string indica que seu valor está codificado em bytes
file.close()

# leitura
file = open("arquivo.dat", mode="rb")
content = file.read()
print(content)  # saída: b'C\xc3\xa1ssio 30'
file.close()  # não podemos esquecer de fechar o arquivo