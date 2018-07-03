from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class SPM(models.Model):
    fm01 = models.CharField(max_length=10) ##
    fm02 = models.TextField() ##
    fm03 = models.DateTimeField('Date Created', auto_now_add=True)
    fm04 = models.IntegerField(blank=True, default=0)
 
    def __str__(self):
        return self.fm01

class SPD(models.Model):
    fm   = models.ForeignKey(SPM, on_delete=models.CASCADE)
    fd01 = models.CharField(max_length=10) ##
    fd02 = models.TextField() ##
    fd03 = models.DateTimeField('Date Created', auto_now_add=True)
    fd04 = models.IntegerField(blank=True, default=0)
 
    def __str__(self):
        return self.fd01

class Poll(models.Model): 
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices',on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ("poll", "voted_by")