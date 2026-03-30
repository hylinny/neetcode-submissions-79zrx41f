class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()
        for email in emails:
            string = []
            i = 0
            while i < len(email):
                if email[i] == '@':
                    string.append(email[i:])
                    break
                elif email[i] == '.':
                    i += 1
                    continue
                elif email[i] == '+':
                    while i < len(email) and email[i] != '@':
                        i += 1
                    string.append(email[i:])
                else:
                    string.append(email[i])
                    i += 1
            hashset.add(''.join(string))
        return len(hashset)
            