import pandas as pd

venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'quantidade': [50, 70]}

vendas_df = pd.DataFrame()


print(vendas_df)


vendas_df = pd.read_excel("Vendas.xlsx")

print(vendas_df)


pd.Series(data=5)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

pd.Series(lista_nomes) # Cria uma Series com uma lista de nomes


print(lista_nomes)


dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}

dados_df = pd.Series(dados) # Cria uma Series com um dicionário


print(dados_df)

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

dados = pd.Series(lista_nomes, index=cpfs)

print(dados)
