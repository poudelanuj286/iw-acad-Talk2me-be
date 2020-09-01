from django.contrib import admin

# Register your models here.
from .models import Feed, FeedLike


class FeedLikeAdmin(admin.TabularInline):
    model = FeedLike

class FeedAdmin(admin.ModelAdmin):
    inlines = [FeedLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Feed

admin.site.register(Feed, FeedAdmin)
