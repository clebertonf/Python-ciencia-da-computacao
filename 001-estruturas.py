#  estruturas do tipo sequência

# ====== Sequência mutável e ordenada de elementos ======
names = ['Cleberton', 'tiago', 'Lucas', 'Fernanda']

# acessando valores
print(names[0])
print(names[-1])

# add valores
names.append('Maria')
print(names)

#remove valores
names.remove('Lucas')
print(names)

# add nova lista
names.extend(['Carlos', 'Basílio'])
print(names)

# retorna index
print(names.index('tiago'))

# ordena lista
names.sort()
print(names)

# ======  Tuplas (tuple) ======

# São similares a listas, porém não podem ser modificados durante a execução do programa

numbers = (1, 5, 3)
print(numbers)
print(numbers[2])

# ====== Conjuntos (set) ======

# Conjunto de elementos únicos e não ordenados. Como conjuntos, implementam operações de união, intersecção e outras.

permicoes = { 'user', 'admin'}

permicoes.add('custommer') # caso ja exista nada é adicionado

print(permicoes)

print(permicoes.union({'seller'})) # faz união dos conjuntos

print(permicoes.intersection({'user', 'admin'})) # # retorna um conjunto resultante da intersecção dos conjuntos

print(permicoes.difference({'admin'})) # retorna a diferença entre os dois conjuntos

# criando conjunto com set
nome = set({"Cleberton"})

print(nome)

# ====== Conjuntos imutáveis (frozenset) ======

# Variação do set, porém imutável, ou seja, seus elementos não podem ser modificados durante a execução do programa.

permissions = frozenset(["member", "group"])  # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

permissions.union({"user"})  # novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo não pode ser modificado

permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos


# ====== Dicionários (dict) ======

# Estrutura que associa uma chave a um determinado valor. É a representação do tão famoso objeto que utilizamos em JavaScript.

pessoas_pelo_id = {1: "Cleber", 2: "Lucas"}
pessoas_pelo_nome = {"Mario": 1, "Carlos": 2}

print(pessoas_pelo_id[1])
print(pessoas_pelo_nome["Mario"])

# elementos podem ser removidos com a palavra chave del
del pessoas_pelo_id[2]

print(pessoas_pelo_id.items()) # um conjunto é retornado com tuplas contendo chaves e valores

info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

print(info.keys()) # array com as keys

# add nova chave / valor
info["recorrente"] = "sim"

print(info)

info.pop("origem")

print(info)

# ====== Range (range) ======

