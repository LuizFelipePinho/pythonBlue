#Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

from datetime import date
dataAtual = date.today().year
print(dataAtual)




def dataExtenso(data):
    dia = data[:2]
    mes = data[3:5]
    mesint = int(mes)
    ano = data[6:]
    mesExtenso = 0
    if mesint == 1:
        mesExtenso = 'Janeiro'
    elif mesint == 2:
        mesExtenso = 'Feveiro'
    elif mesint == 3:
        mesExtenso = 'Março'
    elif mesint == 4:
        mesExtenso = 'Abril'
    elif mesint == 5:
        mesExtenso = 'Maio'
    elif mesint == 6:
        mesExtenso = 'Junho'
    elif mesint == 7:
        mesExtenso = 'Julho'
    elif mesint == 8:
        mesExtenso = 'Agosto'
    elif mesint == 9:
        mesExtenso = 'Setembro'
    elif mesint == 10: 
        mesExtenso = 'Outubro'
    elif mesint == 11:
        mesExtenso = 'Novembro' 
    elif mesint == 12:
        mesExtenso = 'Dezembro'
    
    mensagem = dia + ' de ' + mesExtenso + ' de ' + ano
    
    return mensagem



   
while True:
    data = str(input('Digite a data atual no formato DD/MM/AAAA: '))
    dia = int(data[:2])
    mes = int(data[3:5])
    if len(data) != 10 or dia > 32 or dia < 1 or mes < 1 or mes > 12:
        print('Data inválida:') 
    else:
        break

    


result = dataExtenso(data)
print(result)

