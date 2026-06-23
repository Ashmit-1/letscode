class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {}
        for num in nums:
            if num in seen:
                continue
            count = 1
            i = num - 1
            while True:
                if i in seen:
                    seen[i] += 1
                    if seen[i] == 1:
                        count += 1
                        break
                    else:
                        i -= 1
                        count+=1
                else:
                    break
            i = num + 1
            while True:
                if i in seen:
                    seen[i] += 1
                    if seen[i] == 1:
                        count += 1
                        break
                    else:
                        i += 1
                        count+=1
                else:
                    break
            seen[num] = count
        # print(seen)
        return max(seen.values())
            

                

        