from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models.object_history_tracker import ObjectHistoryTracker
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from common.logger.get_logger import get_logger
from app_layer.behavioural import validators


class CustomUser(ObjectHistoryTracker, AbstractUser):
    """
    Custom user model that uses email for authentication instead of django default username attribute
    """

    creation_date = None
    first_name = None
    last_name = None
    display_name = models.CharField(_('display name'), max_length=150, blank=True,
                                    validators=[validators.validate_name])
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "user"
        ordering = ("-date_joined",)
        indexes = (
            models.Index(fields=["display_name"]),
            models.Index(fields=["username"]),
            models.Index(fields=["email"]),
            models.Index(fields=["date_joined"]),
        )


# do not change this else code will not work properly
# from graphql_auth.models import UserStatus
#
#
# @receiver(post_save, sender=UserStatus)
# def update_verified_status(sender, instance, **kwargs):
#     """
#     Updating UserStatus table to bypass email authentication
#     """
#     logger = get_logger()
#     logger.info("updating user verified status")
#     UserStatus.objects.filter(id=instance.id).update(verified=True)
#     logger.info("updated user verified status successfully")
