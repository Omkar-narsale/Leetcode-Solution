class Solution(object):
    def daysBetweenDates(self, date1, date2):
        from datetime import datetime
        d1=datetime.strptime(date1,"%Y-%m-%d")
        d2=datetime.strptime(date2,"%Y-%m-%d")
        diff=abs((d2-d1).days)
        return diff
    