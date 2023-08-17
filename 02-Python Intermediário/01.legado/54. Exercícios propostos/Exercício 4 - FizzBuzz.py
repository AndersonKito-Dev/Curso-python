"""- Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado."""

from random import randint

#Minha forma
def FizzBuzz(número):
    if número % 5 == 0 and número % 3 == 0: print('FizzBuzz')
    if número % 3 == 0: print('Fizz')
    if número % 5 == 0: print('Buzz')
    else: print(número)
FizzBuzz(randint(0, 100))

"""
#Resolução do professor
def FizzBuzz(número):
    if número % 5 == 0 and número % 3 == 0: return 'FizzBuzz'
    if número % 3 == 0: return'Fizz'
    if número % 5 == 0: return'Buzz'
    return número
resposta = FizzBuzz(randint(0,100))
print(resposta)
"""