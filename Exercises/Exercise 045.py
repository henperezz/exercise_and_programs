from random import randint
import time

user=int(input('''Escolha uma das opções:
[1] Pedra
[2] Papel
[3] Tesoura
'''))

print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO!!')

computador = randint(1,3)

if computador==user:
    if computador==1:
        print(f'''{'EMPATE':=^40}
Ambos jogaram PEDRA!''')
    elif computador==2:
        print(f'''{'EMPATE':=^40}
Ambos jogaram PAPEL!''')
    elif computador==3:
        print(f'''{'EMPATE':=^40}
Ambos jogaram TESOURA!''')
elif user==1 and user!=computador:
    if computador==2:
        print(f'''{'VITÓRIA DA MÁQUINA!':=^40}
A máquina jogou PAPEL e o usuário PEDRA!''')
    elif computador==3:
        print(f'''{'VITÓRIA DO USUÁRIO!':=^40}
A máquina jogou TESOURA e o usuário PEDRA!''')
elif user==2 and user!=computador:
    if computador==1:
        print(f'''{'VITÓRIA DO USUÁRIO':=^40}
A máquina jogou PEDRA e o usuário TESOURA!''')
    elif computador==3:
        print(f'''{'VITÓRIA DA MÁQUINA!':=^40}
A máquina jogou TESOURA e o usuário PAPEL!''')
else:
    if computador==1:
        print(f'''{'VITÓRIA DA MÁQUINA':=^40} 
A máquina jogou PEDRA e o usuário TESOURA!''')
    elif computador==2:
        print(f'''{'VITÓRIA DO USUÁRIO':=^40}
A máquina jogou PAPEL e o usuário TESOURA!''')
