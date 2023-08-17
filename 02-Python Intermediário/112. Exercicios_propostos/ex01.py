# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor da variavel

numeros = list(map(int, input('Digita: ').split()))


def calc(*args):
    total = 1
    for i in args:
        total *= i
    return total


multi = calc(*numeros)
print(multi)
