#Faça um programa que calcule o valor do aluguel de um carro sabendo que R$60 dia e R$0,15 por km

dia=int(input('Quantos dias o carro foi alugado? '))
km=float(input('Quantos km o carro foi rodado? '))

alug=(dia*60)+(km*0.15)

print(f'O aluguel do carro ficará em R${alug:.2f}')