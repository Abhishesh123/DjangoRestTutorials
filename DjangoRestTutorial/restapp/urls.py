from django.urls import path
from restapp import views
 
 
urlpatterns = [
        path('', views.index),
        path('choice/', views.choice_list),
        path('choice_list_id/<int:pk>/',views.choice_list_id, name='choice_list_id')
        
#         
    ] 
