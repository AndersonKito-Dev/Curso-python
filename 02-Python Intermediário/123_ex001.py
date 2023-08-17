questionario = [
    {
        'Pergunta': 'Qual a capital de Goiás?',
        'Opcoes': ['Goiania', 'São Paulo', 'Arapora', 'Florianopolis', 'Rio de Janeiro'],
        'Resposta': 'Goiania'
    },

    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opcoes': ['1', '2', '3', '4', '5'],
        'Resposta': '4'
    },

    {
        'Pergunta': 'Quanto é 5x5 ?',
        'Opcoes': ['20', '25', '30', '35', '30'],
        'Resposta': '25'
    },

    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opcoes': ['2', '3', '4', '5', '6'],
        'Resposta': '5'
    },

]

alternativas = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E'
}


def correspondencia():
    cont = 0
    for num in op:
        cont += 1
        if num == resp:
            return alternativas[cont]


acertos = 0

for i in range(len(questionario)):
    perg = questionario[i]['Pergunta']
    op = questionario[i]['Opcoes']
    resp = questionario[i]['Resposta']

    print(f'Pergunta: {perg} \n')
    print(
        f'Opções: \n A){op[0]} \n B){op[1]} \n C){op[2]} \n D){op[3]} \n E){op[4]} \n')

    escolha = str(input('Escolha uma opção: '))

    if escolha.upper() == correspondencia() or escolha.upper() == resp.upper():
        print('\nVocê acertou!! \n')
        acertos += 1
    else:
        print('\nVocê errou!! \n')

print(f'Você acertou {acertos} de {len(questionario)} perguntas.')
