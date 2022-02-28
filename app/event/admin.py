from django.contrib import admin

from event.models import EventRegistration, Events

# Register your models here.

admin.site.register(Events)
admin.site.register(EventRegistration)