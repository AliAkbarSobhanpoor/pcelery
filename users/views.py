# core python

# core django
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# installed python

# installed django
from celery import shared_task

# created by me
from .forms import MailRequestForm
from .tasks import send_email_in_queue

def mail_request_view(request: HttpRequest) -> HttpResponse:
    form = MailRequestForm()
    if request.method == 'POST':
        form = MailRequestForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # Send email to the user
            confirm_message = "'We received your message and will get back to you soon.'"
            send_email_in_queue.delay(instance.email, message=confirm_message)
            return redirect('mail_thank_you')
        
    return render(request, 'users/mail_form.html', {'form': form})
