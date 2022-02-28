from dataclasses import dataclass
from datetime import date, datetime, timedelta
from time import time
from django.forms import ValidationError
from django.test import TestCase
from ..models import EventRegistration, Events, Payment
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import UserProfile
# Create your tests here.
class TestEventModel(TestCase):


        
    def test_created(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 100
        instance.created_by =self.up
        instance.scheduled_on = timezone.now() + timedelta(days=20)
        instance.booking_start = timezone.now()
        instance.booking_end = timezone.now()+ timedelta(days=10)
        instance.full_clean()
        instance.save()

        
    def test_schedule_date_is_none_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 100
        instance.created_by =self.up
        instance.scheduled_on = None
        instance.booking_start = timezone.now()
        instance.booking_end = timezone.now()+ timedelta(days=10)
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()

    def test_schedule_date_is_less_than_booking_windows_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 100
        instance.created_by =self.up
        instance.scheduled_on = timezone.now() - timedelta(days=5)
        instance.booking_start = timezone.now()
        instance.booking_end = timezone.now()+ timedelta(days=10)
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()


    def test_start_is_after_end_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 100
        instance.created_by =self.up
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.booking_start = timezone.now()+ timedelta(days=10) 
        instance.booking_end =timezone.now()
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()

    def test_capacity_zero_is_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 0
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.created_by =self.up
        instance.booking_start = timezone.now()  
        instance.booking_end =timezone.now()+ timedelta(days=10)
        with self.assertRaises(ValidationError):
                instance.full_clean()
                instance.save()

    def test_name_is_blank_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = ''
        instance.description = 'Test Description'
        instance.max_capacity = 0
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.created_by =self.up
        instance.booking_start = timezone.now()  
        instance.booking_end =timezone.now()+ timedelta(days=10)
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()
        
    def test_description_is_blank_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'Test'
        instance.description = ''
        instance.max_capacity = 0
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.created_by =self.up
        instance.booking_start = timezone.now()  
        instance.booking_end =timezone.now()+ timedelta(days=10)
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()
        
    def test_created_by_is_null_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'Test'
        instance.description = 'Test Discription'
        instance.max_capacity = 100
        instance.created_by =None
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.booking_start = timezone.now()  
        instance.booking_end =timezone.now()+ timedelta(days=10)
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()

    def test_booking_start_is_null_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()

        instance = Events()
        instance.name = 'Test'
        instance.description = 'Test Discription'
        instance.max_capacity = 100
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.created_by =self.up
        instance.booking_start = None 
        instance.booking_end =timezone.now()+ timedelta(days=10)
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()

    def test_booking_end_is_null_invalid(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'Test'
        instance.description = 'Test Discription'
        instance.max_capacity = 100
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.created_by =self.up
        instance.booking_start = timezone.now() 
        instance.booking_end =None
        with self.assertRaises(ValidationError):
            instance.full_clean()
            instance.save()
    
    def test_str(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 100
        instance.scheduled_on = timezone.now() + timedelta(days=20)

        instance.created_by =self.up
        instance.booking_start = timezone.now()
        instance.booking_end = timezone.now()+ timedelta(days=10)
        instance.full_clean()
        instance.save()

        self.assertEquals(str(instance),'TestName')


# Test EventRegistration 
class TestEventRegistration(TestCase):


    def test_created(self):
        self.user = User()
        self.user.username = 'user'
        self.user.set_password('userpassword')
        self.user.save()
        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 100
        instance.scheduled_on = timezone.now() + timedelta(days=20)
        instance.created_by =self.up
        instance.booking_start = timezone.now()
        instance.booking_end = timezone.now()+ timedelta(days=10)
        instance.full_clean()
        instance.save()
        registration = EventRegistration()
        registration.user = self.up
        registration.event = instance
        payment = Payment()
        payment.payment_id = 'testid'
        payment.transaction_compeleted_on = timezone.now()
        payment.save()
        registration.payment = payment
        registration.save()


    def test_str(self):
        self.user = User()
        self.user.username = 'test'
        self.user.set_password('testpassword')
        self.user.save()

        self.up = UserProfile()
        self.up.user = self.user
        self.up.user_type = 2
        self.up.save()
        instance = Events()
        instance.name = 'TestName'
        instance.description = 'Test Description'
        instance.max_capacity = 100
        instance.scheduled_on = timezone.now() + timedelta(days=20)
        instance.created_by =self.up
        instance.booking_start = timezone.now()
        instance.booking_end = timezone.now()+ timedelta(days=10)
        instance.full_clean()
        instance.save()
        registration = EventRegistration()
        registration.user = self.up
        registration.event = instance
        payment = Payment()
        payment.payment_id = 'testid'
        payment.transaction_compeleted_on = timezone.now()
        payment.save()
        registration.payment = payment
        registration.save()
        # self.assertEquals(str(registration),f"User {registration.user.user.username}  Event= {registration.event.name}")

        




class TestPayment(TestCase):
    def test_payment_succesful(self):
        instance = Payment(payment_id ='testid',transaction_compeleted_on=timezone.now())
        instance.save()
        fetch_instance = Payment.objects.get(id = instance.id)
        self.assertEquals(instance.payment_id,fetch_instance.payment_id)