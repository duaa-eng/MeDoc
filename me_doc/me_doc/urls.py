"""
URL configuration for me_doc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('patient', views.PatientApiView.as_view()),
    # path('doctor', views.DoctorApiView.as_view()),
    path('patients/',views.PatientAPIView.as_view(), name='patients'),
    path('patients/<int:pk>/',views. PatientDetailAPIView.as_view(), name='patient-detail'),
    path('doctors/', views.DoctorAPIView.as_view(), name='doctors'),
    path('doctors/<int:pk>/',views.DoctorDetailAPIView.as_view(), name='doctor-detail'),
    # ... other url patterns ...
    path('chatbot/', include('chatbot_app.urls')),  # Include the URLs of chatbot app
    path('doctor-appointments/', views.DoctorAppointmentAPIView.as_view(), name='doctor-appointments'),
    path('doctor-appointments/<int:pk>/', views.DoctorAppointmentDetailAPIView.as_view(), name='doctor-appointment-detail'),
    path('patient-appointments/', views.PatientAppointmentAPIView.as_view(), name='patient-appointments'),
    path('patient-appointments/<int:pk>/', views.PatientAppointmentDetailAPIView.as_view(), name='patient-appointment-detail'),
    # ... other url patterns ...
]


# ]
# urlpatterns = [  
#     path('admin/', admin.site.urls),  
#     path('api-auth/', include('rest_framework.urls')),
#     path('patient', views.patient),  
#     path('show',views.show),  
#     path('edit/<int:id>', views.edit),  
#     path('update/<int:id>', views.update),  
#     path('delete/<int:id>', views.destroy),  
# ]  