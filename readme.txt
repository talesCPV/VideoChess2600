          ************VIDEO CHESS 2600****************

	Lá pelo final dos anos 80 eu era um garoto apaixonado 
por Xadrez, jogava as vezes com meu pai mas na maioria do tempo
não tinha com quem jogar. Nesta época eu tinha um Atari 2600
e quando descobri que existia um jogo de xadrez que eu poderia
jogar contra o computador foi o máximo, me lembro de quando venci
minha primeira partida contra a máquina, aquilo me fez me achar
o melhor jogador de xadrez do mundo, mas no fundo eu já me perguntava:
Como uma máquina pode jogar xadrez? Qual o algorítimo que rodava por
de trás das jogadas? Aquele tempo que demorava entre as jogadas do
computador ele estava realmente "pensando"?
	Hoje existem milhares de algorítimos que jogam xadrez, alguns
até com IA, mas eu resolvi criar o meu próprio algorítimo a fim de 
praticar um pouco de programação e aproveitar para me divertir no 
processo. Para efetuar tal desafio eu escolhi a linguagem Python, por
ser altamente portável para outras plataformas.Então vamos a 
organização do código, dividi em 3 camadas principais:

1) GRÁFICA:
	*Pygame
	*Abre a imagem 'board.png' na tela
	*Recorta a imagem 'pieces.png' (sprites das peças do jogo)
	*Monta a lista tabuleiro na tela (posições das peças no tabuleiro)
	*Posiciona o cursor no tabuleiro no evento onClick do mouse
	***** CHAMA A SEGUNDA CAMADA "POSSIBILIDADES"

2) POSSIBILIDADES:
	*Recebe as coordenadas do click no tabuleiro
	*Analisa e cria uma lista as opções de movimentos
	 possíveis para peça selecionada
	*Se o segundo click for em uma casa possível, efetua
	 o movimento da peça

3) INTELIGÊNCIA ARTIFICIAL
	*Cria listas com localização das peças


