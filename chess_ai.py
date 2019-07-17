import chess_move as chess_move
import copy

tab = []
language = [['R','H','B','Q','K','p'],['B','P']] #
cpu_color = ''
plr_color = ''
cpu_pos = []
plr_pos = []
cpu_reach = []
plr_reach = []
cpu_risk = []
plr_risk = []
game_stage = 1

def get_move(lit,board): # lit = sistema algébrico longo, ex: ('b1','a3') -> Cavalo de b1 para casa a3
    global tab
    tab = board
    if put_on_board(lit): # a jogada recebida pode ser efetuada?
        positions()
        reachs()
        check_risk()
        check_game_stage()
        defense()


#    print('Colors:',cpu_color,plr_color)
#    print('Positions:',cpu_pos,plr_pos)
#    print('Reachs:',cpu_reach,plr_reach)
#    print('Risk:',cpu_risk,plr_risk)


def put_on_board(lit):  # recebe os índices de tabuleiro e efetua a jogada
    index = lit_to_index(lit)
    moves = chess_move.move(lit[0], tab)
    colors(index)
    resp = True
    try:
        x1 = index[0][0]
        y1 = index[0][1]
        x2 = index[1][0]
        y2 = index[1][1]
        for i in moves:
            if i == (x2, y2):
                tab[y2][x2] = tab[y1][x1]
                tab[y1][x1] = (' ', ' ')
                print('->', x1, y1, ' - ', x2, y2)
                resp = True
                break
            else:
                resp = False
    except:
        print('jogada impossível')
        resp = False

    return resp

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

def colors(index): # define as cores do jogador e da CPU
    global cpu_color, plr_color
    plr_color = tab[index[0][1]][index[0][0]][0]
    for y in range(8):
        for x in range(8):
            if not(tab[y][x][0] == ' ') and not(tab[y][x][0] == plr_color):
                cpu_color = tab[y][x][0]
                break

def positions(): # Pega as posições das peças no tabuleiro (em índices)
    global cpu_pos, plr_pos
    while len(cpu_pos) > 0:  # zera o vetor cpu_pos
        cpu_pos.remove(cpu_pos[0])
    while len(plr_pos) > 0:  # zera o vetor plr_pos
        plr_pos.remove(plr_pos[0])

    for y in range(8):
        for x in range(8):
            if (tab[y][x][0] == cpu_color):
                cpu_pos.append((x,y))
            if (tab[y][x][0] == plr_color):
                plr_pos.append((x,y))

def reachs(): # Pega os lances possíveis de cada jogador (em índices)
    global cpu_reach, plr_reach
    while len(cpu_reach) > 0:  # zera o vetor cpu_reach
        cpu_reach.remove(cpu_reach[0])
    while len(plr_reach) > 0:  # zera o vetor plr_reach
        plr_reach.remove(plr_reach[0])

    for x in cpu_pos:
        lit =  chr(97+ x[0]) + str(8 - x[1])
        reach = (chess_move.move(lit,tab),lit)
        if len(reach[0]) > 0:
            cpu_reach.append(reach)
    for x in plr_pos:
        lit =  chr(97+ x[0]) + str(8 - x[1])
        reach = (chess_move.move(lit, tab), lit)
        if len(reach[0]) > 0:
            plr_reach.append(reach)

def check_risk(): # verifica qual peça esta sendo ameaçada por qual
    global cpu_risk, plr_risk
    while len(cpu_risk) > 0:  # zera o vetor cpu_risk
        cpu_risk.remove(cpu_risk[0])
    while len(plr_risk) > 0:  # zera o vetor plr_risk
        plr_risk.remove(plr_risk[0])

    for cpu in cpu_reach:
        for plr in plr_pos:
            for i in cpu[0]:
                if i == plr:
                    x_ = ord(cpu[1][-2]) - 97
                    y_ = 8 - int(cpu[1][-1])
                    _x = plr[0]
                    _y = plr[1]
                    plr_risk.append(((_x,_y, tab[_y][_x][1]),(x_, y_, tab[y_][x_][1])))
    if len(plr_risk)>0:
        plr_risk = risk_order(plr_risk)

    for plr in plr_reach:
        for cpu in cpu_pos:
            for i in plr[0]:
                if i == cpu:
                    x_ = ord(plr[1][-2]) - 97
                    y_ = 8 - int(plr[1][-1])
                    _x = cpu[0]
                    _y = cpu[1]
                    cpu_risk.append(((_x,_y, tab[_y][_x][1]),(x_, y_, tab[y_][x_][1])))
    if len(cpu_risk)>0:
        cpu_risk = risk_order(cpu_risk)

def risk_order(risk): # organiza o risco por ordem de peças ameaçadas (Rei, Dama, Cavalo, Bispo, Torre, Peão
    resp = []
    for i in range(6):
        for x in risk:
            if (i == 0 and x[0][2] == language[0][4]):
                resp.append(x)
            if (i == 1 and x[0][2] == language[0][3]):
                resp.append(x)
            if (i == 2 and x[0][2] == language[0][1]):
                resp.append(x)
            if (i == 3 and x[0][2] == language[0][2]):
                resp.append(x)
            if (i == 4 and x[0][2] == language[0][0]):
                resp.append(x)
            if (i == 5 and x[0][2] == language[0][5]):
                resp.append(x)

    return resp

def check_game_stage():
    global game_stage
    if cpu_color == language[1][1]:
        base_line = 0
    else:
        base_line = 7

    roque = []
    for x in range(8):

        if (tab[base_line][x][0] == cpu_color):
            if tab[base_line][x][1] == language[0][1]: # Já desenvolveu os cavalos?
                game_stage = 1
            elif tab[base_line][x][1] == language[0][2]: # Já desenvolveu os bispos?
                game_stage = 1
            elif tab[base_line][x][1] == language[0][3]: # Já desenvolveu a dama?
                game_stage = 1
            elif tab[base_line][x][1] == language[0][0]: # Achou uma torre? guarde a posição dela
                roque.append((x,base_line))

        if len(roque) > 1: # achou 2 torres
            #print(roque)
            roq_1 = chr(97+ roque[0][0]) + str(8 - roque[0][1])
            roq_2 = chr(97+ roque[1][0]) + str(8 - roque[1][1])
            roq_1 = chess_move.move(roq_1 ,tab)
            roq_2 = chess_move.move(roq_2 ,tab)
            conect = 0
            for x in roq_1:
                for y in roq_2:
                    if x == y:
                        conect += 1
            if conect > 1  or roque[1][0] - roque[0][0] <= 1 : # as torres estão conectadas?
                game_stage = 2
            else:
                game_stage = 1
        else:
            game_stage = 2

    #print(game_stage)

def defense():
    if len(cpu_risk)>0:
        resp = True
        if cpu_risk[0][0][2] == language[0][4]: # A CPU esta em cheque?
            print('check scape ->',check_scape())
        else:
            print('Não estamos em cheque, mas temos peças ameaçadas')
#        for x in cpu_risk:
#            print(x)
    else:
        resp = False

    return resp

def check_scape(): # Como vamos sair de um cheque?
    print('Cheque!!!')
    threat = []
    resp = []
    king_pos = (cpu_risk[0][0][0],cpu_risk[0][0][1])
    king_move = chess_move.move_by_index(king_pos,tab)
    print('entrou king move',king_pos,king_move)

    for x in king_move: # opções de movimento do rei, descartadas as casas ameaçadas
        if not simulate((king_pos,x)):
            king_move.remove(x)

    for x in cpu_risk: # Quem são as ameaças?
        if x[0][2] == language[0][4]:
            threat.append(x[1])

    if len(threat)>1: # Existe mais de uma ameaça?
        if len(king_move) == 0: # Não temos casa pra fugir -> Cheque Matte
            print('Cheque matte')
            return []
        else:
            print('Fuga do rei')
            print(king_pos,king_move)

    else:
        for x in cpu_reach:
            for y in x[0]:
                if(y == (threat[0][0],threat[0][1])): # consigo matar a ameaça?
                    x1 = ord(x[1][-2]) - 97
                    y1 = 8 - int(x[1][-1])
                    if not((x1,y1) == king_pos):
                        resp = (x[1],chr(97+ y[0]) + str(8 - y[1]))
                        put_on_board(resp)
                        return resp
                    else:
                        if len(king_move)>0:
                            print('fuga', king_move) # fuga
                            if simulate((king_pos, king_move[0])): #Posso comer esta peça?
                                lit1 = chr(97 + king_pos[0]) + str(8 - king_pos[1])
                                lit2 = chr(97 + king_move[0][0]) + str(8 - king_move[0][1])
                                resp = (lit1,lit2)
                                if not put_on_board(resp):
                                    resp = []
                            else:
                                print('morri tbm')
                        else:
                            print('morri')

    return resp

def simulate(index):
    new_tab = copy.deepcopy(tab)
    new_plr_reach = []
    resp = True
    x1 = index[0][0]
    y1 = index[0][1]
    x2 = index[1][0]
    y2 = index[1][1]
    new_tab[y2][x2] = new_tab[y1][x1]
    new_tab[y1][x1] = (' ',' ')
    for y in range(8):
        for x in range(8):
            reach = chess_move.move_by_index((x,y),new_tab)
            if len(reach)>0:
                new_plr_reach.append(reach)


    for x in new_plr_reach:
        for i in x:
            if i == (x2,y2):
                resp = False

    return  resp