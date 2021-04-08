from django.db import models
from datetime import datetime
import uuid


# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to="images/", blank=False)
    publish_date = models.DateTimeField(default=datetime.now())
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title
