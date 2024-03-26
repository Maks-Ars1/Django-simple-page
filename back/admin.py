from django.contrib import admin
from .models import MyUser, Task


# Register your models here.
admin.site.register(MyUser)
admin.site.register(Task)

