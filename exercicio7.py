#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os 
# valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

listaPares= list()
listaImpares = list()

for i in range(0,6):
    num = float(input("Digite um número: "))
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)

pares = sorted(listaPares)
impares = sorted(listaImpares)
print(f'Números pares em ordem crescente: {pares}')
print(f'Números impares em ordem decrescente: {impares}')