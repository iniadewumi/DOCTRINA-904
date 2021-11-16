"""Doctrina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from Pages.views import HomepageView, About, SearchResultsView
from Nurses.views import login_page, registration_page, nurse_authenticate, auth2
from Doctors.views import DoctorPage
from Hospitals.views import HospitalPage
from Ratings.views import RateDoctor, ThankYou

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomepageView.as_view(), name="Home"),
    path('admin/', admin.site.urls),
    path('home/', HomepageView.as_view()),

    path('about/', About),
    path('login/', login_page),
    path('signup/', registration_page),

    path('search_results', SearchResultsView.as_view(), name="results"),
    path('<int:hospital_npi_id>/hospital/', HospitalPage),
    path('<int:doctor_npi_id>/doctor/', DoctorPage),
    path('<int:doctor_npi_id>/ratedoctor/', RateDoctor),
    path('<int:doctor_npi_id>/thank_you', ThankYou),
    path('nurse_authenticate', nurse_authenticate),
    path("auth2/", auth2)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

