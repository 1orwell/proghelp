from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField("date of event")
    venue = models.CharField(max_length=200)
    langauge = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    details = models.TextField()
    def __unicode__(self):
        return self.name 
