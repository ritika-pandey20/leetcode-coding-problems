class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)
        for i in s_dict:
            if i in t_dict:
                if t_dict[i] != s_dict[i]:
                    return False
            else:
                return False
        for i in t_dict:
            if i in s_dict:
                if s_dict[i] != t_dict[i]:
                    return False
            else:
                return False
        return True