# Author: Ryan Yong
# Date: November 15, 2020
# Purpose: To find the shortest path from a start vertex to a goal vertex with breadth-first search

from collections import *
from vertex import Vertex


def bfs(start, goal):
    goal_reached = False
    path = []
    frontier = deque()
    frontier.append(start)
    backpointer = {}
    backpointer[start] = None

    # While the frontier is not empty, adds unvisited adjacent vertices to the backpointer dictionary until the goal is inside of the backpointer dictionary
    while len(frontier) != 0:
        v = frontier.popleft()

        # Adds unvisited adjacent vertices to the frontier and backpointer dictionary
        for u in v.adj_list:
            if u not in backpointer:
                frontier.append(u)
                backpointer[u] = v

        if goal in backpointer:
            goal_reached = True
            break

    # If the goal is in the backpointer dictionary, creates a path list of vertices from the goal vertex to the start vertex
    if goal_reached:
        curr = goal

        # While the current vertex exists (and is not at the start vertex), adds the current vertex to the path list and sets itself to the backpointer afterward
        while curr is not None:
            path.append(curr)
            curr = backpointer[curr]

    return path
