from django.contrib import admin
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user','img','id')

admin.site.register(Profile, ProfileAdmin)


