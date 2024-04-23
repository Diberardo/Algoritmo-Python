nome = input('Digite o Nome:')
peso = float(input('Digite o peso:'))

if peso < 52:
    categoria = ''
elif peso < 65:
    categoria = 'Pena'
elif peso < 72:
    categoria = 'Leve'
elif peso < 79:
    categoria = 'Ligeiro'
elif peso < 86:
    categoria = 'Meio - Médio'
elif peso < 93:
    categoria = 'Médio'
elif peso < 100:
    categoria = 'Meio - Pesado'
else:
    categoria = 'Pesado'

msg = 'O Lutador: {} \npesa: {:.3} kg \nE se enquadra da categoria: {}'
if categoria != '':
    print(msg.format(nome,peso,categoria))
else:
    print(f'Peso Invalido: {peso}')

