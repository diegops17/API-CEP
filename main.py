import requests, json

cep = int(input('Informe o cep no formato 00000000: '))
url = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()

for chave, valor in url.items():
    print(f'{chave}: {valor}')