import numpy as np, os

class Gayem:
    def __init__(self):
        pass
    
    def init(self, player, diff):
        os.system('cls')
        self.board = [' ' for i in range(9)]
        self.me = player
        self.c = 'X' if self.me == 'O' else 'O'

        self.diff = [0.1, 0.3, 0.9][diff-1]
        self.moves = [i for i in range(9)]

    def print_board(self, ini):
        print("-----------------")
        if ini:
            for i in (0, 3, 6):
                print("  {}  |  {}  |  {}  ".format(self.board[i], self.board[i+1], self.board[i+2]))
                print("-----------------")
        else:
            for i in (1, 4, 7):
                print("  {}  |  {}  |  {}  ".format(i, i+1, i+2))
                print("-----------------")
    
    def is_win(self):
        #check diagonal
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ': return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ': return self.board[2]
        #check horizontal
        for i in (0, 3, 6):
            if self.board[i] == self.board[i+1] == self.board[i+2] and self.board[i] != ' ': return self.board[i]
        #check vertical
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] != ' ': return self.board[i]
        if ' ' in self.board: return None
        return '.'

    
    def max(self, a, b):
        maxV = -2
        mc = 0

        res = self.is_win()

        if res == self.c: return (1, 0)
        elif res == self.me: return (-1, 0)
        elif res == '.': return (0, 0)

        for move in range(9):
            if self.board[move] == ' ':
                self.board[move] = self.c
                (v, pc) = self.min(a, b)
                a = max(v, a)
                if v > maxV:
                    maxV = v
                    mc = move
                self.board[move] = ' '
                if a >= b: break
        return (maxV, mc)
    

    def min(self, a, b):
        minV = 2
        mc = 0
        
        res = self.is_win()

        if res == self.me: return (-1, 0)
        elif res == self.c: return (1, 0)
        elif res == '.': return (0, 0)

        for move in range(9):
            if self.board[move] == ' ':
                self.board[move] = self.me
                (v, pc) = self.max(a, b)
                b = min(v, b)
                if v < minV:
                    minV = v
                    mc = move
                self.board[move] = ' '
                if b <= a: break
        return (minV, mc)



    def play(self):
        x = m = ''
        player = False if self.c == 'X' else True
        first = False
        while True:
            self.print_board(first)
            first = True
            self.res = self.is_win()

            if self.res != None:
                if self.res == 'X': print("The winner is X")
                elif self.res == 'O': print("The winner is O")
                elif self.res == '.': print("It's a fuckin' tie")
                break

            if player:
                move = int(input(x + " Choose a cell: "))
                x = ''
                if move > 9:
                    x = 'Invalid Move, Try again'
                    os.system('cls')
                    continue
                if self.board[move - 1] != ' ':
                    x = 'Invalid Move, Try again'
                    os.system('cls')
                    continue
                self.board[move - 1] = self.me
                del self.moves[self.moves.index(move - 1)]
                player = False
            
            else:
                k = np.random.choice(['r','o'], p=[1 - self.diff, self.diff])
                if k == 'r': 
                    ran = np.random.choice(self.moves)
                    self.board[ran] = self.c
                    del self.moves[self.moves.index(ran)]
                    player = True
                else:
                    (m, move) = self.max(-5, 5)
                    self.board[move] = self.c
                    del self.moves[self.moves.index(move)]
                    player = True
            os.system('cls')

user = "1"
while user == "1":
    os.system('cls')
    q = input("Choose your letter: ").upper()
    d = input("Choose the diffculty (1 for easy, 2 for medium, 3 for hard): ")
    if not d.isdigit(): continue
    else: d = int(d)
    g = Gayem()
    g.init(q, d)
    g.play()

    user = input("Would u like to play again? 1 for yes, 2 for no: ")