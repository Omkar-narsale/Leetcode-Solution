class Solution(object):
    def findRestaurant(self, list1, list2):
        min_sum = float('inf')
        result = []

        common = [words for words in list1 if words in list2]

        for words in common:
            total = list1.index(words) + list2.index(words)

            if total < min_sum:
                min_sum = total
                result = [words]

            elif total == min_sum:
                result.append(words)

        return result