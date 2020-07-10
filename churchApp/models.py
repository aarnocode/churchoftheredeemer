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
