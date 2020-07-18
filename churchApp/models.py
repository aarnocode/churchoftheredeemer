from django.db import models

# Create your models here.
class DevotionalVerse(models.Model):
    content=models.CharField(max_length=900, unique=True)
    BCV=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.BCV

class VerseOfTheDay(models.Model):
    verse=models.CharField(max_length=900,unique=True)
    BCV=models.CharField(max_length=264,unique=True)
    date=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.BCV

class Sermon(models.Model):
    date=models.DateField(unique=True)
    serviceSermon=models.TextField()

    def __str__(self):
        return str(self.date)

class Announcement(models.Model):
    announcement=models.CharField(max_length=900, unique=True)

    def __str__(self):
        return self.announcement

class Comment(models.Model):
    sermon = models.ForeignKey(Sermon,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)

    class Meta:
        ordering=['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
