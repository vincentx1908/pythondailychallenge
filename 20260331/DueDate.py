from calendar import monthrange
def get_due_date(date_str):
    year, month, day = map(int, date_str.split("-"))
    month += 9
    year += (month - 1) // 12
    month = (month - 1) % 12 + 1
    last_day = monthrange(year, month)[1]

    day = min(day, last_day)


    return f"{year:04d}-{month:02d}-{day:02d}"


# The key to complete this challenge is the import of monthrange.
# Apart from that it is straightforward:
# 1. Add 9 months to the month number,
# 2. Update the year number, and thus update the month number
# 3. Check the day number to see if it's outside the month range.
