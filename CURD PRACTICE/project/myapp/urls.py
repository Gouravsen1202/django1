from django.urls import path
from myapp import views

urlpatterns = [
    path('form/',views.form,name='form'),
    path('update/',views.update,name='update'),
    
]