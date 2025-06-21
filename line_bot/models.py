from django.db import models

class LineBindingStatus(models.Model):
    line_id = models.CharField(max_length=64, unique=True)
    step = models.CharField(max_length=32, default='none')  
    temp_username = models.CharField(max_length=150, blank=True, null=True)
