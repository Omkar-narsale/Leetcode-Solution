class Solution:
    def maxDigitRange(self,nums:list[int])->int:
        max_range=0
        total=0
        for i in range(len(nums)):
            original_number=nums[i]
            temp=nums[i]
            max_digit=0
            min_digit=9
            while temp>0:
                digit=temp%10
                max_digit=max(max_digit,digit)
                min_digit=min(min_digit,digit)
                temp=temp//10
            digit_range=max_digit-min_digit
            if digit_range>max_range:
                max_range=digit_range
                total=original_number
            elif digit_range==max_range:
                total+=original_number
        return total