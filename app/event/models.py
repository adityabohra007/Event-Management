from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils import timezone
from users.models import UserProfile
from .queryset import EventQueryset


class Events(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField()
    max_capacity = models.PositiveIntegerField()
    created_by = models.ForeignKey(UserProfile,default=1,on_delete=models.PROTECT)
    booking_start = models.DateTimeField()
    booking_end = models.DateTimeField()
    scheduled_on = models.DateTimeField(null=False,blank=False)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    event = EventQueryset.as_manager()

    def __str__(self):
        return self.name
    
    def clean(self):
        
        if self.scheduled_on == None:
            raise ValidationError('Scheduled date cannot be None')
        if self.booking_start == None:
            raise ValidationError('Booking start date cannot be None')
        if self.booking_end == None:
            raise ValidationError('Booking end date cannot be None')
        if self.max_capacity == 0:
            raise ValidationError('Cannot be zero capacity')
        if self.booking_start > self.booking_end:
           raise ValidationError('Booking cannot start after the end date')

        if self.scheduled_on < self.booking_start or self.scheduled_on < self.booking_end:
                raise ValidationError('Can be scheduled before booking end ')
    
    def validate(self):
        print('validate')
        pass
        
    def save(self,*args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
class Payment(models.Model):
    payment_id = models.CharField(max_length=100,null=False,default='None',blank=False)
    transaction_compeleted_on = models.DateTimeField()
    
class EventRegistration(models.Model):
    event = models.ForeignKey(Events,on_delete=models.PROTECT)
    user = models.ForeignKey(UserProfile,on_delete=models.PROTECT)
    registered_on = models.DateTimeField(auto_now_add=True)
    payment = models.OneToOneField(Payment,null=True,on_delete=models.SET_NULL,blank=True)

    def clean(self):
        if self.event.scheduled_on <= timezone.now():
            raise ValidationError('Cannot register after event started')
        
        if self.event.booking_start >= timezone.now():
            raise ValidationError('Cannot register since window is not open yet ')

        if self.event.booking_end <= timezone.now():
            raise ValidationError('Cannot register since booking ended')

    def save(self,*args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)
    def __str__(self):
        return  f"User {self.user.user.username}  Event= {self.event.name}"

