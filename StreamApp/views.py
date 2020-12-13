from django.shortcuts import render, redirect
from .models import VideoInfo
# Create your views here.
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="LoginPage")
def Home(request):
    context = {}
    return render(request, "index.html", context)


def Register(request):
    form = CreateUserForm()
    context = {"form": form}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('LoginPage')

    return render(request, "register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('LoginPage')
#


def loginPage(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, "login.html", context)


@login_required(login_url="LoginPage")
def Video(request, id):
    VideoObj = VideoInfo.objects.filter(Video_id=int(id))
    List = [x for x in VideoObj]
    print(List[0].Video_id)
    context = {"Name": List[0].Video_Name,
               "Link": List[0].Video_Link,
               "Description": List[0].Video_Description}
    return render(request, "Video.html", context)


@login_required(login_url="LoginPage")
def ListAllVideos(request):
    List = VideoInfo.objects.all()
    context = {"List": List}
    return render(request, "VideoList.html", context)
