def get_shadow(time):
    h, m = map(int, time.split(":"))
    now = h * 60 + m
    sunrise = 6 * 60
    sunset = 18 * 60
    noon = 12 * 60
    if now < sunrise:
        return "No shadow"
    elif sunrise <= now < noon:
        shadow = ((noon - now) / 60) ** 3
        return f"{shadow:g}ft west"
    elif now == noon:
        return "No shadow"
    elif noon < now < sunset:
        shadow = ((now - noon) /60) ** 3
        return f"{shadow:g}ft east"
    else:
        return "No shadow"


# For most time difference calculations, it is typical method to transfer time to minutes/hours.
