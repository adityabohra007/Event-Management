from genericpath import exists
from os import stat
from random import randint, random
from urllib import request
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from event.models import EventRegistration, Events, Payment
from .permissions import AdminPermission, UserPermission
from rest_framework.response import Response
from event.serializers import EventSerializer, UserEventRegistratedSerializer, UserEventRegistrationSerializer, UserEventSerializer, UserMyBookingsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
class AdminAddEvent(APIView):
    permission_classes =[IsAuthenticated,AdminPermission]
    def get(self,request):
        return Response({'status':'he is admin'})
        

class AdminBookingStatus(APIView):
    permission_classes = [IsAuthenticated,AdminPermission]
    def get(self,*args, **kwargs):
        print(kwargs.get('pk'))
        event = Events.objects.filter(id=kwargs.get('pk'),created_by=self.request.user.userprofile)
        if event.exists():
            registered = EventRegistration.objects.filter(event = event.get()).exclude(payment = None )
            ser = UserEventRegistratedSerializer(registered,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AdminEventList(ListCreateAPIView):
    permission_classes =[IsAuthenticated,AdminPermission]
    queryset = Events.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save()
        
class AdminEventDetail(RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    permission_classes =[IsAuthenticated,AdminPermission]

    queryset = Events.objects.all()
    serializer_class= EventSerializer




class UserEventList(ListAPIView):
    permission_classes = [IsAuthenticated,UserPermission]
    serializer_class = UserEventSerializer

    def get_queryset(self):
        params = self.request.query_params.get('filter')
        if params == 'upcoming':
            return  Events.event.upcoming()
        elif params == 'completed':
            return Events.event.completed()
        else:
            return Events.objects.all()

class UserEventDetail(RetrieveAPIView):
    permission_classes =[IsAuthenticated,UserPermission]
    queryset = Events.objects.all()
    serializer_class= UserEventSerializer


class UserEventRegistration(APIView):
    permission_classes = [IsAuthenticated,UserPermission]
    serializer_class = UserEventRegistrationSerializer

    def post(self,*args, **kwargs):
        print('---------------------------------',self.request.data)
        
        event_id = self.request.data.get('event')
        if event_id == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        event = Events.objects.filter(id = event_id)
        if event.exists():
            event = event.get()
            event_registered = EventRegistration.objects.filter(event=event,user= self.request.user.userprofile).exclude(payment=None)
            if event_registered.exists():
                return Response({'non_field_error':'Already Registered for this event'},status=status.HTTP_400_BAD_REQUEST)
            eventReg = EventRegistration.objects.filter(event = event).exclude(payment = None )
            if event.max_capacity <= eventReg.count():
                return Response({'non_field_error':'Max capacity reached'},status=status.HTTP_400_BAD_REQUEST)
            
            ser = UserEventRegistrationSerializer(data={'event':event.id,'user': self.request.user.userprofile.id})
            if ser.is_valid():
                if event.scheduled_on <= timezone.now():
                    return Response({'non_field_error':'Cannot register after event started'},status=status.HTTP_400_BAD_REQUEST)
                if event.booking_start >= timezone.now():
                    return Response({"non_field_error":'Cannot register since window is not open yet '},status=status.HTTP_400_BAD_REQUEST)
                if event.booking_end <= timezone.now():
                    return Response({"non_field_error":'Cannot register since booking ended'},status=status.HTTP_400_BAD_REQUEST)
                
                saved =ser.save()
                payment = Payment.objects.create(payment_id=randint(1,100),
                                             transaction_compeleted_on= timezone.now())
                saved.payment = payment
                saved.save()
                
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status =status.HTTP_400_BAD_REQUEST)
            


class UserTypeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,*args, **kwargs):
        if self.request.user.userprofile.user_type == 1:
            return Response({'role':'admin'})
        else:
            return Response({'role':'user'})
        
        
class UserMyBooking(APIView):
    permission_classes = [IsAuthenticated,UserPermission]
    
    def get(self,request,*args, **kwargs):
        events = EventRegistration.objects.filter(user= request.user.userprofile).exclude(payment=None)
        if events.exists():
            ser = UserMyBookingsSerializer(events,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        
        else:
            return Response([],status=status.HTTP_200_OK)