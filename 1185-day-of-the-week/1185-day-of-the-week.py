import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Create a date object and format it to return the full weekday name
        return datetime.date(year, month, day).strftime("%A")
