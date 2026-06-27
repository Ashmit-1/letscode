class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_arr = [0] * 26
        for ch in s1:
            s1_arr[ord(ch) - ord('a')]+=1
        s2_arr = [0] * 26

        for ch in s2[:len(s1)]:
            s2_arr[ord(ch) - ord('a')]+=1
        
        if s1_arr == s2_arr:
            return True
        
        left = 0
        for i in range(len(s1), len(s2)):
            s2_arr[ord(s2[left]) - ord('a')]-=1
            left+=1
            s2_arr[ord(s2[i]) - ord('a')]+=1
            if s1_arr == s2_arr:
                return True
        return False

        