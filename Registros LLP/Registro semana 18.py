cargo = input('Digite seu cargo: ').capitalize().strip()
dia = input('Digite o dia da semana: ').capitalize().strip()

if cargo == 'Gerente':
    if dia in 'Sabado' or dia == 'Segunda' or dia == 'Terça' or dia == 'Quarta' or dia == 'Quinta' or dia == 'Sexta':
        print('Acesso válido')
    else:
        print('Acesso inválido')
elif cargo == 'Estagiario':
    if dia == 'Segunda' or dia == 'Quarta' or dia == 'Sexta':
        print('Acesso válido')
    else:
        print('Acesso inválido')
elif cargo == 'Analista':
    if dia == 'Segunda' or dia == 'Terça' or dia == 'Quarta' or dia == 'Quinta' or dia == 'Sexta':
        print('Acesso válido')
    else:
        print('Acesso inválido')
else:
    print('Cargo inválido')