from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path("register/",views.register,name="register"),
    path("home/",views.home,name="home"),
    path("projects/", views.projects,name="projects"),
    path("contact/", views.contact,name="contact"),

    path("gallery/", views.gallery,name="gallery"),
]
urlpatterns+=staticfiles_urlpatterns()
