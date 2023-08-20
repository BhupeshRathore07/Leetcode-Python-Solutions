# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

# Return a sorted list of the items such that:

# The items that belong to the same group are next to each other in the sorted list.
# There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty list if there is no solution.

# Example 1:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]
# Example 2:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 
# Constraints:

# 1 <= m <= n <= 3 * 104
# group.length == beforeItems.length == n
# -1 <= group[i] <= m - 1
# 0 <= beforeItems[i].length <= n - 1
# 0 <= beforeItems[i][j] <= n - 1
# i != beforeItems[i][j]
# beforeItems[i] does not contain duplicates elements.









class Solution:
    def sortItems(self, n: int, m: int, group: List[int], pres: List[List[int]]) -> List[int]:
        max_group_id, project_indegree, group_indegree, project_neighbors, group_neighbors, group_projects, result = m, defaultdict(int), defaultdict(int), defaultdict(list), defaultdict(list), defaultdict(list), []
        for project in range(n):
            if group[project] == -1:
                group[project] = max_group_id
                max_group_id += 1
        for project in range(n):
            group_projects[group[project]].append(project)
            for pre in pres[project]:
                if group[pre] != group[project]:
                    group_indegree[group[project]] += 1
                    group_neighbors[group[pre]].append(group[project])
                else:
                    project_indegree[project] += 1
                    project_neighbors[pre].append(project)
                    
        def top_sort (items: List[int], indegree: Dict[int, int], neighbors: Dict[int, List[int]]) -> List[int]:
            q, result = collections.deque([item for item in items if not indegree[item]]), []
            while q:
                result.append(cur := q.popleft())
                for neighbor in neighbors[cur]:
                    indegree[neighbor] -= 1
                    if not indegree[neighbor]:
                        q.append(neighbor)
            return result
        group_queue = top_sort([i for i in range(max_group_id)], group_indegree, group_neighbors)
        if len(group_queue) != max_group_id:
            return result
        for group_id in group_queue:
            project_queue = top_sort(group_projects[group_id], project_indegree, project_neighbors)
            if len(project_queue) != len(group_projects[group_id]):
                return []
            result += project_queue
        return result




