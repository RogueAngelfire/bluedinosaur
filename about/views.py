from django.shortcuts import render, HttpResponse

# Create your views here.

def about(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')
    # return HttpResponse('this view is working')
