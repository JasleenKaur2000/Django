from django.contrib import admin
from django.urls import path

from lead.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page),
]
