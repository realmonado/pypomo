import time as t
from alive_progress import alive_bar
from rich.console import Console
from rich.markdown import Markdown

while True:
            
  console = Console()
  with open("welcome.md") as welcome:
    markdown = Markdown(welcome.read())
    console.print(markdown)
    
  x = int(input())

  if x==1:
    items = range(1501)

  elif x==2:
    items = range(301) # 301

  elif x==3:
    items = range(901)

  with alive_bar(len(items)) as bar:
    for i in items:
      t.sleep(1)
      bar()

      continue


