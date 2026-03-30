class Solution:
    def reverseBits(self, n: int) -> int:
        # n is always 32 bits
        output = 0
        for i in range(32):
            bit = n & (1 << i)
            if bit:
                output = (output << 1) + 1
            else:
                output <<= 1
        return output

        