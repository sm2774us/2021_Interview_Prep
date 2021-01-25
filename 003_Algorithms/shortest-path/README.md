
In graph theory, the [shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem) is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized. The problem is also sometimes called the **single-pair shortest path problem**, to distinguish it from the following variations:

-**single-source shortest path problem**: in which we have to find shortest paths from a source vertex v to all other vertices in the graph.
-**single-destination shortest path problem**: in which we have to find shortest paths from all vertices in the directed graph to a single destination vertex v. This can be reduced to the single-source shortest path problem by reversing the arcs in the directed graph.
-**all-pairs shortest path problem**: in which we have to find shortest paths between every pair of vertices v, v' in the graph.

These generalizations have significantly more efficient algorithms than the simplistic approach of running a single-pair shortest path algorithm on all relevant pairs of vertices. 

There are many possible solutions to the shortest path problem, the most famous are:

- **Dijkstra**'s algorithm: solves the single-source shortest path problem.
- **Bellman–Ford** algorithm: solves the single-source shortest path problem (if edge weights can be negative).
- **A*** search algorithm: solves for single-pair shortest path, using heuristics (to speed up the search).
- **Viterbi** algorithm: solves the shortest stochastic-path problem with an additional probabilistic weight on each node.

In weighted graph the **time complexity** of Dijkstra is *O(V^2)*. In unweighted graph it can be used the breadth-first search (BFS) to solve the problem with *O(V+E)* time complexity.


Implementation
---------------

Methods
--------


Applications
------------

- The problem of finding the shortest path between two intersections on a road map may be modeled as a special case of the shortest path problem in graphs, where the vertices correspond to intersections and the edges correspond to road segments, each weighted by the length of the segment. 

- Shortest path algorithms are applied to automatically find directions between physical locations, such as driving directions on web mapping websites like MapQuest or Google Maps.

- If vertices represent the states of a puzzle like a **Rubik's Cube** and each directed edge corresponds to a single move or turn, shortest path algorithms can be used to find a solution that uses the minimum possible number of moves. 

- Different applications in [operations research](https://en.wikipedia.org/wiki/Operations_research), include plant and facility layout, robotics, transportation, and VLSI design.

- The [Euclidean shortest path problem](https://en.wikipedia.org/wiki/Euclidean_shortest_path) is a problem in computational geometry: given a set of polyhedral obstacles in a Euclidean space, and two points, find the shortest path between the points that does not intersect any of the obstacles. The algorithms used to solve this problem are based on two different principles: (i) performing a shortest path algorithm such as Dijkstra's algorithm on a visibility graph derived from the obstacles or (ii) propagating a wavefront from one of the points until it meets the other (an approach called continuous Dijkstra).

- The [travelling salesman problem](https://en.wikipedia.org/wiki/Shortest_path_problem) is the problem of finding the shortest path that goes through every vertex exactly once, and returns to the start. Unlike the shortest path problem, which can be solved in polynomial time in graphs without negative cycles, the travelling salesman problem is NP-complete and, as such, is believed not to be efficiently solvable for large sets of data (see P = NP problem). The problem of finding the longest path in a graph is also NP-complete. 

- The Canadian traveller problem and the **stochastic shortest path problem** are generalizations where either the graph is not completely known to the mover, changes over time, or where actions (traversals) are probabilistic.


Quiz
-----


Material
--------
- **Coursera Algorithms Part 2**: week 
- **Algorithms**, Sedgewick and Wayne (2014): Chapter  ""
