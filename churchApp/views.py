from django.shortcuts import render
from churchApp.models import DevotionalVerse,VerseOfTheDay,Sermon,Announcement,Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
import django_user_agents
#import ntplib
from datetime import date
import random
import time,os,platform
# Create your views here.
DEBUG_MODE=False

def DEBUG(message):
    if DEBUG_MODE==True:
        print("DEBUG: "+message)

def index(request):
    os.environ["TZ"]="Asia/Manila"
    if platform.system() != 'Windows':
        time.tzset()
    today=date.today()
    currDate=today.strftime("%b %d")
    currVerse=VerseOfTheDay.objects.first()
    DEBUG(str(currVerse))
    DEBUG('Passed get VOTD')
    if currVerse.date != currDate:
        DEBUG('Entered Condition')
        VerseOfTheDay.objects.all().delete()
        DEBUG('Deleted VOTD')
        count=DevotionalVerse.objects.all().count()
        DEBUG('Get count of all DevVer '+str(count))
        verse=DevotionalVerse.objects.get(pk=random.randrange(1,count+1))
        print(verse.content)
        DEBUG('Get random verse from pool')
        insert=VerseOfTheDay.objects.get_or_create(verse=verse.content,BCV=verse.BCV,date=currDate)
        DEBUG('Inserted chosen verse')
    currVerse=VerseOfTheDay.objects.first()

    index_dict={
    'verseoftheday':currVerse.verse,
    'BCV':currVerse.BCV,
    'announcement':Announcement.objects.all()
    }

    countAnnouncement=Announcement.objects.all().count()
    if countAnnouncement == 0:
        DEBUG('Entered no announcement')
        index_dict['announcement']='No announcements'

    return render(request,'churchApp/index.html',context=index_dict)
    # if request.user_agent.is_mobile:
    #     return mobileSPA(request)
    # else:
    #     return SPA(request)

def pastora_corner(request,urlId=0):
    if urlId==0:
        sermonList=Sermon.objects.all().order_by('-date')
        latestSermon=sermonList.first()
        sermonDate=latestSermon.date
        sermonDate=sermonDate.strftime("%B %d %Y")
        sermonContent=latestSermon.serviceSermon
    pastora_corner_dict={
    'date':sermonDate,
    'sermon':sermonContent
    }
    return render(request,'churchApp/pastora\'sCorner.html',context=pastora_corner_dict)

def sermon_list(request):
    sermoncount=Sermon.objects.all().count()
    list_dict={
    'count':sermoncount,
    'sermonList':Sermon.objects.all().order_by('-date')
    }
    return render(request,'churchApp/sermonList.html',context=list_dict)

def sermon_list_prev(request,urlId):
    previousSermon=Sermon.objects.get(pk=int(urlId))
    sermonDate=previousSermon.date
    sermonDate=sermonDate.strftime("%B %d %Y")
    sermonContent=previousSermon.serviceSermon
    prev_sermon_dict={
    'date':sermonDate,
    'sermon':sermonContent
    }
    return render(request,'churchApp/sermonListPrev.html',context=prev_sermon_dict)

def about(request):
    about='<strong>Something about the church here</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    mission='To know God and proclaim God.'
    vision='To teach the great commandment to do the great comission.'
    about_dict={'about':about,'mission':mission,'vision':vision}
    return render(request,'churchApp/about.html',context=about_dict)


def SPA(request):
    index_dict={
    'announcement':Announcement.objects.all()
    }
    countAnnouncement=Announcement.objects.all().count()
    if countAnnouncement == 0:
        DEBUG('Entered no announcement')
        index_dict['announcement']='No announcements'

    # ABOUT
    about='<strong>Something about the church here</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    mission='To know God and proclaim God.'
    vision='To teach the great commandment to do the great comission.'
    index_dict['about']=about
    index_dict['mission']=mission
    index_dict['vision']=vision
    return render(request,'churchApp/app.html',index_dict)

def mobileSPA(request):
    # HOME
    os.environ["TZ"]="Asia/Manila"
    if platform.system() != 'Windows':
        time.tzset()
    today=date.today()
    currDate=today.strftime("%b %d")
    currVerse=VerseOfTheDay.objects.first()
    DEBUG(str(currVerse))
    DEBUG('Passed get VOTD')

    if currVerse.date != currDate:
        count=DevotionalVerse.objects.all().count()
        DEBUG('Got count of all DevVer '+str(count))
        verse=DevotionalVerse.objects.get(pk=random.randrange(1,count+1))
        while(str(currVerse)==verse.BCV):
            DEBUG("VOTD Repeated")
            verse=DevotionalVerse.objects.get(pk=random.randrange(1,count+1))
        DEBUG(verse.BCV+" "+verse.content)
        VerseOfTheDay.objects.all().delete()
        DEBUG("Deleted VOTD")
        insert=VerseOfTheDay.objects.get_or_create(verse=verse.content,BCV=verse.BCV,date=currDate)
        DEBUG("Inserted Chosen Verse")
    currVerse=VerseOfTheDay.objects.first()

    index_dict={
    'verseoftheday':currVerse.verse,
    'BCV':currVerse.BCV,
    'announcement':Announcement.objects.all()
    }
    countAnnouncement=Announcement.objects.all().count()
    if countAnnouncement == 0:
        DEBUG('Entered no announcement')
        index_dict['announcement']='No announcements'

    # PASTOR's CORNER
    sermonList=Sermon.objects.all().order_by('-date')
    latestSermon=sermonList.first()
    sermonDate=latestSermon.date
    sermonDate=sermonDate.strftime("%B %d %Y")
    sermonContent=latestSermon.serviceSermon
    index_dict['date']=sermonDate
    index_dict['sermon']=sermonContent

    # SERMON'S LIST
    sermoncount=Sermon.objects.all().count()
    index_dict['count']=sermoncount
    index_dict['sermonList']=Sermon.objects.all().order_by('-date')

    # COMMENT's
    template_name='mobile.html'
    sermon=get_object_or_404(Sermon)
    comments=sermon.comments.filter(active=False)
    new_comment=None

    # if request.method == 'POST':
    #     comment_form=CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #
    #         new_comment=comment_form.save(commit=False)
    #         new_comment.sermon=sermon
    #         new_comment.save()
    #         comment_form=CommentForm()
    # else:
    #     comment_form=CommentForm()
    index_dict['sermonPost']=sermon
    index_dict['comments']=comments
    index_dict['new_comment']=new_comment
    # index_dict['comment_form']=comment_form


    # ABOUT
    about='<strong>Something about the church here</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    mission='To know God and proclaim God.'
    vision='To teach the great commandment to do the great comission.'
    index_dict['about']=about
    index_dict['mission']=mission
    index_dict['vision']=vision
    return render(request,'churchApp/mobile.html',index_dict)
