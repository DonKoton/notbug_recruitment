from django.urls import path

from blog import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "blog"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='details'),
    path('add-post/', views.AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='blog:home'), name='logout'),
]
