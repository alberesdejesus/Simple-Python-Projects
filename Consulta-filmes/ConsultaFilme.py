import requests
import json


def requisicao(titulo):
    try:
        req = requests.get(f"http://www.omdbapi.com/?apikey=e0690026&t={titulo}&type=movie")
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as err:
        print('Erro na conexao: ' + str(err))
        return None


def printar_detalhes(filme):
    print('Titulo: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Diretor: ', filme['Director'])
    print('Atores: ', filme['Actors'])
    print('Nota: ', filme['imdbRating'])
    print('Premios: ', filme['Awards'])
    print('Poster', filme['Poster'])
    print('')


sair = False
while not sair:
    op = input("Escreva o nome de um filme ou SAIR para fechar: ").lower()

    if op == 'sair':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme["Response"] == "False":
            print(filme['Error'])
        else:
            printar_detalhes(filme)
