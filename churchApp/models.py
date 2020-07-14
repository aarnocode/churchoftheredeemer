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
