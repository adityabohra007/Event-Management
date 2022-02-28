from django.db import models
from django.contrib.auth.models import User
# Create your models here.
USER_TYPES = ((1,'admin'),(2,'user'))

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES)

    def __str__(self):
        return self.user.username 
    
