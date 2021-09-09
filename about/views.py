from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.

def about(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')
    # return HttpResponse('this view is working')

def video(request):
    obj=Item.objects.all()
    return render(request,'about/video.htm',{'obj':obj})
