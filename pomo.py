import time
import datetime
from time import sleep
from alive_progress import alive_bar
from rich.console import Console
from rich.markdown import Markdown

def countdown_timer(secs, now=datetime.datetime.now):
  target = now()
  one_second_later = datetime.timedelta(seconds=1)
  with alive_bar(secs) as bar:
    for remaining in range(secs, 0, -1):
      target += one_second_later
      time.sleep((target - now()).total_seconds())
      bar()

while True:
            
  console = Console()
  with open("welcome.md") as welcome:
    markdown = Markdown(welcome.read())
    console.print(markdown)

  choice = input() # as mentioned in welcome.md

  if choice=="1":
    secs = 1500 # 20 minutes

  elif choice=="2":
    secs = 300 # 5 minutes 301

  elif choice=="3":
    secs = 900 # 15 minutes

  else:
    print("DONE")
    break;

  countdown_timer(secs)
  continue
