from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    """
    custom user . each website may have its functionality and field required for this part so we do this
    """
    must_change_password = models.BooleanField(default=False)

class MailRequest(models.Model):
    email = models.EmailField("email", help_text="pls enter your email")
    message = models.TextField("message", help_text="enter your name.")

    def __str__(self) -> str:
        return self.email