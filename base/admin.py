from django.contrib import admin

# Register your models here.

from .models import Problem,Topic,Solution,Message

admin.site.register(Problem)
admin.site.register(Topic)
admin.site.register(Solution)
admin.site.register(Message)
