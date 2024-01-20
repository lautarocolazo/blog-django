from django.contrib import admin
from django.urls import path, include
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("", views.home_page, name="home"),
    path("blog/", include("blog.urls")),
]
