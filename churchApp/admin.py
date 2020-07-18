from django.contrib import admin
from django.contrib.admin import AdminSite
from churchApp.models import DevotionalVerse,VerseOfTheDay,Sermon,Announcement,Comment

# Register your models here.
admin.site.register(VerseOfTheDay)
admin.site.register(DevotionalVerse)
admin.site.register(Sermon)
admin.site.register(Announcement)
#This shit is new. lets try using admin.site.register
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','body','sermon','created_on','active')
    list_filter=('active','created_on')
    search_fields=('name','email','body')
    actions=['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)



admin.site.site_header='Church of the Redeemer'
