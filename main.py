from datetime import datetime

def get_days_from_today(date: str) -> int:
   try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
   except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

print(get_days_from_today("2021-10-09"))



import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    if not (1 <= min <= max <= 1000):
        return []
    if not (0 < quantity <= (max - min + 1)):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



