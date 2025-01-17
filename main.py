import pygame
import move_pos as mvp
import move_ai as mai
import chess_move as chess_move
import chess_ai as chess_ai
from pygame.locals import *
import screen as screen
import chess_ai as chess_ai

############ VARIÁVEIS ###########

tabuleiro = [[('P', 'R'), ('P', 'H'), ('P', 'B'), ('P', 'Q'), ('P', 'K'), ('P', 'B'), ('P', 'H'), ('P', 'R')],
            [('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p')],
            [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
            [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
            [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
            [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
            [('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p')],
            [('B', 'R'), ('B', 'H'), ('B', 'B'), ('B', 'Q'), ('B', 'K'), ('B', 'B'), ('B', 'H'), ('B', 'R')]]

click = [] # coordenadas x & y
possible = []
literal = ['','']
render = True

######### FUNÇÕES ##########

def get_cord_pos(pos): #recebe a localização em pixels e retorna a coordenada da casa clicada
    pos0 = pos[0]
    if pos[0] <15:
        pos0 = 15
    elif pos[0] > 527:
        pos0 = 526
    pos1 = pos[1]
    if pos[1] <15:
        pos1 = 15
    elif pos[1] > 527:
        pos1 = 526

    x = (pos0 - 15) // 64
    y = (pos1 - 15) // 64
    return [x, y]

def write_the_move(xy0,xy1): # recebe as coordenadas e retorna o literal, ex:
    x0 = xy0[0]
    y0 = xy0[1]
    x1 = xy1[0]
    y1 = xy1[1]
    lit0 = chr(97+ x0) + str(8 - y0)
    lit1 = chr(97+ x1) + str(8 - y1)

    resp = (lit0,lit1)
    return resp

def mouse_click(pos):
    global possible
    x = get_cord_pos(pos)[0]
    y = get_cord_pos(pos)[1]
    if len(click)>0:
        xy = (click[0],click[1]) #guarda o valor anterior de click
#        peca = tabuleiro[click[1]][click[0]][1]
#        for i in possible:
#            if (x == i[1] and y == i[0]):
#                print('movimento possível')
        for i in possible:
            if i == (x,y):
#                lit = tabuleiro[xy[1]][xy[0]][0] + tabuleiro[xy[1]][xy[0]][1] + lit
                chess_ai.get_move(write_the_move(xy,(x,y)),tabuleiro)
#                print('jogada ->',lit)
#                chess_ai.get_move(lit,tabuleiro)
#        print(possible)
#        if mvp.jogada_plr(xy,[x,y],possible,tabuleiro): # Se teve movimento, muda a vez do jogador
#             mai.main_ai(tabuleiro)

        while len(click)>0: # zera o vetor click
            click.remove(click[0])
    click.append(x)
    click.append(y)

    while len(possible) > 0:  # zera o vetor possible
        possible.remove(possible[0])

    if (tabuleiro[y][x][0] == 'B'):# qualquer uma joga agora... #   turn): # se for a vez da cor selecionada, ver possibilidades
        possible += chess_move.move(literal[1],tabuleiro)

    screen.click = click
    screen.possible = possible

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:
            render = True
            literal[0] = literal[1]
            literal[1] = (chr(97+ get_cord_pos(pygame.mouse.get_pos())[0]) + str(8 - get_cord_pos(pygame.mouse.get_pos())[1]))
            mouse_click(pygame.mouse.get_pos())

    if render: # só renderiza a tela quando precisa
        screen.show(tabuleiro)
        render = False