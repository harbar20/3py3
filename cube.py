import random
import kociemba
import copy

#function to change each face in a  turn. 
def turnSide(side, copy1, copy2, copy3, numMoves, isPrime,
             falseSide1, falseSide2,
             falseCopy1, falseCopy2,
             trueSide1, trueSide2, 
             trueCopy1, trueCopy2,
             twoSide1, twoSide2, 
             twoCopy1, twoCopy2,
             ):
    """
    Changes each face when a turn is made
    """
    if numMoves == 1:
        if not isPrime:
            side[falseSide1][falseSide2] = copy1[falseCopy1][falseCopy2]
        elif isPrime:
            side[trueSide1][trueSide2] = copy2[trueCopy1][trueCopy2]
    elif numMoves == 2:
        side[twoSide1][twoSide2] = copy3[twoCopy1][twoCopy2]

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
            turnSide(self.r_side, b_copy, f_copy, l_copy, numMoves, isPrime, 
                     0, r, 0, r, 0, r, 0, r, 0, r, 0, r)
        
        for f in range(3):
            turnSide(self.f_side, r_copy, l_copy, b_copy, numMoves, isPrime,
                     0, f, 0, f, 0, f, 0, f, 0, f, 0, f)
        
        for l in range(3):
            turnSide(self.l_side, f_copy, b_copy, r_copy, numMoves, isPrime,
                     0, l, 0, l, 0, l, 0, l, 0, l, 0, l)
        
        for b in range(3):
            turnSide(self.b_side, l_copy, r_copy, f_copy, numMoves, isPrime,
                     0, b, 0, b, 0, b, 0, b, 0, b, 0, b)

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
            turnSide(self.u_side, f_copy, b_copy, d_copy, numMoves, isPrime,
                     u, 2, u, 2, u, 2, 2-u, 0, u, 2, u, 2)
        
        for f in range(3):
            turnSide(self.f_side, d_copy, u_copy, b_copy, numMoves, isPrime,
                     f, 2, f, 2, f, 2, f, 2, f, 2, 2-f, 0)
        
        for d in range(3):
            turnSide(self.d_side, b_copy, f_copy, u_copy, numMoves, isPrime,
                     d, 2, 2-d, 0, d, 2, d, 2, d, 2, d, 2)
        
        for b in range(3):
            turnSide(self.b_side, u_copy, d_copy, f_copy, numMoves, isPrime,
                     b, 0, 2-b, 2, b, 0, 2-b, 2, b, 0, 2-b, 2)
        
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
            turnSide(self.r_side, u_copy, d_copy, l_copy, numMoves, isPrime, 
                     r, 0, 2, r, r, 0, 0, 2-r, r, 0, 2-r, 2)
        
        for u in range(3):
            turnSide(self.u_side, l_copy, r_copy, d_copy, numMoves, isPrime,
                     2, u, 2-u, 2, 2, u, u, 0, 2, u, 0, 2-u)
        
        for l in range(3):
            turnSide(self.l_side, d_copy, u_copy, r_copy, numMoves, isPrime,
                     l, 2, 0, l, l, 2, 2, 2-l, l, 2, 2-l, 0)
        
        for d in range(3):
            turnSide(self.d_side, r_copy, l_copy, u_copy, numMoves, isPrime,
                     0, d, 2-d, 0, 0, d, d, 2, 0, d, 2, 2-d)
        
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
            turnSide(self.r_side, f_copy, b_copy, l_copy, numMoves, isPrime,
                     2, r, 2, r, 2, r, 2, r, 2, r, 2, r)
                
        for f in range(3):
            turnSide(self.f_side, l_copy, r_copy, b_copy, numMoves, isPrime,
                     2, f, 2, f, 2, f, 2, f, 2, f, 2, f)
        
        for l in range(3):
            turnSide(self.l_side, b_copy, f_copy, r_copy, numMoves, isPrime,
                     2, l, 2, l, 2, l, 2, l, 2, l, 2, l)
        
        for b in range(3):
            turnSide(self.b_side, r_copy, l_copy, f_copy, numMoves, isPrime,
                     2, b, 2, b, 2, b, 2, b, 2, b, 2, b)
        
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
            turnSide(self.u_side, b_copy, f_copy, d_copy, numMoves, isPrime,
                     u, 0, 2-u, 2, u, 0, u, 0, u, 0, u, 0)
        
        for f in range(3):
            turnSide(self.f_side, u_copy, d_copy, b_copy, numMoves, isPrime,
                     f, 0, f, 0, f, 0, f, 0, f, 0, 2-f, 2)
        
        for d in range(3):
            turnSide(self.d_side, f_copy, b_copy, u_copy, numMoves, isPrime,
                     d, 0, d, 0, d, 0, 2-d, 2, d, 0, d, 0)
        
        for b in range(3):
            turnSide(self.b_side, d_copy, u_copy, f_copy, numMoves, isPrime, 
                     b, 2, 2-b, 0, b, 0, 2-b, 0, b, 2, 2-b, 0)
        
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
            turnSide(self.r_side, d_copy, u_copy, l_copy, numMoves, isPrime,
                     r, 2, 2, 2-r, r, 2, 0, r, r, 2, 2-r, 0)
        
        for u in range(3):
            turnSide(self.u_side, r_copy, l_copy, d_copy, numMoves, isPrime,
                     0, u, u, 2, 0, u, 2-u, 0, 0, u, 2, 2-u)
        
        for l in range(3):
            turnSide(self.l_side, u_copy, d_copy, r_copy, numMoves, isPrime,
                     l, 0, 0, 2-l, l, 0, 2, l, l, 0, 2-l, 2)
        
        for d in range(3):
            turnSide(self.d_side, l_copy, r_copy, u_copy, numMoves, isPrime,
                     2, d, d, 0, 2, d, 2-d, 2, 2, d, 0, 2-d)
        
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

        """
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
        """

        u_state = [self.u_side[i][j] for i in range(3) for j in range(3)]
        l_state = [self.l_side[i][j] for i in range(3) for j in range(3)]
        f_state = [self.f_side[i][j] for i in range(3) for j in range(3)]
        r_state = [self.r_side[i][j] for i in range(3) for j in range(3)]
        b_state = [self.b_side[i][j] for i in range(3) for j in range(3)]
        d_state = [self.d_side[i][j] for i in range(3) for j in range(3)]

        cubeState = u_state + \
                    l_state[:3] + f_state[:3] + r_state[:3] + b_state[:3] + \
                    l_state[3:6] + f_state[3:6] + r_state[3:6] + b_state[3:6] + \
                    l_state[6:9] + f_state[6:9] + r_state[6:9] + b_state[6:9] + \
                    d_state

        state = diagram.format(*cubeState)

        return state

    #switch statement to be used to execute moves
    def executeSwitch(self, move, args):
        """
        Replicates a switch-case statement
        to be used to in self.execute
        """
        #dictionary to assign each move to a function
        switcher = {"U": self.u_move,
                    "R": self.r_move,
                    "F": self.f_move,
                    "D": self.d_move,
                    "L": self.l_move,
                    "B": self.b_move
                    }
        
        #function to get the move, and thus, the function
        func = switcher.get(move[0])
        func(*args)

    def execute(self, moves):
        """Given a list of moves,
        executes them regardless of 
        current state of cube.
        """
        for move in moves:
            if len(move) == 1:
                args = (1,)
            elif move[1] == "2":
                args = (2,) 
            elif move[1] == "'":
                args = (1, True)
            
            self.executeSwitch(move[0], args)

    def get_scramble(self, lenscram):
        """Returns a list of moves 
        to scramble the cube. 
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
        #goes through each list in cubeState, then each letter in each list
        cubeState = [j for i in cubeState for j in i]

        #joins together all the letters in cubeState
        cubeState = ''.join(cubeState)
        cubeState = kociemba.solve(cubeState)

        #separates the solution between spaces
        cubeState = cubeState.split(" ")
        return cubeState
