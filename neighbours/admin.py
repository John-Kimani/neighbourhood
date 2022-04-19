from django.contrib import admin
from .models import Neighborhood,Business,Post,Hood


admin.site.register(Neighborhood)
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(Post)