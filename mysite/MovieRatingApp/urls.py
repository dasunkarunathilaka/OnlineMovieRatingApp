from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index' ),
    url(r'^searchresults$', views.searchResults, name = 'searchResults' ),

    # User auth urls
    url(r'^accounts/login$', views.customLogin, name = 'login' ),
    url(r'^accounts/auth$', views.userAuth, name = 'auth' ),
    url(r'^accounts/loggedin$', views.loggedin, name = 'loggedin' ),
    url(r'^accounts/logout$', views.logout, name = 'logout' ),
    url(r'^accounts/invalid$', views.invalidLogin, name = 'invalid' ),

	url(r'^accounts/signup$', views.signupUser, name = 'signup' ),    
	url(r'^accounts/signedup$', views.signupSuccess, name = 'signedup' ),    
]
