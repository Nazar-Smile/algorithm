
from django.urls import path
from .views import *
urlpatterns = [
    path('questions-list/', QuestionView.as_view()),
    path('categories-list/', CategoryView.as_view()),
    path('services-list/', ServicesView.as_view()),
    path('aboutus-list/', AboutUsView.as_view()),
    path('team-list/', TeamView.as_view()),
    path('information-list/', InformationView.as_view()),
    path('contacts-list/', ContactsView.as_view()),

]
