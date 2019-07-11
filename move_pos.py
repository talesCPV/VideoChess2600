
def jogada_plr(pos1, pos2,possible, tab):
    resp = False
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    for pos in possible:
        x_pos = pos[0]
        y_pos = pos[1]
        if (x2 == x_pos and y2 == y_pos):
            print('move', pos1, pos2)
            if (tab[y1][x1][1] == 'K' and max(x1,x2)- min(x1,x2) > 1): # roque
                if tab[y2][x2 -1][1] == 'R':
                    print('Roque longo!!!')
                    tab[y2][x2 + 1] = (tab[y2][x2 -1][0],tab[y2][x2 -1][1])
                    tab[y2][x2 - 1] = (' ',' ')
                elif tab[y2][x2 +1][1] == 'R':
                    print('Roque curto!!!')
                    tab[y2][x2 - 1] = (tab[y2][x2 +1][0],tab[y2][x2 +1][1])
                    tab[y2][x2 + 1] = (' ',' ')

            tab[y2][x2] = tab[y1][x1]
            tab[y1][x1] = (' ',' ')

            resp = True
    return resp

def jogada_cpu(pos1,pos2,tab):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]

    tab[y2][x2] = tab[y1][x1]
    tab[y1][x1] = (' ', ' ')
    print('jogada',x1,y1,' - ',x2,y2)

