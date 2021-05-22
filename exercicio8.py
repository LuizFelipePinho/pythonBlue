#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a 
# CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos
#  anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


nome = str(input('Digite seu nome: '))
anoNascimento = int(input('Digite a data de nascimento: '))
idade = 2021 - anoNascimento
ctps = int(input('Digite a ctps: '))

pessoa = dict()

pessoa['nome'] = nome
pessoa['idade'] = idade
pessoa['ctps'] = ctps

print(pessoa)

if ctps != 0:
    anoContratacao = int(input('Digite o ano da sua contratação: '))
    salario = float(input('Digite o salário: '))
    pessoa['anoContratacao'] = anoContratacao
    pessoa['salario'] = salario

aposenta = 35 - (2021 - anoContratacao)

print(f'A pessoa deve se aposentar com {aposenta + idade}')