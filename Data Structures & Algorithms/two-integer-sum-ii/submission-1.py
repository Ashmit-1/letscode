class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(arr, left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    return mid
                
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        n = len(numbers)
        for i, num in enumerate(numbers):
            res = binarySearch(numbers, i+1, n-1, target - num)
            print(num, res, target - num)
            if res:
                return [i+1,res+1]
        
        


        