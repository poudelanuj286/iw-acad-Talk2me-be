from django.urls import path

from .views import (
    home_view,
    feed_action_view,
    feed_delete_view,
    feed_detail_view,
    feed_list_view,
    feed_create_view
)

'''
CLIENT
Base ENDPOINT /api/feeds/
'''
urlpatterns = [
    path('', feed_list_view),
    # ph563z
    path('action/', feed_action_view),
    path('create/', feed_create_view),
    path('<int:feed_id>/', feed_detail_view),
    path('<int:feed_id>/delete/', feed_delete_view),
    # path('try', try_view),
]
