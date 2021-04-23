from django_github_oauth.views import GithubOAuthLoginView, GithubOAuthCallbackView
from django.urls import path
from . import views
urlpatterns = [
    path('login', GithubOAuthLoginView.as_view()),
    path('callback', GithubOAuthCallbackView.as_view()),
    path('',views.index,name="index"),
]