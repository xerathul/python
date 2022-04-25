from django.db import models

# Create your models here. 테이블 선언

class Article(models.Model):
    code = models.CharField(max_length=10)  #max_length=10 => Varchar
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    
