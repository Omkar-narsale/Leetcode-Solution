class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            # Skip duplicate i values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                else:
                    result.append([nums[i], nums[j], nums[k]])

                    # Skip duplicate j values
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    # Skip duplicate k values
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

        return result