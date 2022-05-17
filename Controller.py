import random
from CocktailAPI import CocktailAPI
from FishFactAPI import DuckPicAPI

def userActionFunction():
  x = int(random.randrange(0,2))
  temp = CocktailAPI()
  temp2 = FishFactAPI()
  
  if x == 1:
    print(temp.get())
    
  if x == 0:
    print(temp2.get())