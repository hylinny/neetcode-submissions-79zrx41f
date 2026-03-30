class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # we want to accumulate our change
        # 5, 10, 20
        changes = defaultdict(int)
        for bill in bills:
            changes[bill] += 1
            change = bill - 5
            if change == 0:
                continue
            if change == 5:
                if changes[5] == 0:
                    return False
                changes[5] -= 1
            elif change == 15:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[10] == 0 and changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
        return True
            
            
        