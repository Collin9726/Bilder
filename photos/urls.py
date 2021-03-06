from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^all-photos/$', views.all_photos, name = 'all_photos'),
    url(r'^all-categories/$', views.all_categories, name = 'all_categories'),
    url(r'^photo/(\d+)',views.display_photo,name = 'display_photo'),
    url(r'^category/(\d+)',views.display_category,name = 'display_category'),
    url(r'^search/', views.search_categories, name='search_categories'),
    url(r'^location/(\d+)',views.display_location,name = 'display_location'),
    url(r'^all-locations/$', views.all_locations, name = 'all_locations'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)