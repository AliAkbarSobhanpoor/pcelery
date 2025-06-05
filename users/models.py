from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """
    custom user . each website may have its functionality and field required for this part so we do this
    """
    must_change_password = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        # Only schedule task for new users or when must_change_password is True
        if is_new or self.must_change_password:
            from .tasks import change_user_password
            change_user_password.apply_async(args=[self.id], countdown=120)


class MailRequest(models.Model):
    email = models.EmailField("email", help_text="pls enter your email")
    message = models.TextField("message", help_text="enter your name.")

    def __str__(self) -> str:
        return self.email