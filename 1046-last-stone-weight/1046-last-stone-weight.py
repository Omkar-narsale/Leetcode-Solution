class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            first_highest = stones[-1]
            second_highest = stones[-2]

            if first_highest > second_highest:
                stones.remove(first_highest)
                stones.remove(second_highest)
                stones.append(first_highest - second_highest)
            else:
                stones.remove(first_highest)
                stones.remove(second_highest)

        if len(stones) == 0:
            return 0

        return stones[0]