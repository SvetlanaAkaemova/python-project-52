from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('users/', include('task_manager.users.urls')),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
]
