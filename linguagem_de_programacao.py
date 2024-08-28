import numpy as np

'''nota1 = int(input('digite a primeira nota: '))
nota2 = int(input('digite a segunda nota: '))
nota3 = int(input('digite a terceira nota: '))
nota4 = int(input('digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4
    
if media >= 6:
        situação = 'aprovado'
else:
        situação = 'reprovado'
        
print(f"a media das notas é:{media}")
print(f"a situação é:{situação}")




filmes = {
    "A perseguição o filme..": 18,
    "Kung Fu Jacaré": 0,
    "O velho Jon": 12
}

idade = int(input("Qual é a sua idade? "))

for filme, idade_minima in filmes.items():
    if idade >= idade_minima:
        print("Você pode assistir a {}.".format(filme))
    else:
        print("Você não pode assistir a {}.".format(filme))
'''



'''numeros = int(input("digite um numero (ou 0 para sair): "))

while numeros != 0:
    if numeros % 2 == 0:
        print("o numero {} é par".format(numeros))
    else:
        print("o numero {} é impar".format(numeros))
    numeros = int(input("digite um numero (ou 0 para sair): "))
'''


'''filmes = ['Filme 1', 'Filme 2','Filme 3', 'Filme 4', 'Filme 5']

for filme in filmes:
    classificacao = int(input(f'Como você classificaria {filme} de 1 a 5 (ou 0 se quiser parar)?: '))

    if classificacao == 0:
        print('Fim')
        break

    if classificacao < 1 or classificacao > 5:
        print('Classificação inválida. Por favor, digite um número entre 1 e 5.')
    else:
        print(f'Você classificou {filme} com {classificacao}.')

    
'''
'''print("obrigado por classificar os filmes tenha uma otima semana")'''



'''numero = [1,2,3,4,5,6,200]

numero = len(numero)

print(f"O commprimento desta lista é :{numero}")'''


# Lista de notas dos estudantes

notas = [7.6, 8.0, 6.5, 9.0, 7.0]

 

# Função regular para calcular a média

def calcular_media(notas):

    total = sum(notas)

    media = total / len(notas)

    return media

 

# Função lambda para arredondar a média para duas casas decimais

arredondar_media = lambda media: round(media, 2)

 

# Calcular a média

media = calcular_media(notas)

media_arredondada = arredondar_media(media)

 

# Verificar se os estudantes foram aprovados

if media_arredondada > 7:
    situacao = "Aprovado"
else: 
    situacao = "Reprovado"
 

# Resultados

print(notas)

print(media_arredondada)

print(situacao)



texto = "explorando a diversidade de linguagens de programação com Python"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de e no texto = {texto.count('e')}")
print(f"As 5 primeiras letras são: {texto[:5]}")



texto[13]




cores = ['vermelho', 'azul', 'verde', 'rosa']
for cor in cores:

    print(f"A posição = {cores.index(cor)}, cor = {cor}")



Linguagens = ['C#','Java','Javascript','C']
print('Antes da listcomp =',Linguagens)
Linguagens = [item.lower() for item in Linguagens]
print("\nDepois da listcomp = ", Linguagens)



precos_em_dolares = [100,50,75,120]
taxa_de_cambio = 5.25
# Converter preços em dólares para reais
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)



numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros ))
print(numeros_pares)



vogais = ('a','e','i','o','u')
print(f"Tipo do objeto vogais = {type(vogais)}")
for p , x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")



convidados = ('Bob','Jake','Maria','João','Paulo')


confirmados = ['Bob','Jake']

nao_confirmados = [ convidado for convidado in convidados if convidado not in confirmados]


print("convidados que ainda nao Comfirmaram: ")
for pessoa in nao_confirmados:

    print(pessoa)

print("\nEnviando lembretes")



meu_conjunto = set()

meu_conjunto.add(100)
meu_conjunto.add(200)
meu_conjunto.add(300)

print("Meu conjuto com novidade",meu_conjunto)

elemento = 200

if elemento in meu_conjunto:
    print(f"O elemento {elemento} ja existe no conjunto")
else:
   print(f"O elemento {elemento} Não existe no conjunto")

meu_conjunto.remove(200)

print("Meu conjunto com elemento removido", meu_conjunto)



my_array = np.array([100,200,300,400,500])

print('Array Original')
print(my_array)

square_array = my_array ** 2
sum_of_elements = np.sum(my_array)

print("\nArray ao quadrado")
print(square_array)
print("\nSoma dos elementos do array")
print(sum_of_elements)

elements_at_index_2 = my_array[2]
print("\nElemento no indice 2 do array",elements_at_index_2)


