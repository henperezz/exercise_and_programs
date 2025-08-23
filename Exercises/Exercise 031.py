distancia=float(input('Digite a distância em Km: '))

if distancia<=200:
    valor= distancia*0.50
    print(f'O valor por Km da viagem foi de R$0.50, sendo o total de R${valor:.2f}')
else:
    valor= distancia*0.45
    print(f'O valor por Km da viagem foi de R$0.45, sendo o total de R${valor:.2f}')