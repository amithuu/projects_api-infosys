from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('login', obtain_auth_token, name = 'login'),
    path('register', views.register_view, name = 'register'),
    path('logout', views.logout_view, name = 'logout'),
    
    path('api/token', TokenObtainPairView.as_view(), name = 'token_obtain_pair'), #? login
    path('api/token/refresh', TokenRefreshView.as_view(), name = 'token_refresh_view'),  #? Register
    
    path('job_post/', views.PostListAPIView.as_view(), name = 'job_post_list'),
    path('job_post/create', views.PostCreateAPIView.as_view(), name = 'job_post_create'),
    path('job_post/<pk>/', views.PostUpdateAPIView.as_view(), name = 'job_post_detail'),
    
    path('onboarding/', views.OnboardingListCreateView, name = 'onboarding'),
    path('onboarding/<pk>/', views.OnboardingUpdateView, name = 'onboarding'),
    
]

