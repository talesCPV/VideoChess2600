
'''
    chess_move:
        call: move(lit, tabuleiro)
            where: lit
                        -> String
                        -> position on board, ex: 'a2' or move, like BHc6, where B is color and H is piece
                   tabuleiro
                        -> matrix (8x8) of list with 2 Strings, first represent the color and second the piece
                        -> represent pieces on board, ex: [[('B','H'),('B','K'),...],
                                                           [(' ',' '),('P','B'),...],
                                                           ...]
        return: list of possible moves, ex: ((x1,y1),(x2,y2),...)
        IMPORTANT:
            set language:
                the variable language can be change by user, this var represents the first letter of each piece on tab and  which color is this
                ex: language = [['R','H','B','Q','K'],['B','P']]
                    [ # pieces
                    -> R = roque
                    -> H = horse
                    -> B = bishop
                    -> Q = queen
                    -> K = king
                    ],[ # colors
                    -> B = branco
                    -> P = preto
                    ]
'''

tab = []
language = [['R','H','B','Q','K','p'],['B','P']]

def move(lit,board):

    global tab
    tab = board
    try:
        x = ord(lit[-2])-97
        y = 8-int(lit[-1])
        color = tab[y][x][0]
        piece = tab[y][x][1]
    except:
        print('error!!!')
        piece = ''
        color = ''
        x = 0
        y = 0
    resp = []

    if piece == language[0][5]: # PEÃO
        resp += pawn_op(x,y,color)

    elif piece == language[0][0]: #TORRE
        resp += rook_op(x,y,color)

    elif piece == language[0][1]: # CAVALO
        resp += horse_op(x,y,color)

    elif piece == language[0][2]: # BISPO
        resp += bishop_op(x,y,color)

    elif piece == language[0][3]: #RAINHA
        resp += rook_op(x,y,color)
        resp += bishop_op(x,y,color)

    elif piece == language[0][4]: #REI
        resp += king_op(x,y,color)

#    print(resp)
    return resp

def horse_op(x,y,color):
    list = []
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
                if not (tab[y1][x1][0] == color):  # existe uma peça sua no local?
                    list.append((x1, y1))

            x1 = x + 1 * a
            y1 = y + 2 * b
            if (x1 >= 0 and x1 <= 7) and (y1 >= 0 and y1 <= 7):  # a posição desejada esta dentro do tabuleiro?
                if not (tab[y1][x1][0] == color):  # existe uma peça sua no local?
                    list.append((x1, y1))
    return list

def bishop_op(x,y,color):
    lista = []

    if color == 'P':
        enemy_color = 'B'
    else:
        enemy_color = 'P'

    i = 1
    while (x + i < 8 and y + i < 8):  # enquanto x não chega a estremidade direita e superior
        if not (tab[y + i][x + i][0] == color):
            lista.append(((x + i),(y + i)))
            if (tab[y + i][x + i][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x + i < 8 and y - i >= 0):  # enquanto x não chega a estremidade direita e inferior
        if not (tab[y - i][x + i][0] == color):
            lista.append(((x + i),(y - i)))
            if (tab[y - i][x + i][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x - i >= 0 and y + i < 8):  # enquanto x não chega a estremidade esquerda e superior
        if not (tab[y + i][x - i][0] == color):
            lista.append(((x - i), (y + i)))
            if (tab[y + i][x - i][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x - i >= 0 and y - i >= 0):  # enquanto x não chega a estremidade esquerda e inferior
        if not (tab[y - i][x - i][0] == color):
            lista.append(((x - i),(y - i)))
            if (tab[y - i][x - i][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    return lista

def rook_op(x,y,color):
    list = []

    if color == 'P':
        enemy_color = 'B'
    else:
        enemy_color = 'P'

    i = 1
    while (x + i < 8):  # enquanto x não chega a estremidade direita
        if not (tab[y][x + i][0] == color):  # existe uma peça sua no local?
            list.append(((x + i),(y)))
            if (tab[y][x + i][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while (x - i >= 0):  # enquanto x não chega a extremidade esquerda
        if not (tab[y][x - i][0] == color):  # existe uma peça sua no local?
            list.append(((x - i),(y)))
            if (tab[y][x - i][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1

    i = 1
    while y + i < 8:  # enquanto y não chega a extremidade superior
        if not (tab[y + i][x][0] == color):  # existe uma peça sua no local?
            list.append((x , (y + i)))
            if (tab[y + i][x][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1
    i = 1
    while y - i >= 0:  # enquanto y não chega a extremidade inferior
        if not (tab[y - i][x][0] == color):  # existe uma peça sua no local?
            list.append((x,(y - i)))
            if (tab[y - i][x][0] == enemy_color):  # existe uma peça inimiga no local?
                break
        else:
            break
        i += 1

    return list

def pawn_op(x,y,color):
    list = []
    if color == 'P':
        upside = -1
        enemy_color = 'B'
    else:
        upside = 1
        enemy_color = 'P'
    if (y - upside >= 0 and y - upside <= 7):
        if (tab[y - upside][x][0] == ' '):  # há algo na frente do peão?
            list.append((x, (y - upside)))
            if (color == 'B' and y == 6) or (color == 'P' and y == 1):  # é o primeiro moviimento do peão?
                if (tab[y - (upside * 2)][x][0] == ' '):  # existe uma peça sua na segunda casa?
                    list.append((x,(y - (upside * 2))))
        if x <= 6:  # pra não dar out of bounds no tabuleiro
            if (tab[y - upside][x+1][0] == enemy_color):  # a diagonal superior direita é peça inimiga?
                list.append(((x+1), (y - upside)))
        if x - 1 >= 0:  # pra não dar out of bounds no tabuleiro
            if (tab[y - upside][x - 1][0] == enemy_color):  # a diagonal superior esquerda é peça inimiga?
                list.append(((x - 1),(y - upside)))
    return list

def king_op(x,y,color):
    list = []
    for i in range(3):
        for o in range(3):
            if(x+1-i >= 0 and x+1-i <=7 and y+1-o >=0 and y+1-o <=7):
                if not(tab[y+1-o][x+1-i][0] == color):
                    list.append(((x+1-i),(y+1-o)))

    if (tab[7][4][1] == 'K' and tab[7][4][0] == 'B'): #Roque Branco
        if (tab[7][7][1] == 'R' and tab[7][7][0] == 'B'): # curto
            if (tab[7][5][0] == ' ' and tab[7][6][0] == ' '):
                list.append((6,7))
        if (tab[7][0][1] == 'R' and tab[7][0][0] == 'B'): # longo
            if (tab[7][1][0] == ' ' and tab[7][2][0] == ' ' and tab[7][3][0] == ' '):
                list.append((1,7))

    if (tab[0][4][1] == 'K' and tab[0][4][0] == 'P'): #Roque Preto
        if (tab[0][7][1] == 'R' and tab[0][7][0] == 'P'): # curto
            if (tab[0][5][0] == ' ' and tab[0][6][0] == ' '):
                list.append((6,0))
        if (tab[0][0][1] == 'R' and tab[0][0][0] == 'P'): # longo
            if (tab[0][1][0] == ' ' and tab[0][2][0] == ' ' and tab[0][3][0] == ' '):
                list.append((1,0))

    return list