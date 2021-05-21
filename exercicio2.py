#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = str(input('Digite uma frase: ')).lower().strip()

contVogal = 0
palavraSemVogal = ''
for i, e in enumerate(frase):
    if e == 'a' or e == 'e' or e == 'i' or e == 'o' or e == 'u':
        contVogal += 1
    else:
        palavraSemVogal += e


print(f'A quantidade vogais na palavra {frase} é: {contVogal}')
print(f'A palavra que você digitou, sem vogal fica aasim: {palavraSemVogal}')
