def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes
                
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)

    for posicao in posicoes:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
    
    for navios in frota.values():
        for navio in navios:
            for posicao_navio in navio:
                if posicao_navio in posicoes:
                    return False
    
    return True