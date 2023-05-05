def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    if frota == {}:
        return False
    
    for navios in frota.values():
        for posicoes in navios:
            posicao = []
            if orientacao == "vertical":
                for i in range(tamanho):
                    posicao.append([linha + i, coluna])
                    if [linha, coluna] in posicoes:
                        return False
                return True
            elif orientacao == "horizontal":
                for i in range(tamanho):
                    posicao.append([linha, coluna + i])
                    if [linha, coluna] in posicoes:
                        return False
                return True