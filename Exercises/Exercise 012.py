#Faça um programa que leia o preço do produto e desconte 5% a ele

pre=float(input('Digite o valor do produto: R$'))

desc=pre*(5/100)

print(f'O novo valor do produto será de R${pre+desc} após um desconto de 5%')