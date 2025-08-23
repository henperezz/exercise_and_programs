#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e...
#... a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m²

largura=float(input('Digite a largura da parede em metros: '))
altura=float(input('Digite a altura da parede em metros: '))

area=largura*altura
tinta=area/2

print(f'A área da parede é de {area:.1f}M² e a quantidade de tinta necessária é de {tinta:.1f}L')