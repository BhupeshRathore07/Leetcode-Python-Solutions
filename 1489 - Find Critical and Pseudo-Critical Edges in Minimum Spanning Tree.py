# Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

# Note that you can return the indices of the edges in any order.

# Example 1:

# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:

# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
# Example 2:

# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

# Constraints:

# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= ai < bi < n
# 1 <= weighti <= 1000
# All pairs (ai, bi) are distinct.








class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
            if self.rank[rootX] == self.rank[rootY]:
                self.rank[rootY] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: [[int]]) -> [[int]]:
        def dfs(node, depth, ancestor):
            levels[node] = depth
            for neighbor, edge_index in adjacency_list[node]:
                if neighbor == ancestor:
                    continue
                if levels[neighbor] == -1:
                    levels[node] = min(levels[node], dfs(neighbor, depth + 1, node))
                else:
                    levels[node] = min(levels[node], levels[neighbor])
                if levels[neighbor] >= depth + 1 and edge_index not in pseudo_critical:
                    critical.add(edge_index)
            return levels[node]

        critical, pseudo_critical = set(), set()

        weight_to_edges = {w: [] for _, _, w in edges}
        for i, (u, v, w) in enumerate(edges):
            weight_to_edges[w].append([u, v, i])

        union_find = UnionFind(n)

        for weight in sorted(weight_to_edges):
            edge_lookup = defaultdict(set)

            for u, v, edge_index in weight_to_edges[weight]:
                rootU, rootV = union_find.find(u), union_find.find(v)

                if rootU != rootV:
                    union_pair = tuple(sorted((rootU, rootV)))
                    edge_lookup[union_pair].add(edge_index)

            mst_edges, adjacency_list = [], defaultdict(list)

            for (rootU, rootV), edge_indexes in edge_lookup.items():
                if len(edge_indexes) > 1:
                    pseudo_critical.update(edge_indexes)

                edge_idx = edge_indexes.pop()
                adjacency_list[rootU].append((rootV, edge_idx))
                adjacency_list[rootV].append((rootU, edge_idx))
                mst_edges.append((rootU, rootV, edge_idx))
                union_find.union(rootU, rootV)

            levels = [-1] * n

            for u, v, _ in mst_edges:
                if levels[u] == -1:
                    dfs(u, 0, -1)

            for _, _, edge_index in mst_edges:
                if edge_index not in critical:
                    pseudo_critical.add(edge_index)

        return [list(critical), list(pseudo_critical)]






