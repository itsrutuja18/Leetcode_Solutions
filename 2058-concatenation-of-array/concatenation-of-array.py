class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n=[]
        for j in range(2):
            for i in nums:
                n.append(i)
        return n