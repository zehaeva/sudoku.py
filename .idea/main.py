__author__ = 'zehaeva'
import cmd, sys

class SudokuBoard:
    size = 9
    sub = 3
    allow_invalid = True

    #board = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 1, 2, 3, 4, 5, 6, 7, 8], [8, 9, 1, 2, 3, 4, 5, 6, 7],
    #         [7, 8, 9, 1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 1, 2, 3, 4],
    #         [4, 5, 6, 7, 8, 9, 1, 2, 3], [3, 4, 5, 6, 7, 8, 9, 1, 2], [2, 3, 4, 5, 6, 7, 8, 9, 2]]

    def __init__(self, size):
        self.size = size
        self.sub = int(size ** (1/2))
        self.board = [['_' for x in range(1, size + 1)] for x in range(1, size + 1)]

    def __repr__(self):
        my_return = ''
        for x in range(0, self.size):
            my_return += ' '.join([str(x) for x in self.board[x]]) + '\n'
        return(my_return)

    def set_cell(self, value, x, y):
        old_value = self.board[x][y]
        self.board[x][y] = value
        if not self.allow_invalid:
            if not self.valid_cell(x, y):
                self.board[x][y] = old_value
                raise

    def valid_cell(self, x, y):
        am_i = True
        for z in range(0, self.size):
            # Rows
            if self.board[x][y] == self.board[x][z] and z != y:
                am_i = False
                break
            # Columns
            if self.board[x][y] == self.board[z][y] and z != x:
                am_i = False
                break
        # now to check the subcell
        # which cell_row am i in?
        cell_row = int(int(x / self.sub) * self.sub)
        cell_column = int(int(y / self.sub) * self.sub)

        for xs in range(cell_row, (cell_row + self.sub)):
            for ys in range(cell_column, (cell_column + self.sub)):
                if self.board[x][y] == self.board[xs][ys] and (xs, ys) != (x, y):
                    am_i = False
                    break
            if not am_i:
                break
        return am_i

    def valid_board(self):

        am_i = True
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.board[x][y] is not None:
                    am_i = self.valid_cell(x, y)
                    if not am_i:
                        break
            if not am_i:
                break
        return am_i

class SudokuShell(cmd.Cmd):
    intro = 'Welcome to the Sudoku.   Type help or ? to list commands.\n'
    prompt = '(sudoku) '
    board = None

    def do_new(self, arg):
        'Start a new game of Sudoku'
        print(arg)
        self.board = SudokuBoard(int(arg))
    def do_validate(self, arg):
        'Valid the state of the board'
        if self.board.valid_board:
            print('The board is valid!')
        else:
            print('Sorry! Something is wrong!')
    def do_set(self, arg):
        'set the value of the board: X Y Value'
        temp = arg.split(' ')
        self.board.set_cell(int(temp[2]), int(temp[0]), int(temp[1]))
    def do_show(self, arg):
        'Show the game board'
        print(self.board)
    def do_bye(self, arg):
        'Stop recording, close the sudoku window, and exit:  BYE'
        print('Thank you for playing Sudoku')
        return True

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    SudokuShell().cmdloop()
'''
myboard = SudokuBoard(9)

if myboard.valid_board():
    print('Valid')
else:
    print('Invalid')

myboard.board[0][0] = 1
myboard.board[0][1] = 2
myboard.board[0][2] = 3
myboard.set_cell(4, 0, 3)
myboard.board[0][4] = 5
myboard.board[0][5] = 6
myboard.board[0][6] = 7
myboard.board[0][7] = 9
myboard.set_cell(9, 0, 8)#.board[3][8] = 9


if myboard.valid_board():
    print('Valid')
else:
    print('Invalid')
    print(myboard.board)
'''