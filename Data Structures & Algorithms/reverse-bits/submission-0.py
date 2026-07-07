class Solution:
    def reverseBits(self, n: int) -> int:
        return int(('0'*32 + bin(n)[2:])[::-1][:32], 2)

        