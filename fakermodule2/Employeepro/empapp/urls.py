from django.urls import path
from . import views


urlpatterns = [
   
    path('show/', views.ShowEmp_view, name='showdata_url'),
    path('fd/',views.FakerData, name='fakedata_url')
   
]