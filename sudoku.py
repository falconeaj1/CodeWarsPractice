import numpy as np
def done_or_not(board): #board[i][j]
  # your solution here
    npBoard = np.array(board)
    for i in range(9):
        if len(set(npBoard[i,:].flat)) < 9 or len(set(npBoard[:,i].flat)) < 9 or len(set(npBoard[int(i/3)*3:int(i/3)*3+3, (i%3)*3:(i%3)*3+3].flat)) < 9:
            return 'Try again!'
    return 'Finished!'