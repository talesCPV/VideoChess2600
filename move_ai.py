import move_pos as mvp

def main_ai(tab):
    cpu_color = 'P'
    plr_color = 'B'
    cpu = []
    plr = []
    cpu_pos = []
    plr_pos = []
    for y in range(8):
        for x in range(8):
            if tab[y][x][0] == cpu_color:
                cpu.append([x,y,tab[y][x]])
            if tab[y][x][0] == plr_color:
                plr.append([x,y,tab[y][x]])

    cpu_pos += return_pos_list(cpu, tab)
    plr_pos += return_pos_list(plr, tab)

    risco = []
    for x in cpu:
        aux = check_risk((x[0],x[1],import_degree(x[2][1])), plr_pos)
        if len(aux) > 0:
            risco.append(aux)
#    print(reorganiza_lista_risco(risco)) # lista de risco já organizada por prioridade de analise
    reorganiza_lista_risco(risco)
    print(risco)

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
    print('github!!!')

    return list
