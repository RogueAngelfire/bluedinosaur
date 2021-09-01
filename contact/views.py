from django.shortcuts import render, HttpResponse

# Create your views here.

def contact(request):
    """ A view to return the contact page """

    return render(request, 'contact/contact.html')
    #return HttpResponse('this view is working')
