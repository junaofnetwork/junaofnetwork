class Brinquedo:
    def __init__(self, nome,):
        self.nome = nome
    def Mensagem(self):
        print("Olá, eu sou um brinquedo!")
    

class Boneco(Brinquedo):
    def __init__(self, nome, modelo):
        super().__init__(nome,)
        self.modelo = modelo

   
boneco01 = Boneco("Buz lightyear","O imperio da noite")

print(boneco01.nome)
print(boneco01.modelo)
boneco01.Mensagem()

    