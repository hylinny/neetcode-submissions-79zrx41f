class Solution:
    def minOperations(self, logs: List[str]) -> int:
        offset = 0
        for log in logs:
            if log == '../':
                # if offset already in main folder (0), we remain
                if offset > 0:
                    offset -= 1
            elif log == './':
                continue
            else: # move to child folder
                offset += 1
        return offset