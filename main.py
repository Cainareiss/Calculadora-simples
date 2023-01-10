A = int(input('Escolha um sistema de operação, 1 para Soma,2 para Subtração, 3 para Multiplicação, 4 para Divisão:'))
#O codigo utilizara da sua resposta para prosseguir com as resoluções .
if A == 1:
     b = int(input('Digite o primeiro valor:'))
     c = int(input('Digite o segundo valor:'))
     soma = int(b+c)
     print('A soma dos valores é: {}'.format(soma))
#utilizei o int em soma para mudar sua tipagem para inteiro para facilitar o processamento do codigo.
if A == 2:
    b = int(input('Digite o primeiro valor:'))
    c = int(input('Digite o segundo valor:'))
    sub = int(b-c)
    print('A subtração dos valores é: {}'.format(sub))
#O comando .format é de extrema revancia tendo em vista que ele permite usar qualquer tipagem no algoritmo.
if A == 3:
    b = int(input('Digite o primeiro valor:'))
    c = int(input('Digite o segundo valor:'))
    mult = int(b*c)
    print('A multiplicação dos valores é: {}'.format(mult))
#Algo a se levar em conta é de sempre colocar a variavel que ira receber uma tipagem para se encaixar no algoritmo entre ().
if A == 4:
    b = int(input('Digite o primeiro valor:'))
    c = int(input('Digite o segundo valor:'))
    div = int(b/c)
    print('A divisão dos valores é: {}'.format(div))
#É relevante lembar que como utilizei a tipagem "int" todos valores seram inteiro e não quebrados.

