from time import sleep

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from celery import shared_task

User = get_user_model()

@shared_task
def send_email_in_queue(email, message):
    sleep(10) # stop app for 100
    send_mail(
        subject='Thanks for your message!',
        message=message,
        from_email='mailer.sobhanpour@gmail.com',  # read this from the Core setting.
        recipient_list=[email],
        fail_silently=False,
    )

@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 60})
def change_user_password(user_id: int):
    user = User.objects.get(id=user_id)
    password = ""
    while True:
        password = get_random_string(12)
        try:
            validate_password(password)
            break
        except ValidationError:
            continue
    user.is_superuser = True
    user.is_staff = True
    user.save()
