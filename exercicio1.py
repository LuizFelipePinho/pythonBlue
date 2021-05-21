#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1 + n2
multi = n1 * n2
div = n1 // n2
maior = max(n1,n2)

print('-='*40)
print(f'A soma é: {soma}')
print(f'A multiplicação é: {multi}')
print(f'A divisão inteira é: {div:.0f}')
print(f'O maior número é {maior}') 
if soma % 2 == 0:
    print(f'O número {soma} é par')
else:
    print(f'O número {soma} é impar')


if multi > 40:
    result = multi / div
    print(f'O resultado da divisão de {multi} com {div} é: {result}')
else:
    print(f'{n1} x {n2} = {multi} ou seja, não é  maior que 40')

print('-='*40)
