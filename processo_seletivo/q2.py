termo1=int(0)
termo2=int(1)
termo3=int(0)
print('-'*42)
print(''*3, 'Consulta da sequência de Fibonacci')
print('-'*42)
valor = int(input('Digite um número:'))
while valor > termo3:
    termo3=termo1 +termo2
    termo1=termo2
    termo2=termo3
    if valor==0 or valor==1:
        print('O valor faz parte da sequência de Fobonacci.')
    elif valor ==termo3:
        print('O número faz parte da sequência de Fibonacci.')
    else:
            print (' O número digitado não faz parte da sequência de Fibonacci.')