from display import *
from draw import *
from matrix import *

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A) 
print_matrix(A)
print_matrix(B)
ident(B)
matrix_mult(B,A)
print_matrix(A)

##C = [[1,2,3,1],[4,5,6,1]]
##print_matrix(C)
##D = new_matrix()
##ident(D)
##print_matrix(D)
##matrix_mult(D,C)
##print_matrix(C)
##D = [[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]]
##print_matrix(D)
##matrix_mult(D,C)
##print_matrix(C)

screen = new_screen()
color = [ 255, 0, 255 ]
matrix = new_matrix()

add_edge(matrix,50,50,0,50,450,0)
add_edge(matrix,50,50,0,200,350,0)
add_edge(matrix,50,100,0,400,450,0)
add_edge(matrix,50,50,0,350,200,0)

rotation = new_matrix()
rotation[0][1] = 1
rotation[1][0] = -1

draw_lines(matrix,screen,color)

matrix_mult(rotation,matrix)
for x in matrix:
    if x[0] != 0:
        x[0] += 500

draw_lines(matrix,screen,color)

matrix_mult(rotation,matrix)
for x in matrix:
    if x[0] != 0:
        x[0] += 500

draw_lines(matrix,screen,color)

matrix_mult(rotation,matrix)
for x in matrix:
    if x[0] != 0:
        x[0] += 500

draw_lines(matrix,screen,color)

save_extension(screen, 'img.png')

display(screen)
 
