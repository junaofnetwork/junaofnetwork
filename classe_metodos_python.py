class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def cumprimentar(self):
        return f"Olá meu nome é {self.nome}."

    def aniversario(self):
        self.idade += 1


Humano01 = Pessoa('João eduardo Brandenburg de almeida',23,'Macho alfa')


print(Humano01.cumprimentar())

print(f'Idade: {Humano01.idade}')

Humano01.aniversario()

print(Humano01.cumprimentar())

print(f'Sou super: {Humano01.sexo}')

print(f'Nova idade: {Humano01.idade}')