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