print('-------------------------------------------------------------------------------')
# Digite a ou b como 0 pra ver oque acontece:
a = int(input('Digite A para Dividendo'))
b = int(input('Digite C para Divisor'))
r = a / b
print(r)

print('-------------------------------------------------------------------------------')

#erro com tipo de dados
dado = '13o5'
valor = int(dado)
print('valor')

print('-------------------------------------------------------------------------------')

#erros com posições no vetor ¹12, ²13 ³14...
l = [ 12, 13, 14, 15]
print(l[10])

print('-------------------------------------------------------------------------------')

#tente com 0 agora
a = int(input('Digite A para Dividendo'))
b = int(input('Digite C para Divisor'))
try:
    r = a / b
    print(f'O Resultado é: {r}')
except:
    print('Nao é possivel calcular essa divisão')

print('-------------------------------------------------------------------------------')

try:
    a = int(input('Digite A para Dividendo'))
    b = int(input('Digite C para Divisor'))
    r = a / b
    print(f'O Resultado é: {r}')
except:
    print('Nao é possivel fazer essa Divisao')

print('-------------------------------------------------------------------------------')

try:
    a = int(input('Digite A para Dividendo'))
    b = int(input('Digite C para Divisor'))
    r = a / b
    print(f'O Resultado é: {r}')
except ZeroDivisonError:
    print('B nao pode ser 0')
except ValueError:
    print('Digite numeros Inteiros para A e B')
except:
    print('Nao é possivel calcular essa divisão. Erro Desnhecido')

print('-------------------------------------------------------------------------------')