"""
#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

"""


def semVogais(frase):
    contVogal = 0
    qtdRetiradaPalavras = 0

    palavraSemVogal = ''
    for i, e in enumerate(frase):
        if e == 'a' or e == 'e' or e == 'i' or e == 'o' or e == 'u':
            contVogal += 1
            qtdRetiradaPalavras += 1
        else:
            palavraSemVogal += e
    return contVogal, qtdRetiradaPalavras, palavraSemVogal




"""
print(f'A quantidade vogais na palavra {frase} é: {contVogal}')
print(f'A palavra que você digitou, sem vogal fica aasim: {palavraSemVogal}')"""


frase = str(input('Digite uma frase: ')).lower().strip()
result = semVogais(frase)
print(f'Quantidade de letras retiradas: {result[0]}')
print(f'Quantidade de vogais na frase: {result[1]}')
print(f'A palavra sem vogais fica assim: {result[2]}')