from math import prod

def soma (valor1, valor2):
    return valor1 + valor2
        

def subtracao(valor1, valor2):
        return valor1 -  valor2
        
def multiplicacao(valor1, valor2):
        return valor1*valor2
        

def divisao(dividendo, divisor):
    if divisor == 0 :
        print('Não é possível dividir por zero')
    else:
        return dividendo/divisor

def exponenciacao(base, expoente):
        return base**(expoente)

def verificacao(valor1,valor2):
        pass

def fatorial(valor):
    li = [] 
    for x in range(valor,0,-1):
        li.append(x)
        print(f'{x}', end='-')
    print(f'>{prod(li)}')

def tabuada(valor):
    for x in range(1,11) :
        print(f'{x}x{valor}={valor*x} ')

    