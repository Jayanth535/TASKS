from random import randrange
 
def display_board(board):
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[0][0]+    '   |   ' +board[0][1] +   '   |   ' +board[0][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[1][0]+    '   |   ' +board[1][1] +   '   |   ' +board[1][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+\n','|       |       |       |\n',
          '|   ' +board[2][0]+    '   |   ' +board[2][1] +   '   |   ' +board[2][2] +   '   |\n','|       |       |       |',)
    print(' +-------+-------+-------+')
board=[['1','2','3'],['4','X','6'],['7','8','9']]
display_board(board)