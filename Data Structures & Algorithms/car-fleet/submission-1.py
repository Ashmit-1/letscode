class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(sorted(zip(position, speed), key=lambda x: x[0], reverse = True))  
        time = []
        count = 0
        for i in pos_speed:
            pos = i[0]
            v = i[1]
            t = (target - pos) / v
            if not time or t > time[-1]:
                time.append(t)
                count+=1          
         
        return count
        