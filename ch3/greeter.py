import datetime

class Greeter:
    def __init__(self, store):
        self.store = store
    def _day(self) -> str:
        current_datetime = datetime.datetime.now()
        return current_datetime.strftime('%A') # .strftime returns str representing date and time using date, time or datetime object.

    def _part_of_day(self):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
           return 'morning'
        elif current_hour >= 12 and current_hour < 17:
            return 'afternoon'
        else:
            return 'evening'

    def greet(self):
        print(f"Hi, welcome to {self.store}!")
        print(f"How's your {self._day()} {self._part_of_day()} going?")
        print(f"Here's a coupon for 20% off!")