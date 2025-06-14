from django.db import models
from user.models import User

class Events(models.Model):
    title = models.CharField(max_length = 20 , null = False , blank = False)
    date = models.DateField()
    content = models.TextField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)  # 如果你需要收集電話
    note = models.TextField(blank=True, null=True)       # 備註
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.event, self.note)
