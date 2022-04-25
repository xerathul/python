from django.db import models

# Create your models here.
class Guest(models.Model):
    #ID 자동생성 방지
    #myno = models.AutoField(auto_created = True, primary_key = True)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    class Meta:
        #ordering=('title',)
        ordering=('-id',)