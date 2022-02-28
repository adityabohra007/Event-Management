from cmath import log
from datetime import date, datetime, timedelta
from http import client
from time import time
from urllib.parse import urlencode
from django.forms import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from event.models import Events
from users.models import USER_TYPES, UserProfile
from rest_framework.test import APIClient
from django.utils import timezone
class UserAPITests(APITestCase):
    login_url = '/api/dj-rest-auth/login/'
    def setUp(self):

        self.client = APIClient()
        self.admin = {'username':'admin','password':'adminpassword'}
        self.user = {'username':'user','password':'userpassword'}
        def make_user(data,type):
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            self.up = UserProfile()
            self.up.user = user
            self.up.user_type = type
            self.up.save()
            return self.up
        
        self.admin_instance = make_user(self.admin,1)
        self.user_instance = make_user(self.user,2)
        self.authAdmin = self.client.post(UserAPITests.login_url,{'username':self.admin['username'],'password':self.admin['password']}) 
        self.authUser = self.client.post(UserAPITests.login_url,{'username':self.user['username'],'password':self.user['password']}) 
        
        
    def test_login_user(self):
        '''
            Test Normal user Login
        '''
        response = self.client.post(UserAPITests.login_url,self.user,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_api_userprofile_admin(self): 
        response = self.client.post(UserAPITests.login_url,self.admin) 
        user= User.objects.get(id=response.data['user']['pk'])
        self.assertEqual(self.admin_instance.user,user)
        self.assertEqual(self.admin_instance.user_type,user.userprofile.user_type)


    def test_api_userprofile_user(self):
        response = self.client.post(UserAPITests.login_url,self.admin) 
        user= User.objects.get(id=response.data['user']['pk'])
        self.assertEqual(self.admin_instance.user,user)
        self.assertEqual(self.admin_instance.user_type,user.userprofile.user_type)
       

class TestAdminEventList(APITestCase):
    login_url = '/api/dj-rest-auth/login/'
    def setUp(self):

        self.client = APIClient()
        self.admin = {'username':'admin','password':'adminpassword'}
        self.user = {'username':'user','password':'userpassword'}
        def make_user(data,type):
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            self.up = UserProfile()
            self.up.user = user
            self.up.user_type = type
            self.up.save()
            return self.up
        
        self.admin_instance = make_user(self.admin,1)
        self.user_instance = make_user(self.user,2)
        self.authAdmin = self.client.post(UserAPITests.login_url,{'username':self.admin['username'],'password':self.admin['password']}) 
        self.authUser = self.client.post(UserAPITests.login_url,{'username':self.user['username'],'password':self.user['password']}) 

        event = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                              booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))
        
        event.full_clean()
        event.save()

        event1 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                            booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))

        event1.full_clean()
        event1.save()

        event2 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                             booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10)
                            )
        event2.full_clean()
        event2.save()

    def test_get_list(self):
        ''' Test if admin can get list of event 
        Permission IsAuthenticated and  IsAdminUser
        '''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authAdmin.data['access_token'])

        url = reverse('event')
        response = self.client.get(url)
        self.assertEqual(len(response.data),3)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_event_create(self):
        ''' Test if admin can create new event'''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authAdmin.data['access_token'])
        url = reverse('event')
        data ={ 'name' : 'TestEvent',
                'description':"TestDescription",
                'max_capacity':100,
                "scheduled_on" : timezone.now() + timedelta(days=12),
                'booking_start': timezone.now(),
                'booking_end' : timezone.now() + timedelta(days=10)}
        
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        saved_instance = response.data
        self.assertEqual(saved_instance['name'],data['name'])
        self.assertEqual(saved_instance['description'],data['description'])
        self.assertEqual(saved_instance['max_capacity'],data['max_capacity'])




class TestAdminEventDetail(APITestCase):
    login_url = '/api/dj-rest-auth/login/'
    def setUp(self):

        self.client = APIClient()
        self.admin = {'username':'admin','password':'adminpassword'}
        self.user = {'username':'user','password':'userpassword'}
        def make_user(data,type):
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            self.up = UserProfile()
            self.up.user = user
            self.up.user_type = type
            self.up.save()
            return self.up
        
        self.admin_instance = make_user(self.admin,1)
        self.user_instance = make_user(self.user,2)
        self.authAdmin = self.client.post(UserAPITests.login_url,{'username':self.admin['username'],'password':self.admin['password']}) 
        self.authUser = self.client.post(UserAPITests.login_url,{'username':self.user['username'],'password':self.user['password']}) 

        self.event = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                              booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))
        
        self.event.full_clean()
        self.event.save()

        self.event1 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                            booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))

        self.event1.full_clean()
        self.event1.save()

        self.event2 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                             booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10)
                            )
        self.event2.full_clean()
        self.event2.save()


    def test_get_event(self):  
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authAdmin.data['access_token'])
        url = reverse('event_details',kwargs={'pk':self.event.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)      


class TestUserEventList(APITestCase):
    login_url = '/api/dj-rest-auth/login/'
    def setUp(self):

        self.client = APIClient()
        self.admin = {'username':'admin','password':'adminpassword'}
        self.user = {'username':'user','password':'userpassword'}
        def make_user(data,type):
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            self.up = UserProfile()
            self.up.user = user
            self.up.user_type = type
            self.up.save()
            return self.up
        
        self.admin_instance = make_user(self.admin,1)
        self.user_instance = make_user(self.user,2)
        self.authAdmin = self.client.post(UserAPITests.login_url,{'username':self.admin['username'],'password':self.admin['password']}) 
        self.authUser = self.client.post(UserAPITests.login_url,{'username':self.user['username'],'password':self.user['password']}) 

        self.event = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                              booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))
        
        self.event.full_clean()
        self.event.save()

        self.event1 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                            booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))

        self.event1.full_clean()
        self.event1.save()

        self.event2 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                             booking_start = timezone.now() - timedelta(days=8),
                            scheduled_on = timezone.now() - timedelta(days=5),
                            booking_end = timezone.now() - timedelta(days=6)
                            )
        self.event2.full_clean()
        self.event2.save()




    def test_get_list_upcoming(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        url = reverse('user_event')+"?"+urlencode({'filter':'upcoming'})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)     
        self.assertEqual(len(response.data),2) 


    def test_get_list_compeleted(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        url = reverse('user_event')+"?"+urlencode({'filter':'completed'})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)     
        self.assertEqual(len(response.data),1) 

    def test_get_list_no_query(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        url = reverse('user_event')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)     
        self.assertEqual(len(response.data),3) 





class TestUserEventRegistration(APITestCase):
    login_url = '/api/dj-rest-auth/login/'
    def setUp(self):

        self.client = APIClient()
        self.admin = {'username':'admin','password':'adminpassword'}
        self.user = {'username':'user','password':'userpassword'}
        self.user1 = {'username':'user1','password':'userpassword'}

        def make_user(data,type):
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            self.up = UserProfile()
            self.up.user = user
            self.up.user_type = type
            self.up.save()
            return self.up
        
        self.admin_instance = make_user(self.admin,1)
        self.user_instance = make_user(self.user,2)
        self.user_instance1 = make_user(self.user1,2)

        
        self.authAdmin = self.client.post(UserAPITests.login_url,{'username':self.admin['username'],'password':self.admin['password']}) 
        self.authUser = self.client.post(UserAPITests.login_url,{'username':self.user['username'],'password':self.user['password']}) 
        self.authUser1 = self.client.post(UserAPITests.login_url,{'username':self.user1['username'],'password':self.user1['password']}) 
        self.event = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                              booking_start = timezone.now() - timedelta(days=10),
                            scheduled_on = timezone.now() - timedelta(days=2),
                            booking_end = timezone.now() - timedelta(days=3))
        
        self.event.full_clean()
        self.event.save()

        self.event1 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=1,
                            created_by = self.admin_instance,
                            booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))

        self.event1.full_clean()
        self.event1.save()

        self.event2 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                             booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10)
                            )
        self.event2.full_clean()
        self.event2.save()


    def test_registration_failed_schedule (self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        url = reverse('user_event_registration')
        # with self.assertRaises(ValidationError):
        response = self.client.post(url,{'event':self.event.id})
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)     
   
    def test_registration_successful(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        url = reverse('user_event_registration')
        response = self.client.post(url,{'event':self.event1.id})
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)  
        self.assertEqual(response.data,None)
    def test_registration_max_capacity_reached(self):
        self.client.credentials()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser1.data['access_token'])
        url = reverse('user_event_registration')
        response = self.client.post(url,{'event':self.event1.id})
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        url = reverse('user_event_registration')
        response = self.client.post(url,{'event':self.event1.id})
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
        
           
             

class TestUserEventDetail(APITestCase):
    login_url = '/api/dj-rest-auth/login/'
    def setUp(self):

        self.client = APIClient()
        self.admin = {'username':'admin','password':'adminpassword'}
        self.user = {'username':'user','password':'userpassword'}
        def make_user(data,type):
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            self.up = UserProfile()
            self.up.user = user
            self.up.user_type = type
            self.up.save()
            return self.up
        
        self.admin_instance = make_user(self.admin,1)
        self.user_instance = make_user(self.user,2)
        self.authAdmin = self.client.post(UserAPITests.login_url,{'username':self.admin['username'],'password':self.admin['password']}) 
        self.authUser = self.client.post(UserAPITests.login_url,{'username':self.user['username'],'password':self.user['password']}) 

        self.event = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                              booking_start = timezone.now() - timedelta(days=10),
                            scheduled_on = timezone.now() - timedelta(days=2),
                            booking_end = timezone.now() - timedelta(days=3))
        
        self.event.full_clean()
        self.event.save()

        self.event1 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                            booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10))

        self.event1.full_clean()
        self.event1.save()

        self.event2 = Events(name = 'TestEvent',
                            description="TestDescription",
                            max_capacity=100,
                            created_by = self.admin_instance,
                             booking_start = timezone.now(),
                            scheduled_on = timezone.now() + timedelta(days=12),
                            booking_end = timezone.now() + timedelta(days=10)
                            )
        self.event2.full_clean()
        self.event2.save()




    def test_get_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        url = reverse('user_event_details',kwargs={'pk':self.event.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)     




class TestUserTypeAPIView(APITestCase):
    login_url = '/api/dj-rest-auth/login/'
    def setUp(self):

        self.client = APIClient()
        self.admin = {'username':'admin','password':'adminpassword'}
        self.user = {'username':'user','password':'userpassword'}
        def make_user(data,type):
            user = User()
            user.username = data['username']
            user.set_password(data['password'])
            user.save()
            self.up = UserProfile()
            self.up.user = user
            self.up.user_type = type
            self.up.save()
            return self.up
        
        self.admin_instance = make_user(self.admin,1)
        self.user_instance = make_user(self.user,2)
        self.authAdmin = self.client.post(UserAPITests.login_url,{'username':self.admin['username'],'password':self.admin['password']}) 
        self.authUser = self.client.post(UserAPITests.login_url,{'username':self.user['username'],'password':self.user['password']}) 

    def test_get_role(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.authUser.data['access_token'])
        response_role = self.client.get(reverse('user_role'))
        self.assertEqual(response_role.status_code,status.HTTP_200_OK)
        self.assertEqual(response_role.data['role'],'user')
        
