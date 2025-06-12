from django.db import models
from user.models import User
class Events(models.Model):
    title = models.CharField(max_length = 20 , null = False , blank = False)
    date = models.DateField()
    content = models.TextField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    