#Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada

variavel = input(str('Digite uma palavra: '))

def func():
    return variavel 
def func2():
    return func()
executando = func2()
print(executando)