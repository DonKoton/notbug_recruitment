from django.urls import path

from cars import views

app_name = "cars"

urlpatterns = [
    path('cars-list/', views.CarsList.as_view(), name='cars_list'),
    path('store/', views.StoreCarView.as_view(), name='store_car'),
    path('car/<int:pk>', views.CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/add-part/', views.AddPartView.as_view(), name='add_part'),
    path('car/update/<int:pk>/', views.UpdateCarView.as_view(), name='update'),
    path('car/<int:pk>/delete/', views.DeleteCarView.as_view(), name='delete'),
]
