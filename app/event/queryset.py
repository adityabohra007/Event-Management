from django.db.models.query import QuerySet
# from django.db.utils import Q
from django.utils import timezone
class EventQueryset(QuerySet):
    def completed(self):
        return self.filter(scheduled_on__lt = timezone.now())
    def upcoming(self):
        return self.filter(scheduled_on__gt = timezone.now())
    