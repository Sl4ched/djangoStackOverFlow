from django.contrib import admin

from .models import Discuss, Answer, Tag

admin.site.register(Discuss)
admin.site.register(Answer)
admin.site.register(Tag)

