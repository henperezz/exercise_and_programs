#Faça um programa que leia duas notas e calcule a média de um aluno

nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))

media=(nota1+nota2)/2

if media>=5:
    print(f'Parábens, você foi aprovado com uma média de {media}')
else:
    print(f'Você foi reprovado com uma média de {media}')