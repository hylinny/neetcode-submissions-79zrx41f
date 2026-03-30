class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            bit = (n >> i) & 1        # 0 or 1
            output = (output << 1) | bit
        return output


        