# Author: Ryan Yong
# Date: November 11, 2020
# Purpose: To take an input file and create a dictionary of vertex objects

from vertex import Vertex


def load_graph(file):

    vertex_dict = {}
    input1 = open(file, "r")

    # Adds all vertices into the vertex dictionary without the adjacent list
    for line in input1:
        line_items = line.strip().split(";")
        x_y = line_items[2].split(",")

        new_vertex = Vertex(line_items[0], [], x_y[0], x_y[1])
        vertex_dict[line_items[0]] = new_vertex

    input1.close()

    input2 = open(file, "r")

    # Fills in the adjacent vertices list of all vertices in the vertex dictionary
    for line in input2:
        line_items = line.strip().split(";")
        new_adj_list = line_items[1].split(",")

        # Adds the object to the adjacent vertices list after removing spaces around vertex names
        for vertex in new_adj_list:
            vertex_dict[line_items[0]].adj_list.append(vertex_dict[vertex.strip()])

    input2.close()

    return vertex_dict
