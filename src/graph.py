# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:39:04 2018

@author: I329986
"""
import collections

# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def bfs(graph, start):
    queue = collections.deque([start])
    seen = set([start])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
                

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }
print(gdict)

print("Depth first Search")
print(dfs(gdict, 'a'))

print("Breadth First Search")
print(bfs(gdict, 'a'))