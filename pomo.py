import time
from time import sleep
from alive_progress import alive_bar
from rich.console import Console
from rich.markdown import Markdown

while True:
            
  console = Console()
  with open("welcome.md") as welcome:
    markdown = Markdown(welcome.read())
    console.print(markdown)

  choice = input() # as mentioned in welcome.md

  if choice=="1":
    items = range(1500) # 20 minutes

  elif choice=="2":
    items = range(300) # 5 minutes 301

  elif choice=="3":
    items = range(900) # 15 minutes

  else:
    print("DONE")
    break;
  
  start = time.time()

  with alive_bar(len(items)) as bar:
    for i in items:  # HACK using ranges to iterate while also executing bar()
      sleep(1)
      bar()

      continue

  end = time.time()
  print(end-start)
