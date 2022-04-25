from django.contrib import admin
from dbapp.models import Article

# Register your models here.

class ArticleAdimin(admin.ModelAdmin):
    list_display = ('id','code','name','price','pub_date')\

admin.site.register(Article, ArticleAdimin)
    