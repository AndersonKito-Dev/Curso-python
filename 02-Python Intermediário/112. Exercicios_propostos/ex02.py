# Crie uma função fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

numero = int(input('Digite o número: '))


def analise(x):
    if x % 2 == 0:
        return 'Par'
    return 'Ímpar'


RESPOSTA = analise(numero)
print(RESPOSTA)
