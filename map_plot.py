# Author: Ryan Yong
# Date: November 12, 2020
# Purpose: To draw out the map with points plotted and edges drawn

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

# Defines constants
IMG_WIDTH = 1012
IMG_HEIGHT = 811

# Defines variables
map = load_image("dartmouth_map.png")
vertex_dict = load_graph("dartmouth_graph.txt")
mx = IMG_WIDTH / 2
my = IMG_HEIGHT / 2
mouse_pressed = False
start = None
goal = None


# Updates the cursor position
def m_move(x, y):
    global mx, my

    mx = x
    my = y


# Checks if mouse was pressed
def m_press(x, y):
    global mouse_pressed

    mouse_pressed = True


# Checks if mouse was released
def m_release(x, y):
    global mouse_pressed

    mouse_pressed = False


# Main draw function for the map
def map_draw():
    global start, goal

    draw_image(map, 0, 0)

    # Draws all of the vertices and edges of the locations on the map
    for vertex in vertex_dict:
        vertex_dict[vertex].draw_vertex(1, 0, 0)
        vertex_dict[vertex].draw_adj_edges(1, 0, 0)

        # If the mouse was pressed and is in the smallest square surrounding the vertex, sets the start vertex to the vertex where the mouse was pressed
        if mouse_pressed and vertex_dict[vertex].mouse_in_square(mx, my):
            start = vertex_dict[vertex]
        # If the mouse is in the smallest square surrounding the vertex, sets the goal vertex to the vertex where the mouse is hovered
        if vertex_dict[vertex].mouse_in_square(mx, my):
            goal = vertex_dict[vertex]

    # Finds and draws the shortest path between the start and goal vertices if they exist
    if start != None and goal != None:
        shortest_path = bfs(start, goal)

        # Draws all of the vertices and edges between the start and goal vertices
        for i in range(len(shortest_path) - 1):
            shortest_path[i].draw_vertex(0, 1, 0)
            shortest_path[i].draw_edge(shortest_path[i+1], 0, 1, 0)
        shortest_path[-1].draw_vertex(0, 1, 0)


start_graphics(map_draw, mouse_move=m_move, mouse_press=m_press, mouse_release=m_release, width=IMG_WIDTH,
               height=IMG_HEIGHT)
