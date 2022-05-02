from opera import soma, subtracao, multiplicacao, divisao, exponenciacao, verificacao, fatorial, tabuada


def iniciar():
    while True:
        opcao = int(input('1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - exponenciação\n'
        '6 - fatorial\n7 - tabuada\n8 - sair\n'))   

        if opcao == 1:
            valor1 = input('Digite o primeiro valor ')
            valor2 = input('Digite o segundo valor ')
            if valor1.isalpha() or valor2.isalpha():
                print('Por favor Digite somente números!!')
            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                print(soma(valor1,valor2))

        if opcao == 2:
            valor1 = input('Digite o primeiro valor ')
            valor2 = input('Digite o segundo valor ')
            if valor1.isalpha() or valor2.isalpha():
                print('Por favor Digite somente números!!')
            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                print(subtracao(valor1,valor2))

        if opcao == 3:
            valor1 = input('Digite o primeiro valor ')
            valor2 = input('Digite o segundo valor ')
            if valor1.isalpha() or valor2.isalpha():
                print('Por favor Digite somente números!!')
            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                print(multiplicacao(valor1,valor2))

        if opcao == 4:
            valor1 = input('Digite o primeiro valor ')
            valor2 = input('Digite o segundo valor ')
            if valor1.isalpha() or valor2.isalpha():
                print('Por favor Digite somente números!!')
            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                print(divisao(valor1,valor2))

        if opcao == 5:
            valor1 = input('Digite o primeiro valor ')
            valor2 = input('Digite o segundo valor ')
            if valor1.isalpha() or valor2.isalpha():
                print('Por favor Digite somente números!!')
            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                print(exponenciacao(valor1,valor2))

        if opcao == 6:
            valor = input('Digite o valor do fatorial\n')
            if valor.isalpha():
                print('Por favor Digite somente números!!')
            else:
                valor = int(valor)
                fatorial(valor)

        if opcao == 7:
            valor = input('Digite o valor da tabuada que deseja ver\n')
            if valor.isalpha():
                print('Por favor Digite somente números!!')
            else:
                valor = int(valor)
                print(tabuada(valor))

        if opcao == 8:
            break
    
    
