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

