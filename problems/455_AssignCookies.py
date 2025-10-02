"""
Assign Cookies (LeetCode 455)
贪心：小饼干尽量先满足胃口小的孩子。

Time:  O(n log n)  因为排序
Space: O(1)        原地指针
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_i, c_i = 0, 0
        n_g, n_c = len(g), len(s)
        while g_i < n_g and c_i < n_c:
            if g[g_i] <= s[c_i]:
                g_i += 1
            c_i += 1
        return g_i