from account.models import CustomUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class Notification(models.Model):
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='notifications'
    )
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=2500)
    created = models.DateTimeField(default=timezone.now, editable=False)
    unread = models.BooleanField(default=True)

    # "sender" - generic relation to any model.
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()
