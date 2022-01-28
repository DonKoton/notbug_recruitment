from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='details'),
    path('add-post/', views.AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
