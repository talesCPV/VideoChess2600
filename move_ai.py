import move_pos as mvp


def main_ai(tab):
    cpu_color = 'P'
    plr_color = 'B'
    cpu = []
    plr = []
    cpu_pos = []
    plr_pos = []
    exit = []
    for y in range(8):
        for x in range(8):
            if tab[y][x][0] == cpu_color:
                cpu.append([x,y,tab[y][x]])
            if tab[y][x][0] == plr_color:
                plr.append([x,y,tab[y][x]])

    cpu_pos += return_pos_list(cpu, tab)
    plr_pos += return_pos_list(plr, tab)

    risco = []
    for x in cpu: # existe risco?
        aux = check_risk((x[0],x[1],import_degree(x[2][1])), plr_pos)
        if len(aux) > 0: # Sim, existe
            risco.append(aux)
            reorganiza_lista_risco(risco) # organiza por ordem de prioridade

            if (len(risco[0][1]) > 1):
                if (risco[0][0][2]>1):
                    print('corra para as montanhas!!!')
                else:
                    print('abandonar o peão pra morrer, coitado')
                # vai para corra para as montanhas, esta aqui só pra teste
                x_ = risco[0][0][0] #montando o parâmetro 'list' de return_pos_list
                y_ = risco[0][0][1]
                if (len(runaway([x_,y_],tab))>0):
                    mvp.jogada_cpu((x_, y_), runaway([x_,y_],tab)[0], tab)
                    print('não foi a jogada mais inteligente, se pudesse comer seria melhor')
            else:
                print('Da pra contra atacar?')
                pos_enemy = (risco[0][1][0][0],risco[0][1][0][1])
                aux_2 = check_risk(pos_enemy,cpu_pos)
                if (len(aux_2)>0):
                    x_ = aux_2[1][0][0]
                    y_ = aux_2[1][0][1]
                    exit.append(((x_, y_),(aux_2[0])))
                    mvp.jogada_cpu((x_,y_),aux_2[0],tab)
#                    main.turn = 'B'
                    print('Jogada executada', exit)
                    break


def return_pos_list(list, tab): # recebe uma lista de peças e retorna as posições alcançadas e por qual peça
    sub_list = []
    for pos in list:
        x = pos[0]
        y = pos[1]
        cor = pos[2][0]
        peca = pos[2][1]
        aux = mvp.choose_op(x, y, cor, peca, tab)
        if len(aux)>0:
            aux =  [aux]+ [x,y,cor,peca]
            sub_list += [aux]
    return sub_list

###############  DEFESA  ####################

def import_degree(peca):
    resp = 0
    if peca == 'K':
        resp = 5
    elif peca == 'Q':
        resp = 4
    elif peca == 'H':
        resp = 3
    elif peca == 'R' or peca == 'B':
        resp = 2
    elif peca == 'p':
        resp = 1
    return resp

def reorganiza_lista_risco(lista): #recebe uma lista de ameaças e retorna ela organizada por prioridades, (Rei, Dama, Cavalo, Bispo ou Torre, Peão)
    resp = []
    max = 0
    cont = 0
    index = 0
    while len(lista)>0:
        if lista[cont][0][2] > max:
            max = lista[cont][0][2]
            index = cont
        cont += 1
        if cont >= len(lista):
            resp.append(lista[index])
            lista.remove(lista[index])
            cont = 0
            index = 0
            max = 0
    lista += resp
    return resp

def check_risk(casa,lista):# checa o risco de deternimada casa e retorna uma lista de peças perigosas
    list = [casa,[]]
    for pos in lista:
        for sub in pos[0]:
            if (casa[0] == sub[0] and casa[1] == sub[1]):
                list[1].append(([pos[1],pos[2],pos[4]]))
#                list[1].append((pos))

    if not(len(list[1])> 0):
        while len(list)>0:
            list.remove(list[0])
    return list

def can_strike_back(peca,pos):
    x_ = peca[0]
    y_ = peca[1]

    for aux in pos:
        print(aux)

def runaway(peca,tab):
    print('runway!!!')
    resp = []
    x = peca[0]
    y = peca[1]
    cor = tab[y][x][0]
    peca = tab[y][x][1]
    list = []
    list.append([x, y, (cor, peca)])  # cria a lista para parâmetro de return_pos_list
    list = return_pos_list(list, tab)  # uso a mesma variável list_ para pegar o resultado da função
    #faltou ver se este local é seguro
    print('LIST ',list)

    for x in list[0][0]:
        if (tab[x[1]][x[0]][0].strip() == '' ): # casa vazia e segura
            resp.append(x)
            print('casa vazia', x[0],x[1])
    #falta priorizar comer a peça inimiga
    return resp


