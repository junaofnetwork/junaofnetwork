print("hello World")
x = 10 
nome = "aluno"
nota = 8.75
fez_inscricao = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))


nomeDigitado = input("Digite nome: ")
print(nomeDigitado)


print("Olá %s, bem vindo a displina de programção. parabens pelo seu primeiro Hello World" % (nomeDigitado))


print("Olá {}, bem vindo a Disciplina de programação. Parabéns pelo seu primeiro Hello world".format(nomeDigitado))


print(f"Olá {nomeDigitado}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world")

x1 = int(input("Primeiro Numero: "))

y1 = int(input("Segundo Numero: "))

multiplicador = int(input("Quanto tu quer de multiplicador por favor: "))

operacao_1 = x + y1 * multiplicador

operacao_2 = (x + y1) * multiplicador

operacao_3 = x / y1 ** multiplicador

operacao_4 = x % y1 + multiplicador

print(f"Resultado em operacao_1 = {operacao_1}")
print(f"Resultado em operacao_2 = {operacao_2}")
print(f"Resultado em operacao_3 = {operacao_3}")
print(f"Resultado em operacao_4 = {operacao_4}")


a2 = 2
b2 = 0.5
c2 = 1
x2 = float(input("digite o valor de x: "))

y2 = a2 * x2 ** 2 + b2 * x2 + c2

print(f"O resultado de y para x = {x2} é {y2}.")


c3 = 200 #constante

mes = int(input("Digite o mês que deseja saber o resultado: "))

r3 = c3 * mes

print(f"A quantidade de peças para o mês {mes} será {r3}")



a2 = int(input("Digite o primeiro: "))
b2 = int(input("Digite o segundo: "))

if a2 < b2:
    print(f"O maior valor é {b2}")
else:
    print(f"O maior valor é {a2}")

r2 = a2 + b2
print(r2)

print(f"Lista de Codigos para as operações desejada, [5222(compra á vista)] [5333(Compra à prazo no boleto)], [5444(Compra à prazo no cartão)],")
codigo_compra = int(input("Digite a Operação: "))

if codigo_compra == 5222:
    print("Você comprou á vista")
elif codigo_compra == 5333:
    print("Você comprou à prazo no boleto")
elif codigo_compra == 5444:
    print("Você comprou à prazo no cartão")
else:
    print("Operação não encontrada")


qtde_faltas = int(input("Digite a Quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")


numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
'''

'''nomeV = "João Eduardo Brandenburg de almeida"
for i in nomeV:
    print(i)

nomeV2 = "João Eduardo Brandenburg de almeida"
for i, c in enumerate(nomeV2):
    print(f"Posição: {i}, Letra: {c}")


disciplina = "João Eduardo Brandenburg de almeida"
for i in disciplina:
    if i == "a":
        continue
    else:
        print(i)

texto = """
A inserção de comentários no código do programa é uma prática normal.
Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.
O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado (BANIN, p. 45, 2018)."
"""

for i, c in enumerate(texto):
    if c == 'a' or c == 'e':
        print(f"Vogal '{c}' encontrada, na posição {i}")
    else:
        continue


salarioio = 0
salario = float(input("Digite o salário do colaborador: "))

if salario <= 1903.98:
    print(f"O colaborador isento de imposto.")
    print(f"Salário a receber = {salario}")
elif salario <= 2826.65:
    print(f"O colaborador deve pagar R$ 142,80 de imposto.")
    print(f"Salário a receber = {salario - 142.80}")
elif salario <= 3751.05:
    print(f"O colaborador deve pagar R$ 354,80 de imposto.")
    print(f"Salário a receber = {salario - 354.80}")
elif salario <= 4664.68:
    print(f"O colaborador deve pagar R$ 636,13 de imposto.")
    print(f"Salário a receber = {salario - 636.13}")
else:
    print(f"O colaborador deve pagar R$ 869,36 de imposto.")
    print(f"Salário a receber = {salario - 869.36}")


a = int(input("Primeiro valor: "))
b = int(input("Segundo valor:"))

equacao = input("Digite a fórmula geral da equação linear")
print(f"\nA entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")


def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")

    
resultado = imprimir_mensagem("Python", "ADS")
print(f"Resultado = {resultado}")


def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0!
    return f'{d} de {mes_extenso} de {a}'

print(converter_mes_para_extenso('10/12/2021'))

def somar(a, b):
    return a + b

r = somar(200,500)
print(r)


def calcular_desconto(valor, desconto=0): # O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25) # Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")


def cadastrar_pessoa(nome, idade, cidade):
    print("\nDados a serem cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")
    

cadastrar_pessoa("João", 23, "São Paulo")
cadastrar_pessoa("São Paulo", "João", 23)


def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()


texto = converter_maiuscula(flag_maiuscula=False, texto="João") # Passagem nominal de parâmetros
print(texto)

def converter_minuscula(texto, flag_minuscula=True): # O parâmetro flag_minuscula possui True como valor default
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()


texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")

print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")

def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    
    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")

        
print("\nChamada 1")        
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")

print("\nChamada 2")        
imprimir_parametros(desconto=10, valor=100)



def calcular_valor(valor_prod, qtde, moeda="real", **kwargs):
    v_bruto = valor_prod * qtde
    
    if 'desconto' in kwargs:
        desconto = kwargs['desconto']
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif 'acrescimo' in kwargs:
        acrescimo = kwargs['acrescimo']
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto
    
    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0

    
valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")
