from django.db import models


class ObjectHistoryTracker(models.Model):
    """
        Model for Tracking object's creating and updating information
    """
    creation_date = models.DateTimeField(verbose_name="creation date", editable=False, auto_now_add=True)
    last_modified_date = models.DateTimeField(verbose_name="last modified date", editable=False, auto_now_add=True)

    class Meta:
        abstract = True
