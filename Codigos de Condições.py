# Input do Python
a = input('digite algo = ')
print(type(a))

b = input('digite um inteiro = ') #vem em string
print(type(b))
b = int(b)
print(type(b)) # tem mudar o tipo

c = int(input('digite A: ')) #maneira mais rapido



# Como Coloca Biblioteca
import math # pode incluir o função direto // from math import sqrt
x = 49
r = math.sqrt(x)
print(r)
# o cmath é uma biblioteca para variaveis imaginarias

#Condições Mutíplas
ph = float (input('Digite o PH = '))
if ph < 6.0:
    r = 'Acida'
elif ph < 7.0:
    r = 'Levemenete Acida'
elif ph < 8.0:
    r = 'levemente alacalina'
else:
    r = 'alcalina'
print(f'Com ph: {ph} a soluçao: {r}')



# Outro Modelo de Mutíplas
nome = input('Digite o nome')
peso = float(input('digite o peso'))

if peso < 52:
    categoria = ''
elif peso < 65:
    categoria = 'pena'
elif peso < 72:
    categoria = 'leve'
elif peso < 79:
    categoria = 'ligeiro'
elif peso < 86:
    categoria = 'meio-Medio'
elif peso < 93:
    categoria = 'medio'
elif peso < 100:
    categoria = 'meio-pesado'


# Simples Condicionais
a = int(input('digite a = '))
b = int(input('digite b = '))

if b == 0:
    print('Nao é possivel calcular a divisão ')
else:
    r = a / b
    print(r)



# Analise de Riscos
risco = input('Digite BX ou  Al para o grau dos Riscos = ')

if risco != 'bx' and risco != 'al':
    print(f'{risco} é invalido para o grau de risco')
    exit()

valor = float(input('Digite o Valor = '))

if risco == 'bx':
        if valor < 1000.0:
            tipo = 'poupança'
        else:
            tipo = 'Rende Fixa'
else:
        if valor < 1000.0:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'
print(f'Voce deve insvestir em: {tipo} com esse valor: {valor}')