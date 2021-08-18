import json

with open('nome.json') as file:
    content = file.read()
    list_names = json.loads(content)['nomes']

new_list = filter(lambda name: name['idade'] < 20, list_names)


for names in new_list:
    print(names)

