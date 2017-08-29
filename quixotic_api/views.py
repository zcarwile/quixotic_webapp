from rest_framework import viewsets
from quixotic_api.models import Event, Timeblock, Project, User
from quixotic_api.serializers import EventSerializer, TimeblockSerializer, ProjectSerializer, UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TimeblockViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Timeblock.objects.all()
    serializer_class = TimeblockSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer
