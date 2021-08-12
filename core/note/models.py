from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    name = models.CharField(unique=True, max_length=240,blank=False)

    def __str__(self):
        return self.name


class Note(models.Model):
    COLORS = (
        ('y', 'yellow'),
        ('w', 'white'),
        ('r', 'red'),
        ('b', 'blue')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    title = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length=255,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    color = models.CharField(max_length=1, choices=COLORS, default='w')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

