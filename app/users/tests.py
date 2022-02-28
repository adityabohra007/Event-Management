from django.test import TestCase
from django.contrib.auth.models import User

from .models import USER_TYPES, UserProfile


# Create yor tests here.

class UserTestCase(TestCase):
    def test_user(self):
        username = 'shetu'
        password = 'hello'
        u = User(username=username)
        u.set_password(password)
        u.save()
        self.assertEqual(u.username, username)
        self.assertTrue(u.check_password(password))
    
    def test_userprofile_admin(self):
        username = 'testname'
        password = 'password'
        u = User(username=username)
        u.set_password(password)
        u.save()

        user_profile = UserProfile()
        user_profile.user = u
        user_profile.user_type=0
        user_profile.save()
        
        self.assertEqual(user_profile.user,u)
        self.assertEqual(user_profile.user_type,0)

    
    def test_userprofile_user(self):
        username = 'testname'
        password = 'password'
        u = User(username=username)
        u.set_password(password)
        u.save()

        user_profile = UserProfile()
        user_profile.user = u
        user_profile.user_type=1
        user_profile.save()
        
        self.assertEqual(user_profile.user,u)
        self.assertEqual(user_profile.user_type,1)



