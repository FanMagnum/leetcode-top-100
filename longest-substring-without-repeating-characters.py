class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
            lookup.add(s[i])
        return max_len


    def lengthOfLongestSubstringV2(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)  # 更新左指针 i
            dic[s[j]] = j  # 哈希表记录
            res = max(res, j - i)  # 更新结果
        return res