def sum_numbers():
    numbers = []

    continues = True

    while continues == True:
        numbers.append(int(input('Digite um numero: ')))
        resp = input('Deseja digitar outro? s/n: ')
        if resp == 's':
            continues = True
        else:
            continues = False

    print('A soma dos numeros é: ', sum(numbers))


sum_numbers()