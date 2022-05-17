import requests

class CockatilAPI:
  CATAPIURL = "www.thecocktaildb.com/api/json/v1/1/search.php?f=a"

  def __init__(self):
    pass

  def get(self):              
    return (requests.get("www.thecocktaildb.com/api/json/v1/1/search.php?f=a".text)


#creates return statement sending random cocktail list to user
