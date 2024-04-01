from django import forms
from django.forms import ModelForm
from tweetapp.models import tweet


class addtweetform(forms.Form):
    nickname_input = forms.CharField(label="nickname", max_length=10)
    message_input = forms.CharField(label="message", max_length=100,)
    
    


class addtweetmodelform(ModelForm):
        class Meta:
            model=tweet
            fields=["username","message"]
    
