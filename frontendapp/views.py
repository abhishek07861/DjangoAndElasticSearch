from django.shortcuts import render

  
# create a function
def index(request):
    # create a dictionary to pass
    # data to the template
    example_Data = [{
    "country": "US",
    "name": "Natalia",
    "lat": "29.18968",
    "lng": "-98.86253"
  },
  {
    "country": "US",
    "name": "Bear Creek",
    "lat": "34.27482",
    "lng": "-87.70058"
  },
  {
    "country": "US",
    "name": "Fort Hunt",
    "lat": "38.73289",
    "lng": "-77.05803"
  },
  {
    "country": "US",
    "name": "Yorktown",
    "lat": "37.23876",
    "lng": "-76.50967"
  },
  {
    "country": "US",
    "name": "Brighton",
    "lat": "33.43428",
    "lng": "-86.94721"
  },
  {
    "country": "US",
    "name": "Ocean View",
    "lat": "38.54511",
    "lng": "-75.08907"
  },
  {
    "country": "US",
    "name": "Berry",
    "lat": "33.65983",
    "lng": "-87.60001"
  },
  {
    "country": "US",
    "name": "Trinity",
    "lat": "28.18085",
    "lng": "-82.68177"
  },
  {
    "country": "US",
    "name": "Villas",
    "lat": "26.55035",
    "lng": "-81.8687"
  },
  {
    "country": "US",
    "name": "Bessemer",
    "lat": "33.40178",
    "lng": "-86.95444"
  },
  {
    "country": "US",
    "name": "Aurora",
    "lat": "39.057",
    "lng": "-84.90134"
  },
  {
    "country": "US",
    "name": "New Pekin",
    "lat": "38.50506",
    "lng": "-86.01692"
  },
  {
    "country": "US",
    "name": "Stockton",
    "lat": "39.43807",
    "lng": "-99.2651"
  },
  {
    "country": "US",
    "name": "Paducah",
    "lat": "37.08339",
    "lng": "-88.60005"
  },
  {
    "country": "US",
    "name": "Monticello",
    "lat": "32.59653",
    "lng": "-91.394"
  },
  {
    "country": "US",
    "name": "Red Chute",
    "lat": "32.55598",
    "lng": "-93.61323"
  },
  {
    "country": "US",
    "name": "Jessup",
    "lat": "39.14927",
    "lng": "-76.77525"
  },
  {
    "country": "US",
    "name": "Birmingham",
    "lat": "33.52066",
    "lng": "-86.80249"
  },
  {
    "country": "US",
    "name": "Delhi Hills",
    "lat": "39.09284",
    "lng": "-84.61272"
  },
  {
    "country": "US",
    "name": "Turpin Hills",
    "lat": "39.11006",
    "lng": "-84.37994"
  },
  {
    "country": "US",
    "name": "Lugoff",
    "lat": "34.22737",
    "lng": "-80.68925"
  },
  {
    "country": "US",
    "name": "Blountsville",
    "lat": "34.08149",
    "lng": "-86.5911"
  },
  {
    "country": "US",
    "name": "Blue Ridge",
    "lat": "32.49264",
    "lng": "-86.19052"
  },
  {
    "country": "US",
    "name": "Buda",
    "lat": "30.08521",
    "lng": "-97.84028"
  },
  {
    "country": "US",
    "name": "Boaz",
    "lat": "34.20065",
    "lng": "-86.16637"
  },
  {
    "country": "US",
    "name": "Brent",
    "lat": "32.93735",
    "lng": "-87.16472"
  }]

    return render(request, "frontendapp/index.html",example_Data)