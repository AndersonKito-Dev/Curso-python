#Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada; Faça a função1 executar duas funções q recebam um número diferente de argumentos

def mestra(func, *args,**kwargs):
    return func(*args,**kwargs)
def oi(nome):
    return f'Olá {nome}'
def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'
executando = mestra(saudacao, 'Anderson', 'Olá!')
print(executando)