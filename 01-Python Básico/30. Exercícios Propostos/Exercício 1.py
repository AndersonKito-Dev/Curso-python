NUM = input('Digite um número: ')

if NUM.isnumeric():
    num = int(NUM)
    if (num % 2) == 0:
        print('Esse número é par.')
    else:
        print('Esse número é ímpar.')
else:
    print('Sem números com vírgula ou letras amigão.')
