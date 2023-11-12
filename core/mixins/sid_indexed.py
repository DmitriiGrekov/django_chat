import uuid

from django.db import models
from django.utils.text import slugify


class SidIndexedMixin(models.Model):

    class Meta:
        abstract = True

    sid = models.UUIDField('sid', primary_key=True, default=uuid.uuid4, editable=False)

