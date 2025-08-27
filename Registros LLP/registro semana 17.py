nome=input('Digite o nome do aluno: ')
nota1=float(input('Digite a nota do aluno: '))
nota2=float(input('Digite a nota do aluno: '))
nota3=float(input('Digite a nota do aluno: '))
nota4=float(input('Digite a nota do aluno: '))

media=(nota1+nota2+nota3+nota4)/4

print(f'A média do aluno foi {media}')

if media>=7:
    print('Aprovado!')
elif media>=5<7:
    print('Dá para melhorar!!')
else:
    print('Reprovado!!')