#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.
import random

senhaPadrao = str(input('Digite uma senha padrão: '))
senha = ''
while senha != senhaPadrao:
    senha = str(input('Digite sua senha para continuar: '))
    print('-=' * 50 )
    print('Seja bem vindo! Te apresento o jogo da advinhação onde você precisará acertar um número de 0 a 10.')

    numAleatorio = random.randint(0,10)
    numUsuario = ''
    while numUsuario != numAleatorio:
        numUsuario = int(input('Digite seu palpite: '))
        if numUsuario != numAleatorio:
            if numAleatorio > numUsuario:
                print('O número é maior')
            else:
                print('O número é menor')

print('Parabéns você acertou!!')
