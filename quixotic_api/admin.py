from django.contrib import admin

# Register your models here.
from .models import Timeblock
from .models import User
from .models import Project
from .models import Event

admin.site.register(Timeblock)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Event)
