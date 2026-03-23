# Method 1, the easiest and most straightforward
def detect_roast(beans):
  points = 0
  for bean in beans:
    if bean == "'":
      points += 1
    elif bean == "-":
      points += 2
    elif bean == ".":
      points += 3

  average = points / len(beans)
  if average < 1.75:
    return "Light"
  elif average > 2.5:
    return "Dark"
  else:
    return "Medium"


# Method 2, the more "Pythonic" one
def detect_roast(beans):
    points = 0
    points += sum({"'":1, "-":2, ".":3}.get(bean) for bean in beans)
    average = points / len(beans)
    return "Light" if average < 1.75 else "Dark" if average > 2.5 else "Medium"


