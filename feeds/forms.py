from django import forms
from django.conf import settings

from .models import Feed


MAX_FEED_LENGTH = settings.MAX_FEED_LENGTH

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['content']
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_FEED_LENGTH:
            raise forms.ValidationError("This post is too long")
        return content