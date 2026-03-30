class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        j = 0
        for i in range(len(strs)):
            string = strs[i]
            sortedstring = "".join(sorted(string))
            if sortedstring in hashmap:
                continue
            hashmap[sortedstring] = -1
        output = []
        j = 0
        for str in strs:
            sortedstring = "".join(sorted(str))
            if hashmap[sortedstring] == -1:
                hashmap[sortedstring] = j
                j += 1
                output.append([str])
            else:
                hashmap[sortedstring]
                output[hashmap[sortedstring]].append(str)
        return output
            

        