class Aluno:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def show_infos(self):
        print(f"Ola, me chamo {self.nome} meu email é: {self.email}")


aluno_1 = Aluno("Cleber", "cleber@gmail.com")

aluno_1.show_infos()
