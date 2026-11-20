class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [False] * (n + 1)
        memo[len(s)] = True
        

        for i in range(n - 1, -1, -1): #bottom-up approach O(n^2*m), where m is the words in wordict and n is string traversals 
            for word in wordDict:
                if (len(word) + i) <= len(s) and s[i: i + len(word)] == word:
                    memo[i] = memo[i + len(word)]
                if memo[i]:
                    break

        return memo[0]          
