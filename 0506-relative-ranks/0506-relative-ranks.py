class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [""] * len(score)
        temp = score.copy()

        for i in range(len(score)):
            max_score = max(temp)
            index = score.index(max_score)

            if i == 0:
                ans[index] = "Gold Medal"
            elif i == 1:
                ans[index] = "Silver Medal"
            elif i == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(i + 1)

            temp.remove(max_score)

        return ans

          