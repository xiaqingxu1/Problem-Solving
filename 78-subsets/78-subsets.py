class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if not nums:
            return res

        for n in nums:
            newRow = []
            for subset in res:
                if subset:
                    s = subset[:]
                    s.append(n)
                    newRow.append(s)
            newRow.append([n])
            res.extend(newRow)

        return res