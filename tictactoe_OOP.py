
#THIS CLEARS THE SCREEN
import os
def clear():
    os.system('clear')

#THIS CLASS HOLDS INFORMATION ABOUT AND FUNCTIONS PERTAINING TO THE PLAYER
class player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def player1_input(self):

        marker_hold = ''
        #Keep asking player 1 to choose x or o
        
        while marker_hold != 'X' and marker_hold != 'O':
            marker_hold = input('Player 1, choose X or O: ')

            marker_hold = marker_hold.upper()
        #Assign player 2, the opposite marker
        self.marker = marker_hold
        print(' ')
        self.name = input('Player 1, please type your name: ')
        

    def player2_input(self, player1_marker):
        if player1_marker == 'X':
            self.marker = '0'
        else:
            self.marker = 'X'
        
        self.name = input('Player 2, please type your name: ')

        #RANDOMLY DECIDE WHICH PLAYER CHOOSES FIRST - RETURNS A BOOLEAN
        import random
    def choose_first(self):
        firstplayer = random.randint(1,2)
        return firstplayer == 1

        #ASK THE USERS IF THEY WOULD LIKE TO PLAY AGAIN - RETURNS A BOOLEAN VALUE
    def replay(self):
        player_input = input('Would you like to play again, Y/N? ')
        if player_input.upper() == 'Y':
            return True
        else:
            return False

      




    


#THIS CLASS CONTAINS INFORMATION AND FUNCTIONS FOR THE BOARD 
class board:
    def __init__(self, board):
        self.board = board

      #DISPLAY THE TIC TAC TOE BOARD
    def display_board(self):
        clear()
        print(' ')
        print ('   |   |   ')
        x = ' '
        x = x+(self.board[1])+(' | ')+(self.board[2])+(' | ')+(self.board[3])+(' ')
        print(x)
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        y = ' '
        y = y+(self.board[4])+(' | ')+(self.board[5])+(' | ')+(self.board[6])+(' ')
        print(y)
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        z = ' '
        z = z+(self.board[7])+(' | ')+(self.board[8])+(' | ')+(self.board[9])+(' ')
        print(z)
        print('   |   |   ')

#PUT THE PLAYER'S MOVE ON THE BOARD
    def place_marker(self, marker, position):
        self.board[position] = marker

#CHECK THE BOARD TO SEE IF A PLAYER HAS WON - RETURNS A BOOLEAN VALUE
    def win_check(self, marker):
      #DEFAULT ASSUMPTION IS NO PLAYER HAS WON
        win = False

    #THESE ARE THE EIGHT POSSIBLE WAYS TO WIN AT TIC TAC TOE
        a = [1,2,3]
        b = [4,5,6]
        c = [7,8,9]
    
        d = [3,6,9]
        e = [1,4,7]
        f = [2,5,8]
    
        g = [1,5,9]
        h = [7,5,3]
    
        if self.board[a[0]]==marker and self.board[a[1]]==marker and self.board[a[2]]==marker:
            win = True
        elif self.board[b[0]]==marker and self.board[b[1]]==marker and self.board[b[2]]==marker:
            win = True
        elif self.board[c[0]]==marker and self.board[c[1]]==marker and self.board[c[2]]==marker:
            win = True
        elif self.board[d[0]]==marker and self.board[d[1]]==marker and self.board[d[2]]==marker:
            win = True
        elif self.board[e[0]]==marker and self.board[e[1]]==marker and self.board[e[2]]==marker:
            win = True
        elif self.board[f[0]]==marker and self.board[f[1]]==marker and self.board[f[2]]==marker:
            win = True
        elif self.board[g[0]]==marker and self.board[g[1]]==marker and self.board[g[2]]==marker:
            win = True
        elif self.board[h[0]]==marker and self.board[h[1]]==marker and self.board[h[2]]==marker:
            win = True

        return win

#CHECK TO SEE IF A SPACE IS FREE - RETURNS A BOOLEAN VALUE
    def space_check(self, position):
        #Is the space available?
        if self.board[position]=='X' or self.board[position]== 'O':
            return False
        else:
            return True

#CHECK TO SEE IF THE BOARD IS FULL - RETURNS A BOOLEAN VALUE
    def full_board_check(self):
    
        i = 1
        while i<=9:
            if i==9 and (self.board[i]=='X' or self.board[i]=='O'):
                return True
            elif i==9 and not (self.board[i]=='X' or self.board[i]=='O'):
                return False
            elif self.board[i] == ' ':
                return False
            else:
                i += 1
        return False

#ASK THE PLAYER TO CHOOSE A POSTION
    def position_choice(self, player):
        check = False
        while not check:
            position = int(input(player.name + ', ' + player.marker + ', please choose your position 1-9: '))
            if (position >=1 and position <=9) and self.space_check(position):
                check = True
        
        return position

    def replay(self):
        player_input = input('Would you like to play again, Y/N? ')
        if player_input.upper() == 'Y':
            return True
        else:
            return False



#CLASSES COMPLETE - MAIN SECTION OF PROGRAM CODE BEGINS HERE



#PLACEHOLDER BOOLEAN VARIABLES
playing_start = True
player_choosing =None
player_choosing2 = None
reset_names_and_markers = True
first_time_through = False


while playing_start:
    
    if reset_names_and_markers and not first_time_through:
    #ASSIGN THE PLAYERS AND ASK THEIR NAMES
        p1 = player(' ', ' ')
        p1.player1_input()
        print(' ')
        print ('Player 1, your name is ' + p1.name + ' and you chose ' + p1.marker)
        print (' ')

        p2 = player(' ', ' ')
        p2.player2_input(p1.marker)
        print(' ')
        print ('Player 2, your name is ' + p2.name + ' and you have been assigned ' + p2.marker)
        print(' ')

        print('Welcome to Tic Tac Toe, ' + p1.name + ' and ' + p2.name +'!')
    else:
        reset_input = input('Would you like to use the same names and markers Y/N? ')
        print(' ')
        if reset_input.upper() == 'N':

            p1.player1_input()
            print(' ')
            print ('Player 1, your name is ' + p1.name + ' and you chose ' + p1.marker)
            print (' ')

            p2.player2_input(p1.marker)
            print(' ')
            print ('Player 2, your name is ' + p2.name + ' and you have been assigned ' + p2.marker)
            print(' ')

            print('Welcome to Tic Tac Toe, ' + p1.name + ' and ' + p2.name +'!')

    #RANDOMLY ASSIGN WHO GOES FIRST
    #ASSIGN PLAYER MARKERS AND NEXT PLAYER
    if p1.choose_first:
        current_player = p1
        x_or_o = p1.marker
        next_player = p2
    else:
        current_player = p2
        x_or_o = player2_marker
        next_player = p1

    
    print(current_player.name + ' is making the first play.')
    #TELLS THE PLAYERS WHO IS MAKING THE FIRST PLAY
    
    demo_board= board(['#','1','2','3','4','5','6','7','8','9'])
    main_board= board(['#',' ',' ',' ',' ',' ',' ',' ',' ',' '])
    #ASSIGN THE MAIN BOARD AND POSITION DEMO BOARD
    
    demo_board.display_board()
    #board.display_board(demo_board)
    #DISPLAYS THE DEMO BOARD
    
    choosing = True
    while choosing == True:
        player_choosing = main_board.position_choice(current_player)
        if player_choosing == False:
            print(current_player.name + "Please pick an empty spot: ")
        else: 
            choosing = False
     #VERIFIES CHOOSEN SPOT IS EMPTY 
            

    main_board.place_marker(x_or_o, player_choosing) 
    #def place_marker(board, marker, position)
    player_choosing=None
    #reset player_choosing
    
    main_board.display_board()
    #Displays main board
    
    
    first_time_through = True
    playing_main = True
    while playing_main:
        
        current_player = next_player
        
        if next_player == p1:
            x_or_o = p1.marker
          #  print("Player 1, it is now your turn. ")
          #  print("You are playing as: ")
          #  print(x_or_o)
        else:
            x_or_o = p2.marker
          #  print("Player 2 it is now your turn. ")
          #  print("You are playing as: ")
           # print(x_or_o)
            
       
            
        choosing2 = True
        while choosing2 == True:
            player_choosing2 = main_board.position_choice(next_player)
            if player_choosing2 == False:
                print("Please pick an empty spot: ")
            else: 
                choosing2 = False
     #Verifies that the spot is empty   
    
    
        main_board.place_marker(x_or_o, player_choosing2)
        clear()
        main_board.display_board()
        player_choosing2 = None
        
        if main_board.win_check(x_or_o):
            if p1.marker == x_or_o:
                print(p1.name + ' wins!')
                playing_main = False
                reset_names_and_markers = False

                if not main_board.replay():
                    playing_start = False
                    print('Thank you have a nice day.')
    
            else:
                print(p2.name + ' wins')
                playing_main = False
                reset_names_and_markers = False
            
                if not main_board.replay():
                    playing_start = False
                    print('Thank you have a nice day.')
        
        elif main_board.full_board_check():
            print ("The cat wins!")
            if main_board.replay():
                playing_main = False
                reset_names_and_markers = False
                print('Lets start a new game!')
            else:
                playing_main = False
                playing_start = False
                print("OK thanks for playing.")
        else:
            if next_player == p1:
                next_player = p2
            else:
                next_player = p1
