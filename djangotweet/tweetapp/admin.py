from django.contrib import admin
from tweetapp.models import tweet
# Register your models here.

class tweetadmin(admin.ModelAdmin):
    fieldsets=[
        ('message group',{"fields":["message"]}),
        ('nickname group',{"fields":["nickname"]})
        
    ]

    
    #fields=['nickname','message']



admin.site.register(tweet,tweetadmin)
