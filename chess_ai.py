import chess_move as chess_move

tab = []
language = [['R','H','B','Q','K','p'],['B','P']]

def lit_to_index(lit):
    print(lit)
    if lit[-2] == '-':
        print('roque')
    else:
        pos2 = lit[-2:]
        x2 = ord(pos2[-2])-97
        y2 = 8-int(pos2[-1])

        chess_move.move(pos2,tab)
        print(x2,y2)


def get_move(lit,board):
    global tab
    tab = board
    lit_to_index(lit)


