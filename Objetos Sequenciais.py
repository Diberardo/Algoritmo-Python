print('\n--------------------------------------------------------------------\n')
l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print('\nExibição da lista Completa = O Conjunto')
print(l)
print('\nExibição dos elementos Individuais')
i = 0
while i < len(l): #len ja pega o tamanho do lista
    print(l[i], end = '')
    i += 1 # i = i + 1
print('Fim do Programa')

print('\n--------------------------------------------------------------------\n')

l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
type(l)
print('\nPor Elemento')
l[0]
l[1]
l[2]
l[3]
print('\nMostra tamanho da lista')
len(l)
print('Mostrar o grupo, com a primeira possição modificada')
l[0] = 999
print(l)

print('\n--------------------------------------------------------------------\n')

l = []
type(l)
l.append(3.88)
l.append(17.5)
print(l)
type(l[0])

print('\n--------------------------------------------------------------------\n')

#Ele imprime de tráz pra frente, usando o i negativo
a = [10, 12, 14, 16]
print[a[-1]]
print[a[-2]]
print[a[-3]]

print('\n--------------------------------------------------------------------\n')

#Excluir um elemento da lista
a = [10, 12, 14, 16]
del a[0] # função def exclui o elementos
print(a)

print('\n--------------------------------------------------------------------\n')

Origem = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
Destino1 = Origem[3 : 6] # mostra inicio e fim definido
print(Destino1)
Destino2 = Origem[1: 7: 2] # coloca o inicio e fim, mas com um pulo de 2,
print(Destino2)
Destino3 = Origem[:4] # sem o inicio
print(Destino3)
Destino4 = Origem[6:] # sem o fim
print(Destino4)

print('\n--------------------------------------------------------------------\n')

l = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print( 25 in l)
print( 99 in l)
print( 25 not in l)
print( 99 not in l)

print('\n--------------------------------------------------------------------\n')

p = int(input('\nDigite o Primeiro Termo:'))
r = int(input('\nDigite a Razão:'))
q = int(input('\nDigite a Quantidade:'))
termos = [p]
i = 0
while i < q - 1:
    p += r
    termos.append[p]
    i += 1
print('\nLista Resultante:')
print(termos)
print('Fim Do Programa')

print('\n--------------------------------------------------------------------\n')

l = range(10)
m = range(3, 8)
n = range(5, 12, 3)
# inicio, fim e os pulos (step)

print('\n--------------------------------------------------------------------\n')

p = int(input('\nDigite o Primeiro Termo:'))
r = int(input('\nDigite a Razão:'))
q = int(input('\nDigite a Quantidade:'))
ultimo = p + r * (q - 1)
termos = list(range(p, ultimo + 1, r))
print('Lista Gerada Com Ranger')
print(termos)
print('Fim do Programa')

print('\n--------------------------------------------------------------------\n')

l = [ 21, 45, 17, 28]
pos = 1
for valor in l:
    print(f'A Posção {pos} contém {valor}')
    pos += 1
print('Fim do Programa')

print('\n--------------------------------------------------------------------\n')

a = [10, 12, 14, 16]
b = [20, 22, 24]
r = a + b # + é um operador de concatenação
print(r)

print('\n--------------------------------------------------------------------\n')

a = [1, 2, 3] * 3
print(a)
b = [0] * 10 # * = cria multi copiar de uma sequencia
print(b)

print('\n--------------------------------------------------------------------\n')

n  = int(input('Digite a Quantidade:'))
l = []
for i in range(n):
    x = float(f'  elemento{i}:  ')
    l.append(x)
print('\nResultado')
for valor in l:
    print(f'  {valor} ')
print('Fim do Programa')

print('\n--------------------------------------------------------------------\n')

n  = int(input('Digite a Quantidade:'))
lstNeg = []
lstpos = []
for i in range(n):
    x = float(f'  elemento{i}:  ')
    if x > 0:
        lstpos.append(x)
    else:
        lstNeg.append(x)
print(f'\nLista de negativos : {lstNeg}, contém {len(lstNeg)} elementos')
print(f'\nLista de negativos : {lstpos}, contém {len(lstpos)} elementos')
print('Fim do Programa')

print('\n--------------------------------------------------------------------\n')

lstValores = []
valor = int(input('Digite um Inteiro:'))
while valor != 0:
    lstValores.append(valor)
    valor = int(input('Digite um Inteiro:'))
print('\nResultado')
print(lstValores)
print(f'A lista coném {len(lstValores)} Elementos')
print('Fim do Programa')

print('\n--------------------------------------------------------------------\n')

lstValores = []
valor = int(input('Digite um numero Inteiro:'))
while valor != 0:
    if valor in not lstValores:
        lstValores.append(valor)
    else:
        print(f'  ERRO! Valor Digitado {valor} ja esta na Lista')
    valor = int(input('Digite um Numero Inteiro:'))
print('\nResultado')
print(lstValores)
print(f'A lista cotém {len(lstValores)} Elementos')

print('\n--------------------------------------------------------------------\n')

from random import randint
lst = []
qtde = int(input('Digite uma Quantidade:'))
for i in range(qtde):
    a = randint(1,20)
    lst.append(a)
print('Lista Gerada')
print(f'  {lst} \n')
x = 1
while x > 0:
    x = int(input('Digite X:'))
    if x in lst:
        print(f'  Há {lst.count(x) } ocorencias {x}')
    else:
        print(f'  {x} não esta nessa lista')
print('Fim Do Programa')

print('\n--------------------------------------------------------------------\n')

print('\nListas Imnutaveis TUPLAS:') # sao lista que nao podem ser alteradas

print('\n--------------------------------------------------------------------\n')

t = ( 12, 'Python', 27.3, 14) #Testando todos os tipos de dados - Classe
type(t)
u = 12, 'Python', 27.3, 14 # pode colocar com ou sem, tanto faz, da na mesma
type(u)
print(t[0])
print(t[1])
for dados in t:
    print(dados, end = "--" )
t[0] = 26 # vai dar erro pq nao pode mudar
print('vai dar erro pq nao pode mudar ')

print('\n--------------------------------------------------------------------\n')

t = ( 3.6, 120, 'Texto')
type(t)
t = list(t)
type(t)
print('Agora pode modificar porque nao é mais uma tupla')
t[0] = 19.25
print(t)
print('Reconvertendo para tupla')
t = tuple(t)
type(t)
print(t)

print('\n--------------------------------------------------------------------\n')

print('Strings...')

print('\n--------------------------------------------------------------------\n')

s = input('Digite um Numero Inteiro:') # Digite letra pra ver oque acontece!
if s.isnumeric():
    n = int(s)
else:
    print('  ERRO:  digite apenas números')

print('\n--------------------------------------------------------------------\n')

s = input('Digite Dois Numeros Inteiros e um real:')
l = s.split() # faz a sepação dos espaços em branco
print('Lista L: ', l)
a = int(l[0])
b = int(l[1])
c = float(l[2])
print(f'A = {a}, B = {b}, C = {c}')

print('\n--------------------------------------------------------------------\n')

