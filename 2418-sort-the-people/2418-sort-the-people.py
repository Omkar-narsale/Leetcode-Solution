class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        pairs = sorted(zip(heights, names), reverse=True)
        return [name for height, name in pairs]