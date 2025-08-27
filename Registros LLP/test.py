cargo = input('Digite seu cargo: ').capitalize().strip()
dia = input('Digite o dia da semana: ').capitalize().strip()

if cargo == 'Gerente':
    if dia in ['Sabado', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']:
        print('Acesso válido')
    else:
        print('Acesso inválido')
elif cargo == 'Estagiario':
    if dia in ['Segunda', 'Quarta', 'Sexta']:
        print('Acesso válido')
    else:
        print('Acesso inválido')
elif cargo == 'Analista':
    if dia in ['Segunda', 'Terça', 'Quarta', 'Quinta',  'Sexta']:
        print('Acesso válido')
    else:
        print('Acesso inválido')
else:
    print('Cargo inválido')