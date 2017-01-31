from django.db import models
from django.utils import timezone
import datetime
# from django.core.validators import MaxValueValidator, MinValueValidator

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    detail = models.CharField(max_length=500)
    features = models.CharField(max_length=500)
    redaction = models.CharField(max_length=500)
    relevant = models.BooleanField(default=True)

    def __unicode__(self):
        tmp = datetime.datetime.strftime(self.start,"%Y-%m-%d %H:%M:%S")
        return "%s\t%s" % (tmp, self.title)


class Timeblock(models.Model):
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=500, default="Enter activity...")
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=500)
    verified = models.BooleanField(default=False)
    billable = models.BooleanField(default=False)

    def __unicode__(self):
        tmp1 = datetime.datetime.strftime(self.start,"%Y-%m-%d %H:%M:%S")
        tmp2 = datetime.datetime.strftime(self.end,"%Y-%m-%d %H:%M:%S")
        return "%s\t%s\t%s" % (tmp1, tmp2, self.title)


