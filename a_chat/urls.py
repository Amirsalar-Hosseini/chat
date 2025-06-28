from django.urls import path
from a_chat.views import *

urlpatterns = [
    path('', chat_view, name='home'),
]