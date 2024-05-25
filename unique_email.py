# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails):
        result = set()
        for email in emails:
            local, domain = email.split("@")
            new = ""
            for i in local:
                if i == '.':
                    continue
                elif i == '+':
                    break
                else:
                    new += i
            result.add(new + "@" + domain)

        return len(result)


obj = Solution()
print(obj.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))