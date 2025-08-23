frase=input('Digite sua frase: ').upper().strip()

print(f'Quantas vezes aparece a letra A: {frase.count('A')}')
print(f'Em que posição ela aparece pela primeira vez: {frase.find('A')+1}')
print(f'A ultima posição que A aparece: {frase.rfind('A')+1}')