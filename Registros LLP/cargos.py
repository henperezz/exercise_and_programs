cargo=input('Digite o cargo: ').strip().lower()
dia=input('Digite o dia da semana: ').strip().lower()


if cargo==('gerente') and dia==('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado'):
    print('Acesso permitido!')
elif cargo==('analista') and dia==('segunda', 'terça', 'quarta', 'quinta', 'sexta'):
    print('Acesso permitido!')
elif cargo==('estagiário') and dia==('segunda', 'quarta', 'sexta'):
    print('Acesso permitido!')
else:
    print('Acesso negado!')