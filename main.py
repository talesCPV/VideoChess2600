import pygame
import move_pos as mvp
import move_ai as mai
import chess_move as chess_move
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

def mouse_click(pos):
    global possible
    x = get_cord_pos(pos)[0]
    y = get_cord_pos(pos)[1]
    if len(click)>0:
        xy = (click[0],click[1]) #guarda o valor anterior de click
        if mvp.jogada_plr(xy,[x,y],possible,tabuleiro): # Se teve movimento, muda a vez do jogador
             mai.main_ai(tabuleiro)

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
            chess_ai.get_move('BHa3',tabuleiro)


    if render: # só renderiza a tela quando precisa
        screen.show(tabuleiro)
        render = False