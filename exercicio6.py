#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

lista = list()

pergunta1 = str(input('Telefonou para a vítima: [S/N] ')).upper()
lista.append(pergunta1)

pergunta2 = str(input('Esteve no local do crime? [S/N] ')).upper()
lista.append(pergunta2)

pergunta3 = str(input('Mora perto da vítima? [S/N] ')).upper()
lista.append(pergunta3)

pergunta4 = str(input('Devia para a vítima? [S/N] ')).upper()
lista.append(pergunta4)

pergunta5 = str(input('Já trabalhou com a vítima? [S/N] ')).upper()
lista.append(pergunta5)

contS = contN = 0
for i in range(0, len(lista)):
    if lista[i] == 'S':
        contS += 1
    else:
        contN += 1

if contS == 2:
    print('Você é suspeito(a) ')
elif contS >= 3 and contS <= 4:
    print('Você é cumplice')
elif contS == 5:
    print('Você é o culpado')