import random
import kociemba
import copy

"""
#switch statement to be used to execute moves
def executeSwitch(move, args):
    switcher = {
                "U": self.u_move(*args),
                "R": self.r_move(*args),
                "F": self.f_move(*args),
                "D": self.d_move(*args),
                "L": self.l_move(*args),
                "B": self.b_move(*args)
                }
    return switcher.get(move, "Invalid move")
"""
class Cube():
    # All valid 3x3x3 moves in half-turn metric
    notations = {"U", "D",
                 "R", "L",
                 "F", "B"}
    u_side = [["U", "U", "U"], ["U", "U", "U"], ["U", "U", "U"]]
    r_side = [["R", "R", "R"], ["R", "R", "R"], ["R", "R", "R"]]
    f_side = [["F", "F", "F"], ["F", "F", "F"], ["F", "F", "F"]]
    d_side = [["D", "D", "D"], ["D", "D", "D"], ["D", "D", "D"]]
    l_side = [["L", "L", "L"], ["L", "L", "L"], ["L", "L", "L"]]
    b_side = [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]]

    def rotation_side(self, side, copy, numMoves, isPrime):
        """
        Rotates a given side when 
        that same move is made. 
        """
       # print("side before rotation: ", side)
        if numMoves == 1:
            if isPrime == False:
                side[0] = [copy[2][0], copy[1][0], copy[0][0]]
                side[1] = [copy[2][1], copy[1][1], copy[0][1]]
                side[2] = [copy[2][2], copy[1][2], copy[0][2]]
            elif isPrime == True:
                side[0] = [copy[0][2], copy[1][2], copy[2][2]]
                side[1] = [copy[0][1], copy[1][1], copy[2][1]]
                side[2] = [copy[0][0], copy[1][0], copy[2][0]]
        elif numMoves == 2:
            side[0] = [copy[2][2], copy[2][1], copy[2][0]]
            side[1] = [copy[1][2], copy[1][1], copy[1][0]]
            side[2] = [copy[0][2], copy[0][1], copy[0][0]]

      #  print("side after rotation: ", side)
    
    def u_move(self, numMoves, isPrime=False):
        """Applies a certain type of 'U' move to self.u_side
        numMoves: int; number of 'U' moves
        isPrime: bool; is 'U' move prime or not?
        """
        r_copy = copy.deepcopy(self.r_side)
        f_copy = copy.deepcopy(self.f_side)
        l_copy = copy.deepcopy(self.l_side)
        b_copy = copy.deepcopy(self.b_side)
        u_copy = copy.deepcopy(self.u_side)

        for r in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.r_side[0][r] = b_copy[0][r]
                elif isPrime == True:
                    self.r_side[0][r] = f_copy[0][r]
            elif numMoves == 2:
                self.r_side[0][r] = l_copy[0][r]
        
        for f in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.f_side[0][f] = r_copy[0][f]
                elif isPrime == True:
                    self.f_side[0][f] = l_copy[0][f]
            elif numMoves == 2:
                self.f_side[0][f] = b_copy[0][f]
        
        for l in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.l_side[0][l] = f_copy[0][l]
                elif isPrime == True:
                    self.l_side[0][l] = b_copy[0][l]
            elif numMoves == 2:
                self.l_side[0][l] = r_copy[0][l]
        
        for b in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.b_side[0][b] = l_copy[0][b]
                elif isPrime == True:
                    self.b_side[0][b] = r_copy[0][b]
            elif numMoves == 2:
                self.b_side[0][b] = f_copy[0][b]

        self.rotation_side(self.u_side, u_copy, numMoves, isPrime)

    def r_move(self, numMoves, isPrime=False):
        """Applies a certain type of 'R' move to self.r_side
        numMoves: int; number of 'R' moves
        isPrime: bool; is 'R' move prime or not?
        """
        u_copy = copy.deepcopy(self.u_side)
        f_copy = copy.deepcopy(self.f_side)
        d_copy = copy.deepcopy(self.d_side)
        b_copy = copy.deepcopy(self.b_side)
        r_copy = copy.deepcopy(self.r_side)

        for u in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.u_side[u][2] = f_copy[u][2]
                elif isPrime == True:
                    self.u_side[u][2] = b_copy[2-u][0]
            elif numMoves == 2:
                self.u_side[u][2] = d_copy[u][2]
        
        for f in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.f_side[f][2] = d_copy[f][2]
                elif isPrime == True:
                    self.f_side[f][2] = u_copy[f][2]
            elif numMoves == 2:
                self.f_side[f][2] = b_copy[2-f][0]
        
        for d in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.d_side[d][2] = b_copy[2-d][0]
                elif isPrime == True:
                    self.d_side[d][2] = f_copy[d][2]
            elif numMoves == 2:
                self.d_side[d][2] = u_copy[d][2]
        
        for b in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.b_side[b][0] = u_copy[2-b][2]
                elif isPrime == True:
                    self.b_side[b][0] = d_copy[2-b][2]
            elif numMoves == 2:
                self.b_side[b][0] = f_copy[2-b][2]
        
        self.rotation_side(self.r_side, r_copy, numMoves, isPrime)

    def f_move(self, numMoves, isPrime=False):
        """Applies a certain type of 'F' move to self.u_side
        numMoves: int; number of 'F' moves
        isPrime: bool; is 'F' move prime or not?
        """
        r_copy = copy.deepcopy(self.r_side)
        u_copy = copy.deepcopy(self.u_side)
        l_copy = copy.deepcopy(self.l_side)
        d_copy = copy.deepcopy(self.d_side)
        f_copy = copy.deepcopy(self.f_side)

        for r in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.r_side[r][0] = u_copy[2][r]
                elif isPrime == True:
                    self.r_side[r][0] = d_copy[0][2-r]
            elif numMoves == 2:
                self.r_side[r][0] = l_copy[2-r][2]
        
        for u in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.u_side[2][u] = l_copy[2-u][2]
                elif isPrime == True:
                    self.u_side[2][u] = r_copy[u][0]
            elif numMoves == 2:
                self.u_side[2][u] = d_copy[0][2-u]
        
        for l in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.l_side[l][2] = d_copy[0][l]
                elif isPrime == True:
                    self.l_side[l][2] = u_copy[2][2-l]
            elif numMoves == 2:
                self.l_side[l][2] = r_copy[2-l][0]
        
        for d in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.d_side[0][d] = r_copy[2-d][0]
                elif isPrime == True:
                    self.d_side[0][d] = l_copy[d][2]
            elif numMoves == 2:
                self.d_side[0][d] = u_copy[2][2-d]
        
        self.rotation_side(self.f_side, f_copy, numMoves, isPrime)

    def d_move(self, numMoves, isPrime=False):
        """Applies a certain type of 'D' move to self.u_side
        numMoves: int; number of 'D' moves
        isPrime: bool; is 'D' move prime or not?
        """
        r_copy = copy.deepcopy(self.r_side)
        f_copy = copy.deepcopy(self.f_side)
        l_copy = copy.deepcopy(self.l_side)
        b_copy = copy.deepcopy(self.b_side)
        d_copy = copy.deepcopy(self.d_side)

        for r in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.r_side[2][r] = f_copy[2][r]
                elif isPrime == True:
                    self.r_side[2][r] = b_copy[2][r]
            elif numMoves == 2:
                self.r_side[2][r] = l_copy[2][r]
                
        for f in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.f_side[2][f] = l_copy[2][f]
                elif isPrime == True:
                    self.f_side[2][f] = r_copy[2][f]
            elif numMoves == 2:
                self.f_side[2][f] = b_copy[2][f]
        
        for l in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.l_side[2][l] = b_copy[2][l]
                elif isPrime == True:
                    self.l_side[2][l] = f_copy[2][l]
            elif numMoves == 2:
                self.l_side[2][l] = r_copy[2][l]
        
        for b in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.b_side[2][b] = r_copy[2][b]
                elif isPrime == True:
                    self.b_side[2][b] = l_copy[2][b]
            elif numMoves == 2:
                self.b_side[2][b] = f_copy[2][b]
        
        self.rotation_side(self.d_side, d_copy, numMoves, isPrime) 

    def l_move(self, numMoves, isPrime=False):
        """Applies a certain type of 'L' move to self.r_side
        numMoves: int; number of 'L' moves
        isPrime: bool; is 'L' move prime or not?
        """
        u_copy = copy.deepcopy(self.u_side)
        f_copy = copy.deepcopy(self.f_side)
        d_copy = copy.deepcopy(self.d_side)
        b_copy = copy.deepcopy(self.b_side)
        l_copy = copy.deepcopy(self.l_side)
        

        for u in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.u_side[u][0] = b_copy[2-u][2]
                elif isPrime == True:
                    self.u_side[u][0] = f_copy[u][0]
            elif numMoves == 2:
                self.u_side[u][0] = d_copy[u][0]
        
        for f in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.f_side[f][0] = u_copy[f][0]
                elif isPrime == True:
                    self.f_side[f][0] = d_copy[f][0]
            elif numMoves == 2:
                self.f_side[f][0] = b_copy[2-f][2]
        
        for d in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.d_side[d][0] = f_copy[d][0]
                elif isPrime == True:
                    self.d_side[d][0] = b_copy[2-d][2]
            elif numMoves == 2:
                self.d_side[d][0] = u_copy[d][0]
        
        for b in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.b_side[b][2] = d_copy[2-b][0]
                elif isPrime == True:
                    self.b_side[b][2] = u_copy[2-b][0]
            elif numMoves == 2:
                self.b_side[b][2] = f_copy[2-b][0]
        
        self.rotation_side(self.l_side, l_copy, numMoves, isPrime)

    def b_move(self, numMoves, isPrime=False):
        """Applies a certain type of 'B' move to self.u_side
        numMoves: int; number of 'B' moves
        isPrime: bool; is 'B' move prime or not?
        """
        r_copy = copy.deepcopy(self.r_side)
        u_copy = copy.deepcopy(self.u_side)
        l_copy = copy.deepcopy(self.l_side)
        d_copy = copy.deepcopy(self.d_side)
        b_copy = copy.deepcopy(self.b_side)

        for r in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.r_side[r][2] = d_copy[2][2-r]
                elif isPrime == True:
                    self.r_side[r][2] = u_copy[0][r]
            elif numMoves == 2:
                self.r_side[r][2] = l_copy[2-r][0]
        
        for u in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.u_side[0][u] = r_copy[u][2]
                elif isPrime == True:
                    self.u_side[0][u] = l_copy[2-u][0]
            elif numMoves == 2:
                self.u_side[0][u] = d_copy[2][2-u]
        
        for l in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.l_side[l][0] = u_copy[0][2-l]
                elif isPrime == True:
                    self.l_side[l][0] = d_copy[2][l]
            elif numMoves == 2:
                self.l_side[l][0] = r_copy[2-l][2]
        
        for d in range(3):
            if numMoves == 1:
                if isPrime == False:
                    self.d_side[2][d] = l_copy[d][0]
                elif isPrime == True:
                    self.d_side[2][d] = r_copy[2-d][2]
            elif numMoves == 2:
                self.d_side[2][d] = u_copy[0][2-d]
        
        self.rotation_side(self.b_side, b_copy, numMoves, isPrime)

    def __str__(self):
        """Prints the current state
        of the cube. Should look something
        like this:
             |************|
             |*U1**U2**U3*|
             |************|
             |*U4**U5**U6*|
             |************|
             |*U7**U8**U9*|
             |************|
 ************|************|************|************
 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
 ************|************|************|************
 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
 ************|************|************|************
 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
 ************|************|************|************
             |************|
             |*D1**D2**D3*|
             |************|
             |*D4**D5**D6*|
             |************|
             |*D7**D8**D9*|
             |************|
        """
        with open('cube.txt') as f:
            diagram = f.read()

        state = diagram.format(self.u_side[0][0], self.u_side[0][1], self.u_side[0][2], 
                       self.u_side[1][0], self.u_side[1][1], self.u_side[1][2],
                       self.u_side[2][0], self.u_side[2][1], self.u_side[2][2],
                       self.l_side[0][0], self.l_side[0][1], self.l_side[0][2],
                       self.f_side[0][0], self.f_side[0][1], self.f_side[0][2],
                       self.r_side[0][0], self.r_side[0][1], self.r_side[0][2],
                       self.b_side[0][0], self.b_side[0][1], self.b_side[0][2],
                       self.l_side[1][0], self.l_side[1][1], self.l_side[1][2],
                       self.f_side[1][0], self.f_side[1][1], self.f_side[1][2],
                       self.r_side[1][0], self.r_side[1][1], self.r_side[1][2],
                       self.b_side[1][0], self.b_side[1][1], self.b_side[1][2],
                       self.l_side[2][0], self.l_side[2][1], self.l_side[2][2],
                       self.f_side[2][0], self.f_side[2][1], self.f_side[2][2],
                       self.r_side[2][0], self.r_side[2][1], self.r_side[2][2],
                       self.b_side[2][0], self.b_side[2][1], self.b_side[2][2],
                       self.d_side[0][0], self.d_side[0][1], self.d_side[0][2],
                       self.d_side[1][0], self.d_side[1][1], self.d_side[1][2],
                       self.d_side[2][0], self.d_side[2][1], self.d_side[2][2])
        
        return state

    def execute(self, moves):
        """Given a list of moves,
        executes them regardless of 
        current state of cube.
        """
        for move in moves:
            #print('move in loop: ', move)
            if len(move) == 1:
                args = (1,)
            elif move[1] == "2":
                args = (2,) 
            elif move[1] == "'":
                args = (1, True)
            
           # print('args before execution: ', *args)
            
            if move[0] == "U":
                self.u_move(*args)
            if move[0] == "R":
                self.r_move(*args)
            if move[0] == "F":
                self.f_move(*args)
            if move[0] == "D":
                self.d_move(*args)
            if move[0] == "L":
                self.l_move(*args)
            if move[0] == "B":
                self.b_move(*args)
            
           # executeSwitch(move[0])

    def get_scramble(self, lenscram):
        """Returns a list of moves 
        to scramble a 3x3 cube. 
        """ 
        scramble = []
    
        for i in range(lenscram):
            if i == 0:
                move = random.choice(list(self.notations)) + random.choice(["", "'", "2"])
           
            else:
                move = random.choice(list(self.notations - set(scramble[-1][0]))) + random.choice(["", "'", "2"])

            scramble.append(move)

        return scramble
    
    def get_solve(self):
        """Returns the optimal
        solution to the current 
        state of the cube.
        """
        #urfdlb
        cubeState = self.u_side + self.r_side + self.f_side + self.d_side + self.l_side + self.b_side
      #  print("cubestate before: ", cubeState)
        cubeState = [j for i in cubeState for j in i]
     #   print("cubestate during: ", cubeState)
        cubeState = ''.join(cubeState)
     #   print("cubestate after: ", cubeState)

        cubeState = kociemba.solve(cubeState)
       # print("cubestate after kociemba: ", cubeState)

        cubeState = cubeState.split(" ")
        return cubeState
