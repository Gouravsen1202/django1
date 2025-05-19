
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',views.home,name='home'),
path('menu/',views.menu,name='menu'), #selling
path('order/',views.order,name='order'),#purchase
path('Ragister/',views.ragister,name='Ragister'),
path('login/',views.login,name='login'),
path('logout/', views.logout, name='logout'),
path('track/',views.trackorder,name='track order'),
path('Service/',views.Service,name='Service'),

# for query path=+.........
path('query/<int:pk>/', views.query, name='query'),
path('allquery/<int:pk>/', views.allquery, name='allquery'),
path('edit/<int:pk>/', views.edit, name='edit'),
path('qupdate/<int:pk>/', views.qupdate, name='qupdate'),
path('delete/<int:pk>/', views.delete, name='delete'),



path('home/<int:pk>',views.home1,name='home1'),
path('menu/<int:pk>',views.menu1,name='menu1'),
path('order/<int:pk>',views.order1,name='order1'),
path('track/<int:pk>',views.trackorder1,name='track order1'),
path('Service/<int:pk>',views.Service1,name='Service1'),
path('contact/',views.contact_view, name='contact'),
path('deshbord/<int:pk>',views.dashboard,name='deshbord'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
