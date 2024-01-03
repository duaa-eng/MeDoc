# # chatbot_app/urls.py


from django.urls import path
from chatbot_app.views import chatbot_view, getResponse

urlpatterns = [
    path('', chatbot_view, name='chatbot_view'),
    path('chatbot/getResponse', getResponse, name='getResponse')
]


