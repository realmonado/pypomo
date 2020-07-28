import alive_progress
import datetime
import time

def countdown_timer(x, now=datetime.datetime.now):
    target = now()
    one_second_later = datetime.timedelta(seconds=1)
    with alive_progress.alive_bar(x) as bar:
        for remaining in range(x, 0, -1):
            target += one_second_later
            time.sleep((target - now()).total_seconds())
            bar()

start = time.time()

countdown_timer(300)

stop = time.time()

print(stop-start)
