import main

datadict=main.getCrawl()


for item in datadict:
  for key in item.keys():
    print(key)
