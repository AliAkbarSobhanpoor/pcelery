from django.urls import path
from .views import mail_request_view

urlpatterns = [
    path("mailsender/", mail_request_view, name="mail_thank_you")
]
