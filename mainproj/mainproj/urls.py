from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mapapp import views as mapapp_views
from mainapp import views as main_views
from accounts import views as accounts_views
from frameapp import views as frameapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('detail/<int:post_id>', main_views.detail, name="detail"),
    path('mypage/', include('frameapp.urls')),
    path('newpost/', main_views.postformcreate, name='newpost'),
    path('map/', mapapp_views.map, name='map'),
    path('event/', main_views.event, name='event'),
    path('reward/', main_views.reward, name='reward'),
    path('detail_img/',main_views.detail_img, name='detail_img'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)