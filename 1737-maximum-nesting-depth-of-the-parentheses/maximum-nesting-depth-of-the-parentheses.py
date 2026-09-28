class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        par=0
        for i in s:
            if i == '(':
                par+=1
                maxi=max(maxi,par)
            elif i==')':
                par-=1
        return maxi