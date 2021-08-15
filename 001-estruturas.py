#  estruturas do tipo sequência

# Sequência mutável e ordenada de elementos
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

