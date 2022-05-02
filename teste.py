from opera import soma, subtracao, multiplicacao, divisao, exponenciacao
from math import prod


print(soma(2,3))
print(subtracao(5,10))
print(multiplicacao(10,8))
print(divisao(20,10))
print(exponenciacao(2,6))

def tabuada(valor):
    for x in range(1,11) :
        print(f'{x}x{valor}={valor*x} ')

tabuada(5)


def fatorial(valor):
    li = [] 
    for x in range(valor,0,-1):
        li.append(x)
        print(f'{x}', end='-')
    print(f'>{prod(li)}')

fatorial(5)
