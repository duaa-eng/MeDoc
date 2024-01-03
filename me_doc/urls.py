from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_app.urls')),  # Assuming you have defined URLs in webapp.urls
    path('/chatbot', include('chatbot_app.urls')),  # Include the URLs of your chatbot
    # Add a path for the root URL
]