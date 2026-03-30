class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hashmap = defaultdict(int)
        for i in range(len(hand)):
            hashmap[hand[i]] += 1
        for num in hand:
            if hashmap[num]:
                for i in range(num, num + groupSize):
                    if not hashmap[i]:
                        return False
                    hashmap[i] -= 1
        return True
