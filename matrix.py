"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for r in range(4):
        line = ""
        for c in matrix:
            line += c[r] + "  "
        print(line)
    pass

#turn the parameter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(4):
        for y in range(4):
            if x == y:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for col in range(len(m2)):
        tmp = []
        for i in m2[col]:
            tmp.append(i)
        for r in range(4):
            sum = 0
            for c in range(4):
                sum += m2[col][r] * m1[c][r]
        
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
