import pygame
import move_pos as mvp
import move_ai as mai
from pygame.locals import *
import os

############ VARIÁVEIS ###########
turn = 'B'
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
render = False
pygame.init()
screen = pygame.display.set_mode((540,540), 0, 32)
background = pygame.image.load('board.png').convert()
pieces = pygame.image.load('pieces.png').convert_alpha()
icon = pygame.image.load(os.getcwd() + '\icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Video Chess 2600')

######### FUNÇÕES ##########

def get_pieces(param): # recebe a cor e a peça e retorna a localização em pixels dentro de "pieces.png"
    x = 0
    y = 0
    color = param[0]
    kind  = param[1]
    if (color == 'P'): # cor preta? linha 2
        y += 62

    if   kind == 'R': # torre - Rook
        x = 0
    elif kind == 'H': # cavalo - Horse
        x += 62
    elif kind == 'B': # bispo - Bishop
        x += 124
    elif kind == 'Q': # dama - Queen
        x += 186
    elif kind == 'K': # rei - King
        x += 248
    else:
        x += 310  # peão - pawn
    return (x, y)

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



def possibilites(pos): # checa as possibilidades de movimento de cada peça
    while len(pos)>0:
        pos.remove(possible[0])
    x = click[0]
    y = click[1]
    cor = tabuleiro[y][x][0]
    peca = tabuleiro[y][x][1]
    pos += mvp.choose_op(x,y,cor,peca,tabuleiro)
    return pos

def mouse_click(pos):
    global turn
    x = get_cord_pos(pos)[0]
    y = get_cord_pos(pos)[1]
    if len(click)>0:
        xy = (click[0],click[1]) #guarda o valor anterior de click
        if mvp.jogada_plr(xy,[x,y],possible,tabuleiro): # Se teve movimento, muda a vez do jogador
#            if turn == 'B':
#                turn = 'P'
             mai.main_ai(tabuleiro)
#            else:
#                turn = 'B'
        while len(click)>0: # zera o vetor click
            click.remove(click[0])
    click.append(x)
    click.append(y)
    if (tabuleiro[y][x][0] == 'B'):# qualquer uma joga agora... #   turn): # se for a vez da cor selecionada, ver possibilidades
        possibilites(possible)
    else:
        while len(possible)>0: # zera o vetor possible
            possible.remove(possible[0])

def draw_square(): # desenha os quadrados na tela
    for pos in possible:# desenha os quadrados das possibilidades
        x = pos[0]*64+15
        y = pos[1]*64+15
        pygame.draw.rect(screen, (0, 255, 0), [x,y] + [64, 64], 5)
    if len(click)>0: # desenha o quadrado do click
        x = click[0]*64+15
        y = click[1]*64+15
        pygame.draw.rect(screen, (255,0,0), [x,y]+[64, 64],5)


def fill_board(): # enche o tabuleiro com as peças
    global render
    for x in range (8):
        for y in range (8):
            if not(tabuleiro[y][x][1].strip() ==  ''):
                xy =  [x*64+15, y*64+15] # monta x e y no screen (15 é o valor da borda e 64 o valor de cada casa em pixels)
                screen.blit(pieces, xy, get_pieces(tabuleiro[y][x]) + (62, 62))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:
            render = False
            mouse_click(pygame.mouse.get_pos())


    if not render:
        pieces = pygame.transform.scale(pieces, (372, 124))
        screen.fill([0, 100, 255])
        screen.blit(background, (15, 15))
        fill_board()
        draw_square()
        pygame.display.update()
        render = True