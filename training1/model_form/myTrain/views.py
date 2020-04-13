from django.shortcuts import render
from myTrain.forms import UserInfoForm, UserWebsiteForm
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):

    return render(request, 'myTrain/index.html')

def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserInfoForm(data = request.POST)
        website_form = UserWebsiteForm(data = request.POST)

        if user_form.is_valid() and website_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            website = website_form.save(commit = False)
            website.user = user

            if 'portfolio' in request.POST:
                website.portfolio = request.POST["portfolio"]

            website.save()

            registered = True

    else:

        user_form = UserInfoForm()
        website_form = UserWebsiteForm()        

    return render(request, 'mytrain/register.html', context = {'user_form':user_form,'website':website_form, 'registered':registered})

def log_in(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:

            if user.is_active:

                login(request,user)
                print("user is active")
                return HttpResponseRedirect(reverse('index'))

            else:

                return HttpResponse("Something Went Wrong. Did you registered properly?")

        else:

            return HttpResponse("Invalid Credentials")
    
    else:

        return render(request, "myTrain/login.html", {})


@login_required
def log_out(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))


