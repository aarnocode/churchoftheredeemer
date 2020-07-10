from django.shortcuts import render
from churchApp.models import DevotionalVerse,VerseOfTheDay
#import ntplib
from datetime import date
import random
from time import ctime
# Create your views here.
def index(request):
    #c=ntplib.NTPClient()
    #response=c.request('asia.pool.ntp.org',version=3)
    #currDate=ctime(response.tx_time)[4:10]
    today=date.today()
    currDate=today.strftime("%b %d")
    currVerse=VerseOfTheDay.objects.first()
    #print('DEBUG: Passed get VOTD')
    if currVerse.date != currDate:
        #print('DEBUG: Entered Condition')
        VerseOfTheDay.objects.all().delete()
        #print('DEBUG: Deleted VOTD')
        count=DevotionalVerse.objects.all().count()
        #print('DEBUG: Get count of all DevVer '+str(count))
        verse=DevotionalVerse.objects.get(pk=random.randrange(1,count+1))
        print(verse.content)
        #print('DEBUG: Get random verse from pool')
        insert=VerseOfTheDay.objects.get_or_create(verse=verse.content,BCV=verse.BCV,date=currDate)
        #print('DEBUG: Inserted chosen verse')
    currVerse=VerseOfTheDay.objects.first()
    index_dict={
    'verseoftheday':currVerse.verse,
    'BCV':currVerse.BCV
    }
    return render(request,'churchApp/index.html',context=index_dict)


def about(request):
    about='<strong>Something about the church here</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    mission='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
    vision='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
    about_dict={'about':about,'mission':mission,'vision':vision}
    return render(request,'churchApp/about.html',context=about_dict)
