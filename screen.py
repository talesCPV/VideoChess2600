import pygame
import os

board = [[('P', 'R'), ('P', 'H'), ('P', 'B'), ('P', 'Q'), ('P', 'K'), ('P', 'B'), ('P', 'H'), ('P', 'R')],
       [('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p'), ('P', 'p')],
       [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
       [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
       [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
       [(' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' '), (' ', ' ')],
       [('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p'), ('B', 'p')],
       [('B', 'R'), ('B', 'H'), ('B', 'B'), ('B', 'Q'), ('B', 'K'), ('B', 'B'), ('B', 'H'), ('B', 'R')]]

click = [] # coordenadas x & y
possible = []
pygame.init()
screen = pygame.display.set_mode((540,540), 0, 32)
background = pygame.image.load('board.png').convert()
pieces = pygame.image.load('pieces.png').convert_alpha()
pieces = pygame.transform.scale(pieces, (372, 124)) # escala
icon = pygame.image.load(os.getcwd() + '\icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Video Chess 2600')

def show(tab):
    board =  tab
    screen.fill([0, 100, 255])
    screen.blit(background, (15, 15))
    fill_board(board)
    draw_square()
    pygame.display.update()

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

def write_border():
    font = pygame.font.SysFont("verdana", 14)
    color = (0, 0, 0)

    screen.blit(font.render("1", True, color),(3, 485))
    screen.blit(font.render("2", True, color),(3, 421))
    screen.blit(font.render("3", True, color),(3, 357))
    screen.blit(font.render("4", True, color),(3, 293))
    screen.blit(font.render("5", True, color),(3, 229))
    screen.blit(font.render("6", True, color),(3, 165))
    screen.blit(font.render("7", True, color),(3, 101))
    screen.blit(font.render("8", True, color),(3, 37))

    screen.blit(font.render("a", True, color),( 40, 524))
    screen.blit(font.render("b", True, color),(104, 524))
    screen.blit(font.render("c", True, color),(168, 524))
    screen.blit(font.render("d", True, color),(232, 524))
    screen.blit(font.render("e", True, color),(296, 524))
    screen.blit(font.render("f", True, color),(360, 524))
    screen.blit(font.render("g", True, color),(424, 522))
    screen.blit(font.render("h", True, color),(488, 524))

def draw_square(): # desenha os quadrados na tela
    for pos in possible:# desenha os quadrados das possibilidades
        x = pos[0]*64+15
        y = pos[1]*64+15
        pygame.draw.rect(screen, (0, 255, 0), [x,y] + [64, 64], 5)
    if len(click)>0: # desenha o quadrado do click
        x = click[0]*64+15
        y = click[1]*64+15
        pygame.draw.rect(screen, (255,0,0), [x,y]+[64, 64],5)

def fill_board(tab): # enche o tabuleiro com as peças
    for x in range (8):
        for y in range (8):
            if not(tab[y][x][1].strip() ==  ''):
                xy =  [x*64+15, y*64+15] # monta x e y no screen (15 é o valor da borda e 64 o valor de cada casa em pixels)
                screen.blit(pieces, xy, get_pieces(tab[y][x]) + (62, 62))
                write_border()
