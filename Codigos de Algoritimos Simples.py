# Expressões arritímedicas
a = 10
b = 25
c = 7
r = 2 * a + b
print(r)
r = 2 * ( a + b )
print(r)
r = ( a + b ) / ( a + c)
print(r)
r = ( 2 * b - c ) / ( 2 * a )
print(r)
r = -a * 2 + b
print(r)
r = a % b * c
print(r)



# Verificar se O numero é Par ou Impar
num = int(input('Digite um numero = '))
print('Esse Numero é:')

if num % 2 == 0:
    print('Par')
else:
    print('Impar')
 # print(f'O numero {num} é par' ou se for impar é a mesma coisa

A = int(input('Digite o valor de A = '))
B = int(input('Digite o valor de B = '))

if A < B:
     print(f'O {B} é o maior do que {A}')
if A == B:
    print(f'O dois sao iguais')
else:
    print(f'O a = {A} é o maior do que B = {B}')