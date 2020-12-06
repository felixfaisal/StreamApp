from django.shortcuts import render
from .models import VideoInfo

# Create your views here.


def Home(request):
    context = {}
    return render(request, "index.html", context)


def Video(request, id):
    VideoObj = VideoInfo.objects.filter(Video_id=int(id))
    List = [x for x in VideoObj]
    print(List[0].Video_id)
    context = {"Name": List[0].Video_Name,
               "Link": List[0].Video_Link,
               "Description": List[0].Video_Description}
    return render(request, "Video.html", context)


def ListAllVideos(request):
    List = VideoInfo.objects.all()
    context = {"List": List}
    return render(request, "VideoList.html", context)
