print('Inicio DO Programa:')
cont = 1
while cont <= 10:
    print(cont)
    cont+=1
print('Fim Do Promagra')


print('----------------------------------------------------------------------------------')

x = 1
while x != 0:
    x = int(input('Digite o Numero = '))
    if x % 2 == 0:
        print(f'{x}: é Par')
    else:
        print(f'{x}: é Impar')
print('Acabou o Programa')

print('----------------------------------------------------------------------------------')

n = int(input('Digite N:'))
cont = 1
while cont <= 10:
    r = cont * n
    print(f'{cont} X {n} = {r}')
    cont += 1
print('Fim do Programa')

print('----------------------------------------------------------------------------------')

p = int(input('Digite o Primeiro Termo:'))
r = int(input('Digite a Razão:'))
cont = 0
while cont < 10:
    print(p)
    p += r
    cont += 1
print('Fim do Programa')

print('----------------------------------------------------------------------------------')

d = int(input('Digite D:'))
if d < 0:
    print(f'O valor {d} é invalido')
else:
    i = 1
    while i < 100:
        if i % d == 0:
            print(i)
        i += 1
    print('Fim do programa')

print('-----------------------------------------------------------------------------')

soma = 0
qtde = 1
a = 1
while a != 0:
    a = int(input('Digite X: '))
    if a != 0:           # testes sem if
        soma += a
        qtde += 1
print(f'Soma dos Valores: {soma}')
print(f'Quantidade: {qtde}')
print('Fim do Programa')

print('-----------------------------------------------------------------------------')

i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)

print('-----------------------------------------------------------------------------')

x = 1
while True:
    x = int(input('Digite X: '))
    if x == 0:
        print('Você Digitou 0 . . . ')
        break
    print(x)
print('Fim do Programa')

print('-----------------------------------------------------------------------------')

x = 1
while x > 0:
    x = int(input('Digite X: '))
    if x == 0:
        print('\tVoce Digitou 0')
        break
print(x)
else:
    print('Voce Digitou um Nuemro Negativo')
print('Fim Do programa')
