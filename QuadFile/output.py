from datetime import datetime
import time

# TODO: I dunno, but there's gotta be a better way to do this crap. This is way too messy

# Some messages pass a True or False as should_print depending on config variables
# Default to true, but return doing nothing if they pass a False.
def print_log(source, message, should_print=True):
  if should_print == False:
    return

  if source == "Main":
    print('\033[92m', current_time(), source.center(8, '-'), ': \033[0m', message)
  elif source == "Notice":
    print('\033[93m', current_time(), source.center(8, '-'), ': \033[0m', message)
  elif source == "Warning":
    print('\033[91m', current_time(), source.center(8, '-'), ': \033[0m', message)
  elif source == "Web":
    print('\033[95m', current_time(), source.center(8, '-'), ': \033[0m', message)
  else:
    print('\033[94m', current_time(), source.center(8, '-'), ': \033[0m', message)

def current_time():
  return time_to_string(time.time(), True)

def time_to_string(unixtime, time_only = False):
  if time_only:
    return datetime.fromtimestamp(unixtime).strftime('[%H:%M:%S - ' + time.tzname[time.daylight] + ']')
  else:
    return datetime.fromtimestamp(unixtime).strftime('%B %d, %Y (%H:%M:%S - ' + time.tzname[time.daylight] + ')')
