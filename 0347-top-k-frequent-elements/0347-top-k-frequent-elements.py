class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        freq=Counter(nums)
        most_common_val=freq.most_common(k)
        result=[num for num,count in most_common_val ]
        return result
        
        