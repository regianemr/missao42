#!/usr/bin/env python3

def array_de_nomes(pessoas):
    lista = []
    # fazer um for loop no dicionario
    for nome, sobrenome in pessoas.items():
        nome_completo = f"{nome.capitalize()} {sobrenome.capitalize()}"
        lista.append(nome_completo)
    return lista

    #   pegar o nome(chave) e o sobrenome(valor) e capitalizar
    # jogar em uma lista
nomes_pessoas = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_de_nomes(nomes_pessoas))
