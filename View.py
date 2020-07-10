from graphics import *
import time

class View:

    # define window size
    win_width = 600
    win_height = 600

    # define coordinate size
    max_coords_x = 100
    max_coords_y = 100

    # define board area
    board_x_min = max_coords_x * .20
    board_y_min = max_coords_y * .20
    board_x_max = max_coords_x * .80
    board_y_max = max_coords_y * .80

    #define box height and weight
    box_width = (board_x_max - board_x_min)/3
    box_height = (board_y_max - board_y_min)/3

    # font size
    large_font = 36
    small_font = 15

    # img files
    comp_img = 'assets/comp_img.gif'
    player_img = 'assets/player_img.gif'

    def __init__(self):
        self.setupWindow()
        self.insertStatusBar(self.win)
        self.insertGameTitle("Tic-Tac-Toe", self.win)
        self.insertGameBoard()
        self.images = []

    def setupWindow(self, win_width=500, win_height=500, max_coords_x=100, max_coords_y=100):
        self.win = GraphWin("Tic-Tac-Toe", win_width, win_height)
        self.win.setCoords(0, 0, max_coords_x, max_coords_y)

    def insertGameTitle(self, title, win):
        self.game_title = Text(Point(self.max_coords_x/2,self.max_coords_y*.875), title).draw(self.win)
        self.game_title.setSize(self.large_font)

    def insertStatusBar(self, win):
        self.status_bar_container = Rectangle(Point(0,0), Point(100, self.board_y_min-5)).draw(self.win)
        self.status_bar_container.setFill("Gray")
        self.status_bar_container.setWidth(0)

        self.status_bar = Text(Point(self.max_coords_x/2,self.max_coords_y*.080), "status bar").draw(self.win)
        self.status_bar.setSize(self.small_font)

    def insertGameBoard(self):
        board = Rectangle(Point(self.board_x_min,self.board_y_min), Point(self.board_x_max, self.board_y_max)).draw(self.win)
        board.setWidth(4)

        C = self._init_grid_coords()
        lines = [[C[4],C[7]], [C[8],C[11]], [C[1],C[13]], [C[2],C[14]]]

        for line in lines:
            l = Line(line[0], line[1]).draw(self.win)
            l.setWidth(4)

    def drawImage(self, index, img):
        img = Image(self._getBoxAnchor(index), img).draw(self.win)
        self.images.append(img)
        return img

    def _getBoxAnchor(self, index):
        x_i = self.board_x_min + self.box_width/2
        y_i = self.board_y_min + self.box_height/2

        rows = [x_i, x_i + self.box_width, x_i + self.box_width*2]
        columns = [y_i, y_i + self.box_height, y_i + self.box_height*2]

        _grid = []

        for j in columns:
            for i in rows:
                _grid.append(Point(i, j))

        return _grid[index]

    def getClickedBox(self, point):
        # return -1 if no boxes are clicked
        x = point.x
        y = point.y
        
        _grid_coords = self._init_grid_coords()

        _boxes = []

        for i in range(11):
            if i != 3 and i != 7:
                _boxes.append([_grid_coords[i], _grid_coords[i+1], _grid_coords[i+4], _grid_coords[i+5]])
        
        for index, box in enumerate(_boxes):
            if box[0].x <= x <= box[1].x and box[1].y <= y <= box[2].y:
                return index

        return -1

    def _init_grid_coords(self):
        x_i = self.board_x_min
        y_i = self.board_y_min

        rows = [x_i, x_i + self.box_width, x_i + self.box_width*2, x_i + self.box_width*3]
        columns = [y_i, y_i + self.box_height, y_i + self.box_height*2, y_i + self.box_height*3]
        
        _grid_coords = []
        for j in columns:
            for i in rows:
                _grid_coords.append(Point(i, j))   
        
        return _grid_coords

    def set_status_bar_text(self, text, color="black"):
        self.status_bar.setText(text)
        self.status_bar.setFill(color)

    def set_status_bar_text_and_countdown(self, text, color="black", duration=5, increment=1):
        moment_count = 0
        while moment_count <= duration:
            time.sleep(increment)
            display_text = text + f" (Restart in {duration - moment_count} secs)"
            self.set_status_bar_text(display_text, color)
            moment_count += increment

    def isStatusBarPress(self, point):
        x = point.x
        y = point.y
        return self.board_x_min <= x <= self.board_x_max and 0 <= y <= self.board_y_min

    def resetBoardView(self):
        for img in self.images:
            img.undraw()

    def askToQuit(self):
        #time.sleep(5) # pause for 5 seconds before the next round
        self.set_status_bar_text("Press INSIDE to play again or OUTSIDE to quit.", "blue")
        pos = self.win.getMouse()
        return not self.isStatusBarPress(pos)

    def pauseComp(self, sec):
        self.set_status_bar_text("Computer is thinking...")
        time.sleep(sec)

    def getPlayerResponse(self):
        self.set_status_bar_text("It's your turn.", 'DarkGreen')
        return self.win.getMouse()

    def isBoxClicked(self, box_index):
        return True if box_index != -1 else False

    def closeWin(self):
        self.win.close()


