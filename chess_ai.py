import chess_move as chess_move

tab = []
language = [['R','H','B','Q','K','p'],['B','P']]

def get_move(lit,board):
    global tab
    tab = board
    lit_to_index(lit)


def lit_to_index(lit): # convert literal from index to tab
    print(lit)
    resp = []
    try:
        if lit[-2] == '-': # roque
            print('roque')
        else:
            pos2 = lit[-2:]
            x2 = ord(pos2[-2])-97
            y2 = 8-int(pos2[-1])
            color = lit[0]
            if len(lit) == 3:
                piece = 'p'
            else:
                piece = lit[1]

            list_parts = search_piece(color,piece)
            print(list_parts)
            for x in list_parts:
                lit_aux = (chr(97+ x[0]) + str(8 - x[1])) # transform in literal
                print(lit_aux)
                ind_aux = chess_move.move(lit_aux,tab)
                for y in ind_aux:
                    if (x2 == y[0] and y2 == y[1] ):
                        resp.append([x,(x1,y2)])
                        print('resp =',x,(x2,y2))
                        break


            chess_move.move(lit,tab)
            print(x2,y2,color,piece)
    except:
        resp = []
    print(resp)
    return resp

def search_piece(color, piece):
    resp = []
    for y in range(8):
        for x in range(8):
            if (tab[y][x][0] == color and tab[y][x][1] == piece):
                resp.append([x,y])
    return resp