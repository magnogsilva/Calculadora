def calculadora(n1,n2,op):
    if op==1:
        res = n1+n2
        print('O resultado é {}'.format(res))
    elif op==2:
        res = n1-n2
        print('O resultado é {}'.format(res))
    elif op==3:
        res = n1*n2
        print('O resultado é {}'.format(res))
    elif op==4:
        res = n1/n2
        print('O resultado é {}'.format(res))
    else:
        res = 0
        print('O resultado é {}'.format(res))

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('ESCOLHA A OPERAÇÃO DESEJADA')
print('[1] SOMA')
print('[2] SUBTRAÇÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] DIVISÃO')
op = int(input('Digite o número que corresponde a operação: '))
calculadora(n1,n2,op)
