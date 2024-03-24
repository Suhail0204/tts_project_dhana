from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.tts_view),
   path('stt',views.stt_view)

]