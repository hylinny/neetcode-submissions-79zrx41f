class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # "7868190130M7522"
        # phone number: 7868190130
        # gender: M
        # age: 75
        # seat: 22
        output = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                output += 1
        return output