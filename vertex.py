# Author: Ryan Yong
# Date: November 11, 2020
# Purpose: To use for creating a vertex

from cs1lib import *

VERTEX_RADIUS = 7
EDGE_WIDTH = 4


class Vertex:
    def __init__(self, name, adj_list, x, y):
        self.name = name
        self.adj_list = adj_list
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        # Creates a string of the adjacent vertices of the vertex
        vertices_string = ""
        for vertex in self.adj_list:
            vertices_string += vertex.name + ", "

        return self.name + "; Location: " + str(self.x) + ", " + str(
            self.y) + "; Adjacent vertices: " + vertices_string.strip(", ")

    # Draws the vertex with a specified color
    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # Draws the edge between the vertex and another vertex with a specified color
    def draw_edge(self, other_vertex, r, g, b):
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, other_vertex.x, other_vertex.y)

    # Draws all edges between the vertex and its adjacent vertices with a specified color
    def draw_adj_edges(self, r, g, b):
        for vertex in self.adj_list:
            self.draw_edge(vertex, r, g, b)

    # Returns true if the mouse is inside of the smallest square surrounding the vertex
    def mouse_in_square(self, x, y):
        if self.x - VERTEX_RADIUS <= x <= self.x + VERTEX_RADIUS and self.y - VERTEX_RADIUS <= y <= self.y + VERTEX_RADIUS:
            return True
