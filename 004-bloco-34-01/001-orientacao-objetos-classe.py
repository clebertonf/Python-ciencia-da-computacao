# Classe / entidade


class User:
    def __init__(self, name, email, password):
        """Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

    # metodo de envio de email
    def reset_password(self):
        print("Envia email de reset de senha")


# instanciando a classe User

meu_user = User("Cleberton", "clebert@gmail.com", "123")

# acessando atributos

print(meu_user)  # <__main__.User object at 0x7fd15e68adc0>
print(meu_user.name)  # Cleberton
print(meu_user.email)  # clebert@gmail.com
print(meu_user.password)  # 123
meu_user.reset_password()  # Envia email de reset de senha

# Pilares
# Abstarção
# Encapsulamento

