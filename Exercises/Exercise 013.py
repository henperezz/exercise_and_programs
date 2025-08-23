#Faça um programa que leia o salário de um funcionário e mostre ele novamente com um ajuste de 15%

sal1=float(input('Digite o salário: R$'))

sal2=sal1*(15/100)

print(f'O seu salário de R${sal1} sofreu um reajuste e será a partir de agora de R${sal2+sal1}')