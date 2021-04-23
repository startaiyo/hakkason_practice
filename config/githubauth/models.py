from django.db import models
from django_github_oauth.models import AbstractBaseUser

class User(AbstractBaseUser):
    avatar_url=models.CharField(max_length=300)