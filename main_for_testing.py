from View import View
from TicTacToe import TicTacToe
import time

def main():

    V = View()
    Tic = TicTacToe()

    isQuit = False
    isPlayerturn = True

    while (isQuit == False):

        Tic.resetBoard()
        V.resetBoardView()  

        #gameturnLoop
        while not (Tic.isBoardFull()):
            move = -1

            if (isPlayerturn):
                if not (Tic.isWinner('O')): # if comp has not won 
                    while (move == -1):
                        mouse_pos = V.getPlayerResponse()
                        box_index = V.getClickedBox(mouse_pos) 

                        if V.isBoxClicked(box_index): # if the player has clicked a box
                            move = Tic.playerMove(box_index) # check if that box is available

                    V.drawImage(move, V.player_img)
                    isPlayerturn = not isPlayerturn
                else:
                    V.set_status_bar_text_and_countdown("Sorry, Computer's won this time!", 'red')
                    break

            if not (Tic.isWinner('X')): # if player has not won 
                move = Tic.computeMove()

                if move == -1:
                    V.set_status_bar_text_and_countdown("Tie Game! Try Again.")
                    break 
                else:
                    V.pauseComp(1)
                    Tic.insertMoves('O', move)
                    V.drawImage(move, V.comp_img)
                    isPlayerturn = not isPlayerturn
            else:
                V.set_status_bar_text_and_countdown("You won this time! Good Job!", 'DarkGreen')
                break 

        isQuit = V.askToQuit()

    V.closeWin()

main()