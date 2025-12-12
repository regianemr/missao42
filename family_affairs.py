#!/usr/bin/env python3

def find_the_redheads(dicionario):
  #funcao lambda
    def ruivo(x): return x[1] == "red"
    ruivos = list(filter(ruivo, dicionario.items()))
    return [x[0] for x in ruivos]
# list esta sendo usado aqui por requisicao da questao, porem não seria necessário, usando o list comprehension


família_dupont = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

find_the_redheads(família_dupont)
