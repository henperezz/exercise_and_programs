from datetime import date

anonasc = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - anonasc

if idade == 18:
    print('Hora de se alistar!')
elif idade > 18:
    tempopass= idade - 18
    print(f'Passou da hora de se alistar! você deveria ter se alistado há {tempopass} anos')
else:
    tempofut= 18 - idade
    print(f'Ainda há {tempofut} anos para se alistar!')
