
######## Possibilidades de movimento ###########

def choose_op(x,y,cor,peca,tab):
    lista = []
    if peca == 'p': # PEÃO
        lista += pawn_op(x, y, cor, tab)

    elif peca == 'R': #TORRE
        lista += rook_op(x, y, cor, tab)

    elif peca == 'H': # CAVALO
        lista += horse_op(x,y,cor, tab)

    elif peca == 'B': # BISPO
        lista += bishop_op(x, y, cor, tab)

    elif peca == 'Q': #RAINHA
        lista += rook_op(x, y, cor, tab)
        lista += bishop_op(x, y, cor, tab)

    elif peca == 'K': #REI
        lista += king_op(x, y, cor, tab)

    return lista

def horse_op(x,y,cor, tabuleiro):
    lista = []
    for i in range(2):
        if i % 2:
            a = 1
        else:
            a = -1
        for o in range(2):
            if o % 2:
                b = 1
            else:
                b = -1
            x1 = x + 2 * a
            y1 = y + 1 * b
            if (x1 >= 0 and x1 <= 7) and (y1 >= 0 and y1 <= 7):  # a posição desejada esta dentro do tabuleiro?
                if not (tabuleiro[y1][x1][0] == cor):  # existe uma peça sua no local?
                    lista.append((x1, y1))

            x1 = x + 1 * a
            y1 = y + 2 * b
            if (x1 >= 0 and x1 <= 7) and (y1 >= 0 and y1 <= 7):  # a posição desejada esta dentro do tabuleiro?
                if not (tabuleiro[y1][x1][0] == cor):  # existe uma peça sua no local?
                    lista.append((x1, y1))
    return lista

def bishop_op(x,y,cor, tabuleiro):
    lista = []

    if cor == 'P':
        conta_cor = 'B'
    else:
        conta_cor = 'P'

    i = 1
    while (x + i < 8 and y + i < 8):  # enquanto x não chega a estremidade direita e superior
        if not (tabuleiro[y + i][x + i][0] == cor):
            lista.append(((x + i),(y + i)))
            if (tabuleiro[y + i][x + i][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x + i < 8 and y - i >= 0):  # enquanto x não chega a estremidade direita e inferior
        if not (tabuleiro[y - i][x + i][0] == cor):
            lista.append(((x + i),(y - i)))
            if (tabuleiro[y - i][x + i][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x - i >= 0 and y + i < 8):  # enquanto x não chega a estremidade esquerda e superior
        if not (tabuleiro[y + i][x - i][0] == cor):
            lista.append(((x - i), (y + i)))
            if (tabuleiro[y + i][x - i][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x - i >= 0 and y - i >= 0):  # enquanto x não chega a estremidade esquerda e inferior
        if not (tabuleiro[y - i][x - i][0] == cor):
            lista.append(((x - i),(y - i)))
            if (tabuleiro[y - i][x - i][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    return lista

def rook_op(x,y,cor, tabuleiro):
    lista = []

    if cor == 'P':
        conta_cor = 'B'
    else:
        conta_cor = 'P'

    i = 1
    while (x + i < 8):  # enquanto x não chega a estremidade direita
        if not (tabuleiro[y][x + i][0] == cor):  # existe uma peça sua no local?
            lista.append(((x + i),(y)))
            if (tabuleiro[y][x + i][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x - i >= 0):  # enquanto x não chega a extremidade esquerda
        if not (tabuleiro[y][x - i][0] == cor):  # existe uma peça sua no local?
            lista.append(((x - i),(y)))
            if (tabuleiro[y][x - i][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1

    i = 1
    while y + i < 8:  # enquanto y não chega a extremidade superior
        if not (tabuleiro[y + i][x][0] == cor):  # existe uma peça sua no local?
            lista.append((x , (y + i)))
            if (tabuleiro[y + i][x][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while y - i >= 0:  # enquanto y não chega a extremidade inferior
        if not (tabuleiro[y - i][x][0] == cor):  # existe uma peça sua no local?
            lista.append((x,(y - i)))
            if (tabuleiro[y - i][x][0] == conta_cor):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1

    return lista

def pawn_op(x,y,cor, tab):
    lista = []
    if cor == 'P':
        upside = -1
        conta_cor = 'B'
    else:
        upside = 1
        conta_cor = 'P'
    if (y - upside >= 0 and y - upside <= 7):
        if (tab[y - upside][x][0] == ' '):  # há algo na frente do peão?
            lista.append((x, (y - upside)))
            if (cor == 'B' and y == 6) or (cor == 'P' and y == 1):  # é o primeiro moviimento do peão?
                if (tab[y - (upside * 2)][x][0] == ' '):  # existe uma peça sua na segunda casa?
                    lista.append((x,(y - (upside * 2))))
        if x <= 6:  # pra não dar out of bounds no tabuleiro
            if (tab[y - upside][x+1][0] == conta_cor):  # a diagonal superior direita é peça inimiga?
                lista.append(((x+1), (y - upside)))
        if x - 1 >= 0:  # pra não dar out of bounds no tabuleiro
            if (tab[y - upside][x - 1][0] == conta_cor):  # a diagonal superior esquerda é peça inimiga?
                lista.append(((x - 1),(y - upside)))
    return lista

def king_op(x,y,cor, tabuleiro):
    lista = []

    for i in range(3):
        for o in range(3):
            if(x+1-i >= 0 and x+1-i <=7 and y+1-o >=0 and y+1-o <=7):
                if not(tabuleiro[y+1-o][x+1-i][0] == cor):
                    lista.append(((x+1-i),(y+1-o)))

    return lista

def jogada(pos1, pos2,possible, tab):
    resp = False
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    for pos in possible:
        x_pos = pos[0]
        y_pos = pos[1]
        if (x2 == x_pos and y2 == y_pos):
            tab[y2][x2] = tab[y1][x1]
            tab[y1][x1] = (' ',' ')
            resp = True
    return resp
