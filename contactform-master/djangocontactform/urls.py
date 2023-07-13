from django.contrib import admin
from django.urls import path,include

from contact.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('', include('contact.urls')),
    path('', include('django.contrib.auth.urls')),
]
