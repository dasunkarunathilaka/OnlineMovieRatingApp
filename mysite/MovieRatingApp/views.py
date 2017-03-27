from django.shortcuts import render
from . import twitterConnector
from models import Tweet

# Create your views here.

def index (request):
	# Loads the homepage.
    return render(request, 'movieratingapp/index.html')

def searchResults (request):
	# Loads the result output page.

	twitterConnectorObj = twitterConnector.twitterConnector()

	userInput = request.POST.get('name', None)
	userInput = '#' + userInput
	twitterConnectorObj.searchTwitter(userInput)
	return render (request, 'movieratingapp/searchResults.html')
