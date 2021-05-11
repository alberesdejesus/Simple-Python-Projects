import requests
import json


def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            print('Pesquisando na pagina: ', i)
            req = requests.get(f"http://www.omdbapi.com/?apikey=e0690026&s={titulo}&type=movie&page={str(i)}")
            dicionario = json.loads(req.text)
            if dicionario['Response'] == 'True':
                for filme in dicionario['Search']:
                    title = filme['Title']
                    ano = filme['Year']
                    string = title + '(' + ano + ')'
                    lista.append(string)
            else:
                print('Fim das paginas')
                break
        except:
            print('Erro na conexao:')
    return sorted(lista)


sair = False
while not sair:
    op = input("Escreva o nome de um filme ou SAIR para fechar: ").lower()

    if op == 'sair':
        sair = True
        print('Saindo...')
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados:', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)
