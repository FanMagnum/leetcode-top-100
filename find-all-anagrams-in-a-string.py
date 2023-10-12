from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m:
            return res
        p_counter, s_counter = [0] * 26, [0] * 26
        for i in range(m):
            p_counter[ord(p[i]) - ord('a')] += 1
            s_counter[ord(s[i]) - ord('a')] += 1
        if p_counter == s_counter:
            res.append(0)
        for i in range(m, n):
            s_counter[ord(s[i]) - ord('a')] += 1
            s_counter[ord(s[i - m]) - ord('a')] -= 1
            if s_counter == p_counter:
                res.append(i - m + 1)
        return res

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))