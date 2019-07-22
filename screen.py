'''
    screen:
        call: show(tab)
            where:
               tab
                -> matrix (8x8) of list with 2 Strings, first represent the color and second the piece
                -> represent pieces on board, ex: [[('B','H'),('B','K'),...],
                                                   [(' ',' '),('P','B'),...],
                                                    ...]
        return:
            Screen with represent the tab in the board.

        IMPORTANT:
            The files 'pieces.png' and 'icon.png' must be in the same directory
            where:
                pieces.png (792x264) {132x132 each piece} with alpha channel
                icon.png (256x256) with alpha channel

            set language:
                the variable language can be change by user, this var represents the first letter of each piece on tab and  which color is this
                ex: language = [['R','H','B','Q','K'],['B','P']]
                    [ # pieces
                    -> R = roque
                    -> H = horse
                    -> B = bishop
                    -> Q = queen
                    -> K = king
                    ],[ # colors
                    -> B = white
                    -> P = dark
                    ]
'''

import pygame
import os

click = [] # coordenadas x & y
possible = []
pygame.init()
language = [['R','H','B','Q','K','p'],['B','P']]
screen = pygame.display.set_mode((542,542), 0, 32)
pieces = pygame.image.load('pieces.png').convert_alpha()
pieces = pygame.transform.scale(pieces, (372, 124)) # escala
icon = pygame.image.load(os.getcwd() + '\icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Video Chess 2600')

def show(tab):
    screen.fill([0, 0, 0])
    draw_board()
    write_border()
    fill_board(tab)
    draw_square()
    pygame.display.update()

def draw_board(): # Desenha o tabuleiro na tela
    color = True
    dark = (185,122,87)
    white = (255,255,255)
    for y in range(8):
        color = not color
        for x in range(8):
            if color:
                pygame.draw.rect(screen, dark, [15+(64*x),15+(64*y)] + [64, 64], 0)
                color = False
            else:
                pygame.draw.rect(screen, white, [15+(64*x),15+(64*y)] + [64, 64], 0)
                color = True


def get_pieces(param): # recebe a cor e a peça e retorna a localização em pixels dentro de "pieces.png"
    x = 0
    y = 0
    color = param[0]
    kind  = param[1]
    if (color == language[1][0]): # cor preta? linha 2
        y = 0
    else:
        y += 62

    if   kind == language[0][0]: # torre - Rook
        x = 0
    elif kind == language[0][1]: # cavalo - Horse
        x += 62
    elif kind == language[0][2]: # bispo - Bishop
        x += 124
    elif kind == language[0][3]: # dama - Queen
        x += 186
    elif kind == language[0][4]: # rei - King
        x += 248
    else:
        x += 310  # peão - pawn
    return (x, y)

def write_border():
    font = pygame.font.SysFont("verdana", 14)
    color = (255, 255, 255)

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
