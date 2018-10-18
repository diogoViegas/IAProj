import copy

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


class sol_state:
    def __init__(self, board):
            self.board = board
    #def __lt__ (self,sol_state_1):
            #Heuristic

#class Solitaire(Problem):
    #Models a Solitaire problem as a satisfaction problem.
     #A solution cannot have more than 1 peg left on the board.
     #def __init__(self, board):
     #…
     #def actions(self, state):
     #…
     #def result(self, state, action):
     #…
     #def goal_test(self, state):
     #…
     #
     #def path_cost(self, c, state1, action, state2):
     #…
     #def h(self, node):
     #"""Needed for informed search.        

