from rest_framework import viewsets
from quixotic_api.models import Event, Timeblock, Project, User
from quixotic_api.serializers import EventSerializer, TimeblockSerializer, ProjectSerializer, UserSerializer

from django.utils import timezone
import datetime

class EventViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Event objects """
    base_name = "events"
    serializer_class = EventSerializer
    def get_queryset(self):

        t = self.request.query_params.get('tags', None)
        s = self.request.query_params.get('selected_date', None)
        print(self.request.query_params)

        # must supply a date
        if s is None:
	    return Event.objects.filter(tags="Impossible")

        s_dt = datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
        s_dt_plus_1 = s_dt + datetime.timedelta(days=1)
        if t is not None:
            queryset = Event.objects.filter(tags__exact=t, start__gt=s_dt, start__lt=s_dt_plus_1)
        else:
            queryset = Event.objects.filter(start__gt=s_dt, start__lt=s_dt_plus_1)
        return queryset

class TimeblockViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Timeblock objects """
    queryset = Timeblock.objects.all()
    serializer_class = TimeblockSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Project objects """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing User objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer

