# Crie funções que duplica, triplicam ou quadruplicam o número recebido

number1 = int(input('Digite um número: '))
number2 = int(input('Digite um número: '))


def mult(multiplier):
    def result(num):
        return multiplier * num
    return result


answer = mult(number1)
print(answer(number2))
