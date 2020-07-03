from django.shortcuts import render,reverse,HttpResponseRedirect
from twitterUser.models import TwitterUser
from authentication.forms import signupForm,signinForm
from django.contrib.auth import logout, login, authenticate


# Create your views here.
def index(request):
    return render(request,'index.html')

def loginuser(request):
    if request.method == "POST":
        form = signinForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
    form = signinForm()
    return render(request,'index.html',{'Form':form})

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def signupuser(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
    form = signupForm()
    return render(request, 'index.html', {'Form': form})