class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= k:
                isEqual = True
                for i in range(k):
                    if c != stack[-1-i]:
                        isEqual = False
                if isEqual:
                    for j in range(k):
                        stack.pop()
        return ''.join(stack)
