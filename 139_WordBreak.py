import time


class Solution:

    # ref: https://www.youtube.com/watch?v=Sx9NNgInc3A

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for index in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if index + len(word) > len(s):
                    continue
                if s[index : index + len(word)] == word:
                    dp[index] = dp[index + len(word)]
                if dp[index]:
                    break
            # print(index, dp)

        return dp[0]

    # con: store too many information
    # pro: might be useful in WordBreak2, where we need to return all the solutions
    def wordBreak_accepted(self, s: str, wordDict: list[str]) -> bool:
        #  arr = [[]] * len(s) stored the address of same array in every slot, causing any write to any index also write to all the slots
        map = [[] for _ in range(len(s))]

        # build the traverse map
        for word in wordDict:
            ptr = 0
            while ptr < len(s):
                result = s.find(word, ptr)
                if result == -1:
                    break
                map[result].append(result + len(word))
                ptr = result + 1

        # find path to len(s)
        paths = [0]
        while len(paths):
            path = paths.pop(0)  # pop first element
            if path == len(s):
                return True

            for node in map[path]:
                if node not in paths:
                    paths.append(node)

        return False

    # don't work for aaaaaaa..b,["a","aa"..."aaaa"]
    def wordBreak_bruteforce(self, s: str, wordDict: list[str]) -> bool:
        ptrs = [0]
        while len(ptrs):
            ptr = ptrs.pop()
            for word in wordDict:
                new_ptr = ptr + len(word)

                if s[ptr::].find(word) != 0:
                    continue

                if new_ptr == len(s):
                    return True
                ptrs.append(new_ptr)

        return False


def validate(s, wordDict, exp):
    start = time.time()
    result = (Solution()).wordBreak(s, wordDict)

    if result != exp:
        print(s, wordDict, exp, result)
    print("--T: {:.2f}".format(time.time() - start))


validate("leetcode", ["leet", "code"], True)
validate("applepenapple", ["apple", "pen"], True)
validate("a", ["a"], True)
validate("aaaaa", ["a"], True)
validate("catsandog", ["cats", "dog", "sand", "cat"], False)
validate("catsandogcat", ["cats", "dog", "sand", "cat"], False)
validate("catsandogcat", ["cats", "dog", "sand", "and", "cat", "an"], True)
validate("abcd", ["a", "abc", "b", "cd"], True)
validate("abcd", ["a", "b", "cd", "abc"], True)
# validate(
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
#     [
#         "a",
#         "aa",
#         "aaa",
#         "aaaa",
#         "aaaaa",
#     ],
#     False,
# )
