# import python math function
import math

def perfect_cube_count(a, b):
  low = min(a, b)
  high = max(a, b)

  start = math.ceil(math.cbrt(low))
  end = math.floor(math.cbrt(high))

  count = 0
  for i in range(start, end + 1):
    if low <= i ** 3 <= high:
      count += 1

  return count
