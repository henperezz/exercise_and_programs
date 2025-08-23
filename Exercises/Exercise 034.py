nome=input('Digite seu nome: ')
sal=float(input('Digite seu salário: R$'))

if sal>1250:
    aumento=(10/100)*sal
    novosal=aumento+sal
    print(f'Olá {nome}, seu salário sofreu um reajuste de 10%, passando a ser R%{novosal:.2f}')
else:
    aumento=(15/100)*sal
    novosal=aumento+sal
    print(f'Olá {nome}, seu salário sofreu um reajuste de 15%, passando a ser R%{novosal:.2f}')