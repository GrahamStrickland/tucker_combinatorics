# Tucker - Applied Combinatorics 6e - Section 2.1 Ex. 20. (a)
# Given list of vertices (V) and list of tuples representing edges (E),
# find Euler cycle if one exists. Output in form of list with elements 
# representing consecutive vertices in Euler cycle. Return empty list if 
# no Euler cycle exists.
from typing import List

def find_euler_cycle(V: List[int], E: List[tuple[int]]) -> List[int]:
    """Return a list containing an Euler cycle in the graph represented 
    by G = (V, E) if one exists, otherwise return empty list."""
    degrees = {vertex: 0 for vertex in V}

    # Add all degrees
    for edge in E:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    # Check degree of all vertices, if not even, no Euler cycle exists
    if any(value % 2 != 0 for value in degrees.values()):
        return []
    else:   # Find Euler cycle
        e_cycle = []
        curr_edge = E[0]
        E.remove(curr_edge)
        e_cycle.append(curr_edge[0])
        e_cycle.append(curr_edge[1])
        while len(E) > 0:
            for edge in E:  # Search through edges for edge containing vertex
                if curr_edge[1] in edge:
                    if curr_edge[1] == edge[0]:
                        e_cycle.append(curr_edge[0])
                        curr_edge = edge
                    else:
                        e_cycle.append(curr_edge[1])
                        curr_edge = edge[::-1]
                    E.remove(edge)

                    # Decrease degree of starting vertex
                    if degrees[curr_edge[0]] > 0:
                        degrees[curr_edge[0]] -= 1
                    else:   # No Euler cycle exists
                        return []

        return e_cycle
