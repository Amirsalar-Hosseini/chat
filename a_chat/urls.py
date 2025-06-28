from django.urls import path
from a_chat.views import *

app_name = 'a_chat'
urlpatterns = [
    path('', ChatView.as_view(), name='home'),
]