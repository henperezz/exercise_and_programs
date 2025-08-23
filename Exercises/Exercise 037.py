numero = int(input('Digite um número inteiro: '))
acao = int(input('''Escolha uma base de conversão
Digite [1] para binário
Digite [2] para Octal
Digite [3] para Hexadecimal
Digite [4] para Sair
'''))

if acao == 1:
    bina = bin(numero)
    print(bina[2:])
elif acao == 2:
    octal = oct(numero)
    print(octal[2:])
elif acao == 3:
    hexa = hex(numero)
    print(hexa[2:])
else:
    print('Saindo')
