from django.contrib import admin
from churchApp.models import DevotionalVerse,VerseOfTheDay,Sermon
# Register your models here.
admin.site.register(VerseOfTheDay)
admin.site.register(DevotionalVerse)
admin.site.register(Sermon)
