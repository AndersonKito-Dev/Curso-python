"""
49. Desafio - Valide um CPF  //  Código para validar se o CPF é válido ou não
"""
while True:
    cpf = input('Digite seu CPF: ')
    cpf = cpf.replace('.', '') .replace('-', '')
    cpf_lista = list(cpf)

    if cpf.isnumeric():
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
                resultado = int(
                    cpf_lista[multiplicações_feitas_2]) * multiplicador
                multiplicações_feitas_2 += 1
                soma_2 += resultado
            digito_2 = 11 - (soma_2 % 11)  # Determinar o último número do CPF
            if digito_2 == int(cpf_lista[10]):
                print('CPF validado!')
                break
            else:
                print('CPF inválido!')
                break
        else:
            print('CPF inválido!')
            break
    else:
        print('ERROR')
        resposta_usuario = str(
            input('Digite "T" para tentar novamente e "sair" para sair: '))
        if resposta_usuario == 'T' or resposta_usuario == 't':
            continue
        else:
            break
