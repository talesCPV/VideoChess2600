import move_pos as mvp
import copy
import random

def main_ai(tab):
    cpu_color = 'P'
    plr_color = 'B'
    cpu = []
    plr = []
    cpu_pos = []
    plr_pos = []
    exit = []
    ataque = False
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

            if (len(risco[0][1]) > 1): # tem mais de uma peça te ameaçando?
                if (risco[0][0][2]>1): # A peça ameaçada não é um peão né?
                    print('corra para as montanhas!!!')
                    x_ = risco[0][0][0]  # montando o parâmetro 'list' de return_pos_list
                    y_ = risco[0][0][1]
                    if (len(runaway([x_, y_], tab)) > 0):# Vai para runaway e devolve a casa que deve ir
                        print('movimento...', (x_, y_), runaway([x_, y_], tab))
                        mvp.jogada_cpu((x_, y_), runaway([x_, y_], tab), tab)
                        ataque = False
                        break
                    else:
                        print('já era essa peça, vamos pensar no ataque')
                        ataque = True
                else:
                    print('abandonar o peão pra morrer, coitado')
                    print(' vamos pensar no ataque...')
                    ataque = True

            else:
                print('Da pra contra atacar?')
                pos_enemy = (risco[0][1][0][0],risco[0][1][0][1])
                aux_2 = check_risk(pos_enemy,cpu_pos)
                if (len(aux_2)>0): # sim, da pra contra atacar
                    print('Sim, da pra contra atacar')
                    x_ = aux_2[1][0][0]
                    y_ = aux_2[1][0][1]
                    exit.append(((x_, y_),(aux_2[0])))
                    mvp.jogada_cpu((x_,y_),aux_2[0],tab)
#                    main.turn = 'B'
                    print('Jogada executada', exit)
                    ataque = False
                    break
                else:
                    print('não da pra contra atacar =(')
                    if (risco[0][0][2] > 1):  # A peça ameaçada não é um peão né?
                        print('da pra fugir?...', x[0], x[1])
                        run = runaway([x[0], x[1]], tab)
                        if (len(run) > 0):
                            print('da sim...', run)
                            mvp.jogada_cpu((x[0], x[1]), run, tab)
                            ataque = False
                            break
                        else:
                            print('vish, não da pra fugir não... bora atacar')
                            ataque = True

                    else:
                        print('já era um peão, bora pensar no ataque')
                        ataque = True
        else:
            ataque = True

    if ataque:
        strike(cpu_pos,tab)

    print('*****  Fim main  *****')

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
#            print('')
            if (casa[0] == sub[0] and casa[1] == sub[1]):
                list[1].append(([pos[1],pos[2],pos[4]]))

    if not(len(list[1])> 0):
        while len(list)>0:
            list.remove(list[0])
    return list

def runaway(peca,tab):
    print('runway!!!')
    x = peca[0]
    y = peca[1]
    cor = tab[y][x][0]
    peca = tab[y][x][1]
    list = []
    list.append([x, y, (cor, peca)])  # cria a lista para parâmetro de return_pos_list
    list = return_pos_list(list, tab)  # uso a mesma variável list_ para pegar o resultado da função
    #faltou ver se este local é seguro
    pos_ok = []
    escolha = []
    if len(list)>0: # a lista não esta zerada?
        for aux in list[0][0]:
            if simula_jogada(tab,((x,y),aux)):
                pos_ok.append(aux)
        if len(pos_ok)> 0:
            escolha = pos_ok[0]
            for aux in pos_ok:
                if tab[aux[1]][aux[0]][0] == 'B':
                    escolha = aux

    return escolha


def simula_jogada(tab,jogada):
    new_tab = copy.deepcopy(tab)
    resp = True
    x1 = jogada[0][0]
    y1 = jogada[0][1]
    x2 = jogada[1][0]
    y2 = jogada[1][1]
    new_tab[y2][x2] = new_tab[y1][x1]
    new_tab[y1][x1] = (' ',' ')
    brancas = []
    for y in range(8):
        for x in range(8):
            if new_tab[y][x][0] == 'B':
                brancas.append([x,y,new_tab[y][x]])

    new_reach = return_pos_list(brancas,new_tab)
    for x in new_reach:  # existe risco?
        for y in x[0]:
            if (x2 == y[0] and y2 == y[1]):
                resp = False
    return resp

def ataque_seguro(cpu_pos, tab): #verifica se pode comer alguma peça adversária e se é seguro
    print('ataque seguro!!!')
    resp = True
    jog = []
    for x in cpu_pos:
        for y in x[0]: # varre jogadas
            if (tab[y[1]][y[0]][0] == 'B'): # # posso abater uma peça inimiga?
                jog.append([(x[1],x[2]),y]) # adiciona jogada na lista

    if len(jog)>0: # lista de jogadas de ataque é maior q 0?
        for x in jog:
            if (simula_jogada(tab,x)): # esta jogada é segura?
                mvp.jogada_cpu(x[0],x[1], tab)
                resp = False
                break
            else:
                resp = True
    return resp

def strike(cpu_pos, tab):
    print('Strike!!!')
    if ataque_seguro(cpu_pos,tab): # verifica se posso comer alguma peça adversária, se sim faz a jogada e retorna false
        print('ataque')
        peoes = []
        pecas = []
        for x in cpu_pos:
            for y in x[0]: # varre jogadas (separa peças de peoes)
                if simula_jogada(tab,[(x[1],x[2]),y]):
                    if x[4] == 'p':
                        peoes.append([(x[1], x[2]), y])
                    else:
                        pecas.append([(x[1], x[2]), y])

        if (len(pecas) <= 10 and len(peoes) > len(pecas)): # temos poucas opções de jogadas? vamos abrir os peoes
            print('vamos de peão')
            J = peoes[random.randint(0,len(peoes))] # sorteia uma jogada de peão qualquer
            mvp.jogada_cpu(J[0],J[1], tab)
        else:
            print('vamos de peças')
            max = 0
            for index,x in enumerate(pecas):
                print(x)
                if x[1][0] > pecas[max][1][1]:
                    max = index
                    print('max',x[1][0])
            if len(pecas)>0:
                print(pecas[max])
                mvp.jogada_cpu(pecas[max][0],pecas[max][1], tab)
            else:
                print('sem jogadas seguras...',len(pecas),len(peoes))
