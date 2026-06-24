class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # basically, if theres email overlap, merge
        # email overlap will always have same name
        # step 1: build hashmap email -> name
        # step 2: build ufds
        # step 3: build output with root node as name placeholder
        # step 4: convert root node email to names
        emailToName = {}
        ufds = {}
        for account in accounts:
            for i in range(1, len(account)):
                emailToName[account[i]] = account[0]
                ufds[account[i]] = account[i]

        def find(email):
            if ufds[email] == email:
                return email
            ufds[email] = find(ufds[email])
            return ufds[email]
        
        def union(email1, email2):
            ufds[find(email1)] = find(email2)

        for account in accounts:
            email = account[1]
            for i in range(2, len(account)):
                union(email, account[i])

        outputMap = defaultdict(set) # set for dedup
        for email, _ in emailToName.items():
            outputMap[find(email)].add(email)
        
        output = []
        for rootEmail, emails in outputMap.items():
            acc = []
            acc.append(emailToName[rootEmail])
            acc.extend(sorted(emails))
            output.append(acc)
        
        return output


            

        

        