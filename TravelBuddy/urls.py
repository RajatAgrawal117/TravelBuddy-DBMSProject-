from django.contrib import admin
from django.urls import path,include
from django.urls import path
from recco import urls
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("recco.urls"))
]
