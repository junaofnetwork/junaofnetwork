class Personagem:
    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.habilidades_basicas = self.classe.habilidades_basicas.copy()
        self.bonus_classe = self.classe.bonus_classe.copy()

    def imprimir_ficha(self):
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Classe: {self.classe.nome}")
        print("Habilidades Básicas:")
        for habilidade, valor in self.habilidades_basicas.items():
            print(f"  {habilidade}: {valor}")
        print(f"Bônus de Classe: {self.bonus_classe}")


class Guerreiro:
    nome = "Guerreiro"
    habilidades_basicas = {
        "Ataque": 10,
        "Defesa": 5,
        "Agilidade": 5,
        "Inteligência": 0,
        "Carisma": 0,
        "Força": 10,
        "Resistência": 5
    }
    bonus_classe = {"Ataque": 10, "Força": 10}


class Mago:
    nome = "Mago"
    habilidades_basicas = {
        "Ataque": 5,
        "Defesa": 5,
        "Agilidade": 5,
        "Inteligência": 10,
        "Carisma": 0,
        "Força": 0,
        "Resistência": 5
    }
    bonus_classe = {"Inteligência": 10}


class Bardo:
    nome = "Bardo"
    habilidades_basicas = {
        "Ataque": 5,
        "Defesa": 5,
        "Agilidade": 10,
        "Inteligência": 5,
        "Carisma": 10,
        "Força": 0,
        "Resistência": 5
    }
    bonus_classe = {"Agilidade": 10}


def selecionar_raca():
    print("Selecione uma raça:")
    print("1. Humano")
    print("2. Elfo")
    print("3. Anão")
    print("4. Orc")
    print("5. Goblin")
    escolha = input("Digite o número da raça: ")
    if escolha == "1":
        return "Humano"
    elif escolha == "2":
        return "Elfo"
    elif escolha == "3":
        return "Anão"
    elif escolha == "4":
        return "Orc"
    elif escolha == "5":
        return "Goblin"
    else:
        print("Raça inválida. Tente novamente.")
        return selecionar_raca()


def selecionar_classe():
    print("Selecione uma classe:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Bardo")
    escolha = input("Digite o número da classe: ")
    if escolha == "1":
        return Guerreiro
    elif escolha == "2":
        return Mago
    elif escolha == "3":
        return Bardo
    else:
        print("Classe inválida. Tente novamente.")
        return selecionar_classe()


# Example usage
nome = input("Digite o nome do personagem: ")
raca = selecionar_raca()
classe = selecionar_classe()
personagem = Personagem(nome, raca, classe)
personagem.imprimir_ficha()