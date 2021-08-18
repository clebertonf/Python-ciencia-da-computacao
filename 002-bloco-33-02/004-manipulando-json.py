import json


with open('pokemons.json') as file:
    content = file.read()  # leitura do arquivo
    pokemons = json.loads(content)['results']  # o conteúdo é transformado em estrutura python equivalente, dicionário neste caso.
    # acessamos a chave results que é onde contém nossa lista de pokemons


print(pokemons[0]) # imprime o primeiro pokemon da lista


# A leitura pode ser feita diretamente do arquivo, utilizando o método load ao invés de loads.
#  O loads carrega o JSON a partir de um texto e o load carrega o JSON a partir de um arquivo.
# load ja ler o arquivo e retorna

with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

print(pokemons[0])  # imprime o primeiro pokemon da lista

# Escrita de dados
# A escrita de arquivos no formato JSON é similar a escrita 
# de arquivos comum, porém primeiro temos de transformar os dados.


# Lendo
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Filtarndo
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# Escrevendo
# Abre o arquivo para escrevermos apenas o pokemons do tipo grama

with open("pokemons_file.json", "w") as file:
    json_poke = json.dumps(grass_type_pokemons)  # conversão de Python para o formato json (str)
    file.write(json_poke)


#  Assim como a desserialização, que faz a transformação de texto em formato JSON para Python , 
# a serialização, que é o caminho inverso, também possui um método equivalente para escrever em 
# arquivos de forma direta.

# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)