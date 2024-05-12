from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.aboutus, name="aboutus"),
    path("faqs", views.faqs, name="faqs"),
    path("gallery", views.gallery, name="gallery"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("service", views.service, name="service"),
]