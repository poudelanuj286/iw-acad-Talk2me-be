import random
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
User = settings.AUTH_USER_MODEL

class FeedLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey("Feed", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Feed(models.Model):
    # many users can many contents
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='feed_user', blank=True, through=FeedLike)
    content = RichTextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:   
        ordering = ['-id']

    @property
    def is_share(self):
        return self.parent != None
    

    def serialize(self):
        return{
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }