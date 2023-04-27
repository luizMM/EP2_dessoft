def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]  # Cria um tabuleiro vazio de 10x10
    
    for navio, posicoes in frota.items():
        for coordenadas in posicoes:
            for linha, coluna in coordenadas:
                tabuleiro[linha][coluna] = 1  # Marca a posição com um navio
    
    return tabuleiro
