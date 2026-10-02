class Solution(object):
    def checkPrimeFrequency(self, nums):
        from collections import Counter
        freq = Counter(nums)
        for num, count in freq.items():
            if count < 2:
                continue
            prime = True
            for i in range(2, count):
                if count % i == 0:
                    prime = False
                    break
            if prime:
                return True
        return False