from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib import auth
from django.core.context_processors import csrf
# Cross Site Request Forgery - pass a token to every POST method, check the returned forms token with the sent token. This token changes with each request.

# Twitter analyzing imports
from . import twitterConnector
from analyzeSentiment import analyze
from rateCalculator import calculateRating
from tweetDisplayer import displayTweets

# User registration
from forms import UserForm
from django.contrib.auth import login, authenticate

from youtubeConnector import youtubeSearch


def index(request):
    # Loads the homepage.
    return render(request, 'movieratingapp/index.html')


def searchResults(request):
    # Loads the result output page.
    twitterConnectorObj = twitterConnector.twitterConnector()
    userInput = request.POST.get('name', None)
    # To get the movie name, entered by the user.

    modifiedUserInput = userInputModifier(userInput)
    twitterConnectorObj.searchTwitter(modifiedUserInput)

    tweetCount = twitterConnectorObj.numberOfTweets()

    if tweetCount > 15:
        analyze()
        ratedValue = calculateRating()
        sample_tweets = displayTweets()
        # A list of tuples (text, username) is returned.

        videoURL = youtubeSearch(userInput)

        return render(request, 'movieratingapp/searchResults.html',
                      {'movie_name': userInput, 'rating': ratedValue, 'firstText': sample_tweets[0][0],
                       'firstUser': sample_tweets[0][1], 'secondText': sample_tweets[1][0],
                       'secondUser': sample_tweets[1][1], 'videoURL': videoURL})

    else:
        return render(request, 'movieratingapp/searchResultsError.html')


def customLogin(request):
    # To identify whether a user has already logged in or not.
    if request.user.is_authenticated():
        return HttpResponseRedirect('/movieratingapp/')
    else:
        return userLogin(request)


def userLogin(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'movieratingapp/login.html', c)


def userAuth(request):
    # When user submits the login form, it comes here.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    # If there is no value returned, empty string is returned by the second parameter.

    user = auth.authenticate(username=username, password=password)
    # If there is no user matching username and password, return None object. None = Null

    if user is not None:
        auth.login(request, user)
        # Set the current user's status to logged in.

        # Follwing returns a url... it will be checked in the urls.py to decide what to do.
        # render returns a html page. So the correct path should be given to that file.
        return HttpResponseRedirect('loggedin')
    # user is already in the 'movieratingapp/accounts/' url. we need to give the next location only.

    else:
        return HttpResponseRedirect('invalid')


def loggedin(request):
    return render(request, 'movieratingapp/loggedin.html', {'user_name': request.user.first_name})


def invalidLogin(request):
    return render(request, 'movieratingapp/invalid.html')


def logout(request):
    auth.logout(request)
    return render(request, 'movieratingapp/logout.html')


def signupUser(request):
    if request.method == 'POST':
        # Only when user submits the form, POST method is called.

        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            # as soon as a new user is created, he is logged into the system.

            return HttpResponseRedirect('signedup')

    else:
        form = UserForm().as_ul()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render(request, 'movieratingapp/signup.html', args)


def signupSuccess(request):
    return render(request, 'movieratingapp/signedup.html')


def userInputModifier(userInput):
    # To get a input which is suitable for twitter search.

    userInput = userInput.strip().replace(" ", "")
    # For movie names with multiple words.

    userInput = '#' + userInput
    return userInput
