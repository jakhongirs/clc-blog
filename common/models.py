from django.db import models
from helpers.models import BaseModel
# Create your models here.


class FAQ(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()
