# VideoChess2600
Logic for computer play chess against a human being

I divide the logic in 3 layers:

1) Graphic:
  In this layer we:
    Import pygame
    Open the 540x540 screen
    Open image 'board.png' in the background
    Open image 'pieces.png' in alpha (this image get all the pieces we use)
    Open image 'icon.png' for use just for icon
    Set screen caption
    Here we have some important functions:
      Fill Board:
        This function get the list 'tabuleiro' and put every piece on the corect position on the board
        ** The list tabuleiro is a matrix 8x8 the contain a little list inside with the color and what piece is in it

