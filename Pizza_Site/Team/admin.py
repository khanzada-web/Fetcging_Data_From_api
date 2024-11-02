from django.contrib import admin
from .models import Team_Member

class Team_Add_Admin(admin.ModelAdmin):
    list_display=['Profile_Image','Name','Role']

admin.site.register(Team_Member,Team_Add_Admin)
