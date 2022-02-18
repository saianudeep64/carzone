from django.contrib import admin
from .models import Team


class Teamadmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name',"created_at")

admin.site.register(Team,Teamadmin)
