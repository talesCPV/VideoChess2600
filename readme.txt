          ************VIDEO CHESS 2600****************

	L� pelo final dos anos 80 eu era um garoto apaixonado 
por Xadrez, jogava as vezes com meu pai mas na maioria do tempo
n�o tinha com quem jogar. Nesta �poca eu tinha um Atari 2600
e quando descobri que existia um jogo de xadrez que eu poderia
jogar contra o computador foi o m�ximo, me lembro de quando venci
minha primeira partida contra a m�quina, aquilo me fez me achar
o melhor jogador de xadrez do mundo, mas no fundo eu j� me perguntava:
Como uma m�quina pode jogar xadrez? Qual o algor�timo que rodava por
de tr�s das jogadas? Aquele tempo que demorava entre as jogadas do
computador ele estava realmente "pensando"?
	Hoje existem milhares de algor�timos que jogam xadrez, alguns
at� com IA, mas eu resolvi criar o meu pr�prio algor�timo a fim de 
praticar um pouco de programa��o e aproveitar para me divertir no 
processo. Para efetuar tal desafio eu escolhi a linguagem Python, por
ser altamente port�vel para outras plataformas.Ent�o vamos a 
organiza��o do c�digo, dividi em 3 camadas principais:

1) GR�FICA:
	*Pygame
	*Abre a imagem 'board.png' na tela
	*Recorta a imagem 'pieces.png' (sprites das pe�as do jogo)
	*Monta a lista tabuleiro na tela (posi��es das pe�as no tabuleiro)
	*Posiciona o cursor no tabuleiro no evento onClick do mouse
	***** CHAMA A SEGUNDA CAMADA "POSSIBILIDADES"

2) POSSIBILIDADES:
	*Recebe as coordenadas do click no tabuleiro
	*Analisa e cria uma lista as op��es de movimentos
	 poss�veis para pe�a selecionada
	*Se o segundo click for em uma casa poss�vel, efetua
	 o movimento da pe�a

3) INTELIG�NCIA ARTIFICIAL
	*Cria listas com localiza��o das pe�as


