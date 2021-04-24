from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.conf import settings

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, github_url, password=None, **extra_fields):

        if not github_url:
            raise ValueError('Users must have an github url')
 
        user = self.model(github_url=github_url, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, github_url, password=None):
        
        user = self.create_user(
            email=email,
            github_url=github_url,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 
 
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=255,
        unique=True,
    )
    github_url = models.URLField(unique=True)
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'github_url'
    REQUIRED_FIELDS = ['email']
 
    def __str__(self):
        return self.github_url

 
class Request(models.Model):
    applicant = models.ForeignKey(User,related_name='applicant',on_delete=models.CASCADE)
    recruiter = models.ForeignKey(User,related_name='recruiter',on_delete=models.CASCADE)
    is_proceeded = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Recruitment(models.Model):
    created_user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    detail = models.TextField()
    approval_msg = models.CharField(max_length=200)
    refusal_msg = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    sender = models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE)
    accepter = models.ForeignKey(User,related_name='accepter',on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    recruitment = models.ForeignKey(Recruitment,on_delete=models.CASCADE)


# Create your models here.
