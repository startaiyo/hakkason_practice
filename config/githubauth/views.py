from django.shortcuts import render

# Create your views here.
from django_github_oauth.views import GithubOAuthCallbackView
from django_github_oauth.models import User
def index(request):
    return render(request,"top.html")

class GithubOAuthCallbackView(GithubOAuthCallbackView):
    def get(self,request, *args, **kwargs):
        headers = {'Authorization': 'token %s' % self.token}
        r = requests.get('https://api.github.com/user', headers=headers)
        data = r.json()
        defaults = dict(login=data['login'],token=self.token)
        user,created = User.objects.update_or_create(defaults,id=data['id'])
        