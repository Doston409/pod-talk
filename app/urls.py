from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login_page, name="login_page"),
    path('about/', views.about_page, name="about_page"),
    path('contact/', views.contact_page, name="contact_page"),
    path('detail-page/', views.detail_page, name="detail_page"),
    path('listing_page/', views.listing_page, name="listing_page"),

]
