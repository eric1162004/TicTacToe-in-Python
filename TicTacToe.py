import random

class TicTacToe:

    def __init__(self):
        self.board = [' ' for x in range(9)]

    def insertMoves(self, player, pos):
        self.board[pos] = player

    def spaceIsFree(self, pos):
        return self.board[pos] == ' '

    def isWinner(self, p, bo=None):
        if bo == None:
            bo = self.board

        return \
            (bo[0] == p and bo[1] == p and bo[2] == p) or\
            (bo[3] == p and bo[4] == p and bo[5] == p) or\
            (bo[6] == p and bo[7] == p and bo[8] == p) or\
            (bo[0] == p and bo[3] == p and bo[6] == p) or\
            (bo[1] == p and bo[4] == p and bo[7] == p) or\
            (bo[2] == p and bo[5] == p and bo[8] == p) or\
            (bo[0] == p and bo[4] == p and bo[8] == p) or\
            (bo[2] == p and bo[4] == p and bo[6] == p)

    def playerMove(self, pos):
        if self.spaceIsFree(pos):
            self.insertMoves('X', pos)
            return pos
        else:
            return -1

    @classmethod
    def selectRandom(cls, _list):
        _len = len(_list)
        index = random.randrange(0,_len)
        return _list[index]

    def computeMove(self):
        possibleMoves = [index for index, box in enumerate(self.board) if box == ' ']
        move = -1

        # pick the next move that will allow the computer to win
        # or pick the next move that will allow the player to win
        for p in ['O','X']:
            for move in possibleMoves:
                boardCopy = self.board[:] # making a clone of board
                boardCopy[move] =  p
                if self.isWinner(p, boardCopy):
                    return move

        # pick any available corners
        cornersOpen = []
        for i in possibleMoves:
            if i in [0,2,6,8]:
                cornersOpen.append(i)

        if len(cornersOpen) > 0:
            move = TicTacToe.selectRandom(cornersOpen)
            return move

        # pick the center if it is available
        if 4 in possibleMoves:
            move = 4
            return move

        # pick any available edges
        edgesOpen = []
        for i in possibleMoves:
            if i in [1,3,5,7]:
                edgesOpen.append(i)

        if len(edgesOpen) > 0:
            move = TicTacToe.selectRandom(edgesOpen)

        return move

    def isBoardFull(self):
        return False if self.board.count(' ') > 0 else True

    def resetBoard(self):
        for i, j in enumerate(self.board):
            self.board[i] = ' '

    def getBoard(self):
        return self.board