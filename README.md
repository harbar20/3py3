# 3py3
Virtual Rubik's Cube in Python.

# How to Use
This program creates a class called `Cube()`. The user has to create an instance of `Cube()` and now has the capability to use the following functions:

  # Cube.execute(self, moves)
  This function executes a given list of notations on the current state of the cube, regardless of whether the cube is in its solved state    or not.
  
  # Cube.get_scramble(self, numMoves)
  This function returns a list of notations that is exactly `numMoves` long. This list can be used to input into `Cube.execute(moves)` to 
  execute the list of notations.
  
  # Cube.get_solve(self)
  This function returns a list of notations that gives the exact solution to the current state of the cube; it does not require any         inputs. 
  
# __str__
When printing this function, the printed cube should look somewhat like this:
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
Where each letter represents a color based on the orientation of your cube. 

# ENJOY
  
  
