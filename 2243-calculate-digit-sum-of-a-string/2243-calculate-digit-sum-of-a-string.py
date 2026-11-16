class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            groups=[]

            for i in range(0,len(s),k):
                groups.append(s[i:i+k])

            new=''
            for group in groups:
                total=sum(int(digit) for digit in group)
                new+=str(total)
            s=new

        return s