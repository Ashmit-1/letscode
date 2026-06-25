class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 0: return 0
        if n <= 1: return 1
        characters = dict()
        left = 0
        right = 1
        maxLen = 0
        characters[s[0]] = 1
        res = 0
        while right < n:
            if s[right] in characters:
                characters[s[left]] -= 1
                if characters[s[left]] == 0: del characters[s[left]]
                left+=1
            
            if s[right] not in characters:
                characters[s[right]] = 1
            else: characters[s[right]]+=1
            right+=1

            if len(characters) == (right - left ): 
                maxLen=max(maxLen, right-left)
            else:
                characters[s[left]] -= 1
                if characters[s[left]] == 0: del characters[s[left]]
                left+=1
            

           
        return maxLen

        