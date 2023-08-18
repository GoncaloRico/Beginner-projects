from Player import HumanPlayer, RandomComputerPlayer, Player

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] #using a single list to represent game board 
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0, 1, 2, etc (tells us what number corresponds to each box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot ==" "] #This is the same as everything that is below, until "return moves".
        # moves = []
        # for (i, spot) in enumerate(self.board): #This will associate a position to a move. If the board looks like this: "X O O" it will turn into [(0, "X"), (1, "O"), (2, "O")]
        #     if spot == " ": #this will mean that spot is available for a move, so we will append it to "moves"
        #         moves.append(i)
        #         return moves
    def empty_squares(self):
        return " " in self.board #This will return a boolean telling us if there are empty squares in the board.
    
    def num_empty_squares(self):
        return len(self.available_moves())
    
    def make_move(self, square, letter):
        # if valid move, then assign letter to square then return true. Else return false
        if self.board[square] == " ":
            self.board[square] = letter
            for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
                print("| " + " | ".join(row) + " |")
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #winner if 3 in a row anywhere.
        #check row
        row_ind = square // 3 #this devides the chosen square by 3 and then rounds down
        row = self.board[row_ind*3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)] 
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonal
        #but only if the square is an even number, as they are the only possible moves to win in diagonal (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #this is the 1st diagonal (left to right diag)
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diag
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #if all of these fail, no winner
        return False

def play(game, x_player, o_player, print_game=True):
    #returns winner or None if tie
    if print_game:
        game.print_board_nums()

    letter = "X" #Starting letter
    #Iterate while game still has available moves
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #defining a function to make move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board
                print(" ")

            if game.current_winner != None:
                if print_game:
                    print(f"Congratulations {letter}, you win!")
                    return letter

            #After making move, we need to alternate letters:
            letter = "O" if letter == "X" else "X"
        
    if print_game:
        print("It's a tie!")

if __name__ == "__main__":
        x_player = HumanPlayer("X")
        o_player = RandomComputerPlayer("O")
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)


