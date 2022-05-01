from django.shortcuts import render
import json
  
# create a function
def index(request):
    # create a dictionary to pass
    # data to the template
    inFile = open ("db.json","r")
    data = json.load(inFile)
    page = 1
    itemsPerPage = 10
    list_of_cities = data[0:itemsPerPage-1]
    example_Data = {
      "list_of_cities":data,
      "currentPage":page
    }
    return render(request, "frontendapp/index.html",example_Data)