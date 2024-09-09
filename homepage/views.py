from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm2


def index(request):
    form = ContactForm2(request.POST)
    if form.is_valid():
        print("form is valid")
        name = form.cleaned_data.get("name")
        company = form.cleaned_data.get("company")
        object = form.cleaned_data.get("object")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        full_message = f"""
        Received message below from Name: {name}, 
        email: {email}, 
        company: {company},
        Object: {object}
        ________________________


        {message}
        """
        print("message receieved")
        print(full_message)
        send_mail(subject="Received contact from portfolio",message=full_message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=[settings.NOTIFY_EMAIL])
        return render(request, 'homepage/about/thankyou.html')
    else:
        form = ContactForm2()
    return render(request, 'homepage/index.html', {'form': form})


