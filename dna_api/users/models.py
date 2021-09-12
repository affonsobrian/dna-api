import uuid  # pragma: no cover

from django.conf import settings  # pragma: no cover
from django.contrib.auth.models import AbstractUser  # pragma: no cover
from django.db import models  # pragma: no cover
from django.db.models.signals import post_save  # pragma: no cover
from django.dispatch import receiver  # pragma: no cover
from rest_framework.authtoken.models import Token  # pragma: no cover


class User(AbstractUser):  # pragma: no cover
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # pragma: no cover

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # pragma: no cover
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
