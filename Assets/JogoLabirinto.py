

PAREDE_HORIZONTAL = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
VAZIO = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|']
tabuleiro = [PAREDE_HORIZONTAL, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, PAREDE_HORIZONTAL]
PAREDE_INTERNA = '#'
PROBABILIDADE = 0.3
INICIO = 'I'
DESTINO = 'D'
# linhaInicio
# colunaInicio
# linhaDestino
# colunaDestino


for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro)):
        if j == 9:
            print("\n")
        else:
            print(tabuleiro[i][j])

