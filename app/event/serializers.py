from dataclasses import field
from rest_framework import serializers
from users.serializers import UserProfileSerializer
from event.models import EventRegistration, Events
from django.utils import timezone
from rest_framework.exceptions import ValidationError

class EventSerializer(serializers.ModelSerializer):
    # created_by = serializers. 
    class Meta:
        model = Events
        fields = "__all__"

    def create(self, validated_data):
        # print(self.context['request'].user.userprofile)
        return Events.objects.create(**validated_data,created_by =self.context['request'].user.userprofile )

    def validate(self, attrs):
        if attrs['scheduled_on'] == None:
            raise ValidationError('Scheduled date cannot be None')
        if attrs['booking_start'] == None:
            raise ValidationError('Booking start date cannot be None')
        if attrs['booking_end'] == None:
            raise ValidationError('Booking end date cannot be None')
        if attrs['max_capacity'] == 0:
            raise ValidationError('Cannot be zero capacity')
        if attrs['booking_start'] > attrs['booking_end']:
            raise ValidationError('Booking cannot start after the end date')
        if attrs['scheduled_on'] < attrs['booking_start'] or attrs['scheduled_on'] < attrs['booking_end']:
                raise ValidationError('Cannot be scheduled before booking end ')

        return attrs
    def save(self,*args, **kwargs):
        return super().save(*args, **kwargs)

class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"

class UserEventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = "__all__"


    def create(self,validated_data):
        
        instance = EventRegistration.objects.create(**validated_data)
        return instance
    
    
   

   
class UserEventRegistratedSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = EventRegistration
        fields = ['user','registered_on']

    
   
   
class UserMyBookingsSerializer(serializers.ModelSerializer):  
    event = EventSerializer()
    class Meta:
        model = EventRegistration
        fields  = "__all__"