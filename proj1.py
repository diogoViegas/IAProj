import copy
from search import *

# TAI content
def c_peg ():
    return "O"
def c_empty ():
    return "_"
def c_blocked ():
    return "X"
def is_empty (e):
    return e == c_empty()
def is_peg (e):
    return e == c_peg()
def is_blocked (e):
    return e == c_blocked()

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
    return (l, c)
def pos_l (pos):
    return pos[0]
def pos_c (pos):
    return pos[1]

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f):
    return [i, f]
def move_initial (move):
    return move[0]
def move_final (move):
    return move[1]

#Exemplo de um tabuleiro
b1 = [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"],
["O","_","O","_","_"], ["_","O","_","_","_"]]

def board_moves (b1):
    res = []
    for i in range (0,len(b1)):
        for j in range (0,len(b1[i])):   
            if is_peg(b1[i][j]):
                if is_empty(b1[i][j-2]) and is_peg(b1[i][j-1]) :
                    if j-2 >= 0:
                        res_aux=[]
                        res_aux.append(tuple((i,j)))
                        res_aux.append(tuple((i,j-2)))
                        res.append(res_aux)
                if  is_empty(b1[i-2][j]) and is_peg(b1[i-1][j]) :
                    if i-2 >= 0:
                        res_aux=[]
                        res_aux.append(tuple((i,j)))
                        res_aux.append(tuple((i-2,j)))
                        res.append(res_aux)
                if j+2 < len(b1[i]):
                    if is_empty(b1[i][j+2]) and is_peg(b1[i][j+1]):
                        res_aux=[]
                        res_aux.append(tuple((i,j)))
                        res_aux.append(tuple((i,j+2)))
                        res.append(res_aux)                
                if i+2 < len(b1):
                    if is_empty(b1[i+2][j]) and is_peg(b1[i+1][j]):
                        res_aux=[]
                        res_aux.append(tuple((i,j)))
                        res_aux.append(tuple((i+2,j)))
                        res.append(res_aux)                        
    return res
                    
def board_perform_move(b1,pos):
    i_inicial=pos[0][0]
    j_inicial=pos[0][1]
    i_final= pos[1][0]
    j_final= pos[1][1]
    if (i_inicial == i_final) and (j_final > j_inicial):
        i_inter = i_inicial
        j_inter = j_final-1
    if (i_inicial == i_final) and (j_final < j_inicial):
        i_inter = i_inicial
        j_inter = j_final+1
    if (j_inicial == j_final) and (i_final > i_inicial):
        j_inter = j_inicial
        i_inter = i_final-1
    if (j_inicial == j_final) and (i_final < i_inicial):
        j_inter = j_inicial
        i_inter = i_final + 1     
    res = copy.deepcopy(b1)
    
    res[i_inicial][j_inicial] = "_"
    res[i_final][j_final] = "O"
    res[i_inter][j_inter] = "_"
    return res

#funcao base da heuristica
#quanto menor o numero de pecas isoladas -- melhor 

#def number_of_iso_pegs(board):
    #counter=0
    #res=[]
    #for i in range (0,len(board)):
        #for j in range (0,len(board[i])):
            #if is_peg(board[i][j]):
                #if (i-1>0 and j-1>=0 and i+1<len(board) and j+1 <= len(board[i])):
                    #if (is_empty(board[i][j-1]) or is_blocked(board[i][j-1])) and (is_empty(board[i-1][j]) or is_blocked(board[i-1][j])) and (is_empty(board[i+1][j]) or is_blocked(board[i+1][j])) and (is_empty(board[i][j+1]) or is_blocked(board[i][j+1])):
                        #res.append(tuple((i,j)))
                        #counter+=1
    #return res                                                                          
              
                                                                                                     
            
class sol_state:
    def __init__(self, board):
            self.board = board
            #self.number_of_iso = number_of_iso_pegs(board)
            self.number_moves = len(board_moves(board))
    def __lt__ (self,other):
            #return self.number_of_iso < other.number_of_iso
            return self.number_moves > other.number_moves

class solitaire(Problem):
        #Models a Solitaire problem as a satisfaction problem.
        #A solution cannot have more than 1 peg left on the board.
        def __init__(self, board):
            super().__init__(sol_state(board))
                       
        def actions(self, state):
            return board_moves(state.board)
        
        def result(self, state, action):
            return sol_state(board_perform_move(state.board, action))
            
        def goal_test(self, state):
            counter=0
            for i in range(0,len(state.board)):
                for j in range(0,len(state.board[i])):
                    if is_peg(state.board[i][j]):
                        counter+=1
            if (counter==1):
                return True
            else:
                return False
            
        #def h(self, node):
            #"""Needed for informed search.        




#input do teste 25, nao esta a passar
#print(xx_invalid_solution([["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]],depth_first_tree_search(solitaire([["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]))))


