from django import forms
from .models import ContactMessages
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactMessagesForm(forms.ModelForm):

    class Meta:
        model = ContactMessages
        fields = ['name', 'email', 'projectsummary']
        captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
