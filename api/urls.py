from django.urls import path
from . import views
 
urlpatterns = [
    path('list/', views.car_list_view),
              #dynamic url
    path('<int:pk>',views.car_details_api),
    path('showroom',views.Showroom_list_api.as_view()),
]