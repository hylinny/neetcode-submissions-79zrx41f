import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by start time
        # choose to take current job and bisect_left for next non-overlap interval index, or choose to skip 
        # return maximum profit
        # base case: no jobs left (i = n), return 0
        # optimal substructure: assume we have an optimal choice of jobs S. we split our solution into S and S' = S \ earliest job, and J' = J \ jobs that overlap with earliest job. Assume we have a better choice of jobs for J' = Sbetter, then we replace S' in S with Sbetter, resulting in an overall better choice of jobs. Contradiction!
        jobs = []
        for s, e, p in zip(startTime, endTime, profit):
            jobs.append((s, e, p))
        jobs.sort(key=lambda x: x[0])
        startTimes = [job[0] for job in jobs]
        n = len(jobs)
        dp = {}
        def solve(i):
            if i in dp:
                return dp[i]
            if i == n:
                return 0
            skip = solve(i+1)
            start, end, profit = jobs[i]
            j = bisect.bisect_left(startTimes, end)
            take = solve(j) + profit
            dp[i] = max(skip, take)
            return dp[i]
        return solve(0)