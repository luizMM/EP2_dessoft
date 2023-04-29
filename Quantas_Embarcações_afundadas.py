def afundados(frota, tabuleiro):
    afundados = 0

    for navio, posicoes in frota.items():
        for posicao in posicoes:
            afundado = True
            for coordenada in posicao:
                x, y = coordenada
                if tabuleiro[x][y] != 'X':
                    afundado = False
                    break
            if afundado:
                afundados += 1

    return afundados
