import math

def calculate_parking_fee(park_time, pickup_time):
    sh, sm = map(int, park_time.split(":"))
    start = 60 * sh + sm
    eh, em = map(int, pickup_time.split(":"))
    end = 60 * eh + em
    parking_fee = 0
    over_night_fee = 0

    if end < start:
        over_night_fee = 10
        end += 24 * 60
    hours_parked = math.ceil((end - start) / 60)

    parking_fee = max(5, 3 * hours_parked + over_night_fee)

    return f"${parking_fee}"


# First time got praised by ChatGPT 😂
# parking_fee = max(5, 3 * hours_parked + over_night_fee) is actually a smart way to set the minimum parking fee
