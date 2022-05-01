
import json


with open("db.json","r") as inFile:
  with open ("output.json","w") as outFile:
      data = json.load(inFile)
      index = 1
      listOfCitys = [ ]
      for city in data:
        currentCity =  {
        "model": "api.satecity",
        "pk": index,
        "fields": {
          "city": city['city'],
          "growth": city['growth_from_2000_to_2013'],
          "latitude": str(city['latitude']),
          "longitude": str(city['longitude']),
          "population": int(city['population']),
          "rank": int(city['rank']),
          "state": city['state']
          }
        }
        listOfCitys.append(currentCity)
        index = index + 1
      json.dump(listOfCitys, outFile)

