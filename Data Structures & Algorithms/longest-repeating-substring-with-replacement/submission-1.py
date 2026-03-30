class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        frequency = defaultdict(int)
        left = 0
        maxfrequency = 0
        for i in range(len(s)):
            frequency[s[i]] += 1
            maxfrequency = max(maxfrequency, frequency[s[i]])
            while maxfrequency + k < i - left + 1:
                frequency[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, i - left + 1)
        return maxLength