class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # size of the pattern is strictly 3
        arr = list(zip(timestamp, username, website))
        arr.sort()
        hashmap = defaultdict(list)
        for time, user, site in arr:
            hashmap[user].append(site)
        # Now, we have hashmap of each user 
        # and their chronological web visits
        count = defaultdict(int)
        for user in hashmap:
            sites = hashmap[user]
            patterns = set()
            for i in range(len(sites)):
                for j in range(i+1, len(sites)):
                    for k in range(j+1, len(sites)):
                        patterns.add((sites[i], sites[j], sites[k]))
            for p in patterns:
                count[p] += 1
        output = set()
        c = 0
        for pattern, freq in count.items():
            if freq > c or (freq == c and pattern < output):
                c = freq
                output = pattern
        return list(output)

