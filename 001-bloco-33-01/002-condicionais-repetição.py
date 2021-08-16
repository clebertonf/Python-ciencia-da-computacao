# ====== if and else ====== 

# exemplos simples
salary = 1500

if salary  <= 2000:
    print('Estagiario')
elif 2000 < salary <= 3000:
    print('Junior')

position = ""
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"

# Em alguns casos, que não prejudiquem a legibilidade, podemos criar estruturas de mapeamento 
# ( dicts ) para simplificar o aninhamento de condicionais.

key = "id"
from_to = {
    "id": "identifier",
    "mail": "email",
    "lastName": "last_name",
}
from_to[key]


# ==== Estruturas de repetição ====== 

# for 

restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rate = 3.0

# laço for
for restaurant in restaurants:
    if restaurant['nota'] > min_rate:
        filtered_restaurants.append(restaurant)

print(filtered_restaurants)

for index in range(5):
    print(index)

# compreensão de listas (como se fosse o filter no javaScript)

min_rating = 3.0
filtered_restaurants = [restaurant
                         for restaurant in restaurants
                         if restaurant["nota"] > min_rating]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# A compreensão de listas é declarada da mesma maneira que uma lista comum, 
# porém no lugar dos elementos nós colocamos a iteração que irá gerar os elementos da nova lista. 
# Um detalhe importante é que é possível filtrar esses elementos utilizando o if

# Poderíamos listar também somente o nome dos restaurantes.

# min_rating = 3.0
filtered_restaurants = [restaurant["name"]  # aqui pedimos somente o nome do restaurante
                       for restaurant in restaurants
                       if restaurant["nota"] > min_rating]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

print("###############################################################")

filter = [restaurant 
          for restaurant in restaurants
          if restaurant["name"] == 'Restaurante A']
print(filter)

# while

# A Sequência de Fibonacci

n = 10
last, next = 0, 1 # atribuição multipla
while last < n:
    print(last)
    last, next = next, last + next

# Calculo fatorial

numero = 5
resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count +=1

print(resultado)

# mudar sequencia de ratings de ratings = [6, 8, 5, 9, 10] para ratings = [6, 8, 5, 9, 10]

ratings = [6, 8, 5, 9, 10]
new_ratings = []

for rate in ratings:
    new_ratings.append(rate * 10)

print(new_ratings)

# Imprimir multiplos de 3 (divisiveis por 3)

values = [60, 80, 50, 90, 100]
values_mult = []

for number in values:
    if number % 2 == 0:
        values_mult.append(number)

print(values_mult)

