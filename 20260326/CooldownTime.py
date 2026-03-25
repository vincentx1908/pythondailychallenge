from datetime import datetime
def can_retake(finish_time, current_time):
  f_time = datetime.fromisoformat(finish_time)
  c_time = datetime.fromisoformat(current_time)

  delta = c_time - f_time

  return (delta.total_seconds.() / 3600) >= 48

# Actually straightforward calculation of two times with the import of datetime.
# only thing to notice is that as the format of the imput time is "2026-03-25T14:00:00",
# Python can directly decode the ISO format datetime with datetime.fromisoformat.
