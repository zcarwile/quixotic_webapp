from rest_framework import serializers
from quixotic_api.models import Event, Timeblock, Project, User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("start", "end", "title","user")

class TimeblockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeblock
        fields = ("start","end","title","user","project")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = tuple(["name"])

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name","email")
