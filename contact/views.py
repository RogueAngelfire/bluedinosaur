from django.shortcuts import render, HttpResponse
from .models import ContactMessages
from .forms import ContactMessagesForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def _send_confirmation_email(form):
    """
        Send the user a confirmation email
    """
    print('I am printing form data on line number 14 below')
    print(form)
    subject = render_to_string(
        'contact/emails/email_subject.txt',
        {'form': form}
        )
    body = render_to_string(
        'contact/emails/email_body.txt',
        {
            'form': form,
            'contact_email': settings.DEFAULT_FROM_EMAIL
        }
        )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [form.email]
    )

# Email to be sent to Blue Dinosaur Animation

def _send_bdinosaur_email(form):
    """
        Send the user a confirmation email
    """
    print('I am printing form data on line number 40 below')
    print(form)
    print(_send_bdinosaur_email)
    subject = render_to_string(
        'contact/emails/email_subject.txt',
        {'form': form}
        )
    body = render_to_string(
        'contact/emails/email_bdbody.txt',
        {
            'form': form,
        }
        )

    send_mail(
        subject,
        body,
        form.name,
        #settings.DEFAULT_FROM_EMAIL,
        ['bluedinosauranimation@gmail.com']
    )

def contact(request):
    """ A view to return the contact page """
    
    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'projectsummary': request.POST['projectsummary'],
        }
        form = ContactMessagesForm(request.POST)
        if form.is_valid():
            messages_form = form.save()
            #cust_email = messages_form.email
            _send_confirmation_email(messages_form)
            _send_bdinosaur_email(messages_form)
    return render(request, 'contact/contact.html')
    #return HttpResponse('this view is working')
