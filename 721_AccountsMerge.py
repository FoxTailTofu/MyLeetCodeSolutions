from pprint import pprint
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # generate union find data
        uf = UnionFind(len(accounts))
        known_emails = {}
        for index, account in enumerate(accounts):
            emails = account[1::]
            for email in emails:
                known_index = known_emails.get(email)
                
                if known_index is not None:
                    uf.union(index,known_index)
                else:
                    known_emails[email] = index

        # create merged accounts
        merged = [[] for _ in range(len(accounts))]
        for index in range(len(merged)):
            emails = accounts[index][1::]
            union_index = uf.find(index)
            merged[union_index].extend(emails)

        # remove duplicated email and sort
        for index in range(len(merged)):
            emails = merged[index]
            emails = list(set(emails))
            emails.sort()
            emails.insert(0, accounts[index][0])  # insert name at front
            merged[index] = emails
        
        merged = [x for x in merged if len(x) != 1]
        return merged


def validate(input, wanted):
    result = (Solution()).accountsMerge(input)
    if result == wanted:
        print("OK")
    else:
        print("Failed")
        print("I: ", input)
        print("O: ", result)
        print("E: ", wanted)


# validate([["J","Mail1"],["K","Mail2"],["J","Mail1"]],[["J","Mail1"],["K","Mail2"]])
# validate(
#     [
#         ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#         ["John", "johnsmith@mail.com", "john00@mail.com"],
#         ["Mary", "mary@mail.com"],
#         ["John", "johnnybravo@mail.com"],
#     ],
#     [
#         ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
#         ["Mary", "mary@mail.com"],
#         ["John", "johnnybravo@mail.com"],
#     ],
# )
# validate(
#     [
#         ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
#         ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
#         ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
#         ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
#         ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
#     ],[
#         ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
#         ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
#         ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
#         ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
#         ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
#     ]
# )

# validate(
#     [
#         ["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
#         ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
#         ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
#         ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
#         ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]
#     ], [
#         ["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],
#         ["Ethan","Ethan0@m.co","Ethan3@m.co"],
#         ["Kevin","Kevin2@m.co","Kevin4@m.co"],
#         ["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"]
#     ]
# )

# validate(
#     [
#         ["David","David0@m.co","David1@m.co"],
#         ["David","David3@m.co","David4@m.co"],
#         ["David","David4@m.co","David5@m.co"],
#         ["David","David2@m.co","David3@m.co"],
#         ["David","David1@m.co","David2@m.co"]
#     ],[
#         ["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]
#     ]
# )


validate([["David","David4@m.co","David2@m.co","David4@m.co"],["John","John7@m.co","John5@m.co","John3@m.co"],["Fern","Fern6@m.co","Fern4@m.co","Fern5@m.co"],["Celine","Celine0@m.co","Celine7@m.co","Celine7@m.co"],["Gabe","Gabe8@m.co","Gabe8@m.co","Gabe1@m.co"],["Ethan","Ethan1@m.co","Ethan6@m.co","Ethan6@m.co"],["Celine","Celine4@m.co","Celine8@m.co","Celine6@m.co"],["Celine","Celine0@m.co","Celine0@m.co","Celine4@m.co"]]

,[["David","David2@m.co","David4@m.co"],["John","John3@m.co","John5@m.co","John7@m.co"],["Fern","Fern4@m.co","Fern5@m.co","Fern6@m.co"],["Gabe","Gabe1@m.co","Gabe8@m.co"],["Ethan","Ethan1@m.co","Ethan6@m.co"],["Celine","Celine0@m.co","Celine4@m.co","Celine6@m.co","Celine7@m.co","Celine8@m.co"]]
)