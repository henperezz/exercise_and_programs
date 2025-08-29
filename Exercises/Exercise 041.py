from datetime import date

nome=input('Digite o nome do(a) atleta: ')
nascimento=int(input('Digite o ano de nascimento do(a) atleta: '))

idade = date.today().year - nascimento

print(f'O(a) atleta {nome} pode ser classificado em 5 categorias: Mirim, Infantil, Junior, Sênior e Master!')

if idade<=9:
    print('Atleta Mirim!')
elif idade<=14:
    print('Atleta Infantil')
elif idade<=19:
    print('Atleta Junior')
elif idade<=25:
    print('Atleta Sênior')
else:
    print('Atleta Master')
