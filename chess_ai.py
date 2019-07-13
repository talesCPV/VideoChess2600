import chess_move as chess_move

tab = []
language = [['R','H','B','Q','K','p'],['B','P']]
index = []
cpu_color = ''
plr_color = ''

def get_move(lit,board): # lit = sistema algébrico longo, ex: ('b1','a3') -> Cavalo de b1 para casa a3
    global tab, index
    tab = board
    index = lit_to_index(lit)
    put_on_board(lit)
    colors()

def colors(): # define as cores do jogador e da CPU
    global cpu_color, plr_color
    plr_color = tab[index[1][1]][index[1][0]][0]
    for y in range(8):
        for x in range(8):
            if not(tab[y][x][0] == ' ') and not(tab[y][x][0] == plr_color):
                cpu_color = tab[y][x][0]
                break


def put_on_board(lit): # recebe os índices de tabuleiro e efetua a jogada
    moves = chess_move.move(lit[0],tab)
#    index = lit_to_index(lit)
    try:
        x1 = index[0][0]
        y1 = index[0][1]
        x2 = index[1][0]
        y2 = index[1][1]
        for i in moves:
            if i == (x2,y2):
                tab[y2][x2] = tab[y1][x1]
                tab[y1][x1] = (' ', ' ')
                print('->',x1,y1,' - ',x2,y2)
    except:
        print('jogada impossível')

def lit_to_index(lit): # converte notação algébrica longa para índices de tabuleiro, ex: ('b1','a3') -> ((1,7),(0,5))
    try:
        x0 = ord(lit[0][-2]) - 97
        y0 = 8 - int(lit[0][-1])  # transformo o literal destino em índice
        x1 = ord(lit[1][-2]) - 97
        y1 = 8 - int(lit[1][-1])  # transformo o literal destino em índice

        resp = ((x0,y0),(x1,y1))
    except:
        resp = []

    return resp

