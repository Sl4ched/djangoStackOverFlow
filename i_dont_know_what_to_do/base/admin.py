from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Discuss, Answer, Tag, MyUser


class EmployeeInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = "myuser"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Discuss)
admin.site.register(Answer)
admin.site.register(Tag)
