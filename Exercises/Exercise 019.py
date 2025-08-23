import random

nome1=input('Digite o nome do aluno: ')
nome2=input('Digite o nome do aluno: ')
nome3=input('Digite o nome do aluno: ')
nome4=input('Digite o nome do aluno: ')

list=[nome1, nome2, nome3, nome4]
escolhido=random.choice(list)

print(f'O aluno selecionado foi {escolhido}')