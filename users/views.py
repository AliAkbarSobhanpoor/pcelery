from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from .forms import MailRequestForm
# from .models import MailRequest

def mail_request_view(request: HttpRequest) -> HttpResponse:
    form = MailRequestForm()
    
    if request.method == 'POST':
        form = MailRequestForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # Send email to the user
            send_mail(
                subject='Thanks for your message!',
                message='We received your message and will get back to you soon.',
                from_email='mailer.sobhanpour@gmail.com', #read this from the Core setting.
                recipient_list=[instance.email],
                fail_silently=False,
            )
            return redirect('mail_thank_you')
        
    return render(request, 'users/mail_form.html', {'form': form})
