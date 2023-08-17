"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # N tem
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],  # tem
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],  # tem
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],  # tem
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],  # tem
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],  # tem
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],  # tem
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],  # tem
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],  # tem
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],  # tem
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],  # tem
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  # N tem
]


def duplicado(l):
    s1 = set()
    passagens = 0
    flag = 0

    for numero in l:
        passagens += 1

        if numero in s1:
            return numero

        if passagens == 10 and flag == 0:
            return -1

        s1.add(numero)

################

# Mudanças ao ver a resolução do prof


def dup(l):
    num_checados = set()
    num_duplicado = -1

    for numero in l:

        if numero in num_checados:
            num_duplicado = numero
            break

        num_checados.add(numero)

    return num_duplicado


######

# Isso é só pra mostrar no terminal
for lista in lista_de_listas_de_inteiros:
    print(f'{duplicado(lista)}\n')
    print(f'{dup(lista)}\n')
