"""
51. Gerando CPFs com Python  //  Código para gerar e validar se o CPF é válido ou não
"""
from random import randint
while True:
    cpf = ''
    while True:  # Para sortear números e gerar um CPF
        numero = str(randint(0, 9))
        cpf += numero
        if len(cpf) == 11:
            break
    cpf_lista = list(cpf)
    soma_1 = 0
    multiplicações_feitas_1 = 0
    for multiplicador in range(10, 1, -1):
        resultado = int(cpf_lista[multiplicações_feitas_1]) * multiplicador
        soma_1 += resultado
        multiplicações_feitas_1 += 1
    digito_1: None  # Determinar o penúltimo número do CPF
    fórmula_1 = 11 - (soma_1 % 11)
    if fórmula_1 > 9:
        digito_1 = 0
    else:
        digito_1 = fórmula_1
    if digito_1 == int(cpf_lista[9]):
        soma_2 = 0
        multiplicações_feitas_2 = 0
        for multiplicador in range(11, 1, -1):
            resultado = int(cpf_lista[multiplicações_feitas_2]) * multiplicador
            multiplicações_feitas_2 += 1
            soma_2 += resultado
        digito_2 = 11 - (soma_2 % 11)  # Determinar o último número do CPF
        if digito_2 == int(cpf_lista[10]):
            trio_1 = ''.join([cpf_lista[0], cpf_lista[1], cpf_lista[2]])
            trio_2 = ''.join([cpf_lista[3], cpf_lista[4], cpf_lista[5]])
            trio_3 = ''.join([cpf_lista[6], cpf_lista[7], cpf_lista[8]])
            print(f'Seu CPF: {trio_1}.{trio_2}.{trio_3}-{digito_1}{digito_2}')
            break
        else:
            continue
    else:
        continue
