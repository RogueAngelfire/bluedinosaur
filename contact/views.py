from django.shortcuts import render, HttpResponse
from .models import ContactMessages
from .forms import ContactMessagesForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def _send_confirmation_email(form, cust_email):
    """
        Send the user a confirmation email
    """
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
        [cust_email]
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
            cust_email = messages_form.email
            _send_confirmation_email(messages_form, cust_email)
    return render(request, 'contact/contact.html')
    #return HttpResponse('this view is working')
