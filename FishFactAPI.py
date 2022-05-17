import requests

class FishFactAPI:
  FISHAPIURL = "https://www.fishwatch.gov/api/species"

  def __init__(self):
    pass
    
  def get(self):
      return (requests.get("https://www.fishwatch.gov/api/species".text)

#sends random fish fact to user