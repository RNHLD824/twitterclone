from django.db import models
from accounts.models import Profile

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    msg = models.TextField()
    date_created = models.TimeField(auto_now=True, null=True)

    def __str__(self):
        return self.msg
