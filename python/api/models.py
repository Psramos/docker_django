import uuid
from django.db import models


class Dummy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
