# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

# Example 1:

# Input: strs = ["tars","rats","arts","star"]
# Output: 2
# Example 2:

# Input: strs = ["omv","ovm"]
# Output: 1
 

# Constraints:

# 1 <= strs.length <= 300
# 1 <= strs[i].length <= 300
# strs[i] consists of lowercase letters only.
# All words in strs have the same length and are anagrams of each other.




from collections import defaultdict

class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        words = set(strs)
        groups = defaultdict(list)
        # group by combinations
        for word in words:
            vec = [0] * 26
            for c in word:
                vec[ord(c) - 97] += 1
            groups[tuple(vec)].append(word)

        def find_parent(parents, i):
            if parents[i] == i:
                return i
            parents[i] = find_parent(parents, parents[i])
            return parents[i]

        def union(parents, i, j):
            i, j = find_parent(parents, i), find_parent(parents, j)
            if i < j:
                parents[j] = i
            else:
                parents[i] = j

        def num_groups(parents):
            for i in range(len(parents)):
                find_parent(parents, i)
            return len(set(parents))

        def is_adjacent(word1, word2):
            cnt = 0
            for i, c in enumerate(word1):
                if c != word2[i]:
                    cnt += 1
                if cnt >= 3:
                    return False
            return True

        num_similar_groups = 0
        # for each group
        for _, group_words in groups.items():
            parents = [i for i in range(len(group_words))]
            # connect words
            for i in range(len(group_words)):
                for j in range(i+1, len(group_words)):
                    if is_adjacent(group_words[i], group_words[j]):
                        union(parents, i, j)
            num_similar_groups += num_groups(parents)
        return num_similar_groups
      
      
