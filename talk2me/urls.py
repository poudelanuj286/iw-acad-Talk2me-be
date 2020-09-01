from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from feeds import urls as feeds_url
from auth_system import urls as auth_system_url #added
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home_view),
    # path('create-feed', feed_create_view),
    # path('feeds', feed_list_view),
    # path('feeds/<int:feed_id>', feed_detail_view),
    # path('api/feeds/<int:feed_id>/delete', feed_delete_view),
    path('api/feeds/', include(feeds_url)),
    # djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path(r'mdeditor/', include('mdeditor.urls'))
    # path('auth/', include('djoser.urls.authtoken'))
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)