from unicodedata import name
from django.urls import include, path
from .apiviews import AdminAddEvent, AdminBookingStatus, AdminEventDetail, AdminEventList,UserEventList,UserEventDetail, UserEventRegistration, UserMyBooking, UserTypeAPIView

urlpatterns = [
        path('dj-rest-auth/', include('dj_rest_auth.urls')),
        # path('djangorestframeworkdjangorestframework')
        path('isadmin/',AdminAddEvent.as_view(),name='isadmin'),
        path('events/<int:pk>/bookings',AdminBookingStatus.as_view(),name='event_booking' ),
        path('events/',AdminEventList.as_view(),name='event'),
        path('events/<int:pk>/',AdminEventDetail.as_view(),name='event_details'),

        path('user/events/',UserEventList.as_view(),name="user_event"),
        path('user/events/<int:pk>',UserEventDetail.as_view(),name="user_event_details"),
        path('user/event/registration',UserEventRegistration.as_view(),name="user_event_registration"),
        path('user/role',UserTypeAPIView.as_view(),name="user_role"),
        path("mybookings",UserMyBooking.as_view(),name ="user_booking")
        
]
