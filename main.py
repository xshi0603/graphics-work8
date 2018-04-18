from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

i = new_matrix()
ident(i)
stack = [i]

parse_file( 'script', stack, edges, polygons, transform, screen, color )
'''
m = new_matrix()
ident(m)
m[2][2] = 123
m.append([1, 2, 3, 4])
print_matrix(m)


t = copy_matrix(m)
print_matrix(t)
'''
