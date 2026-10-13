from django.urls import path
from . import views
# registerer urls
    # register
        # login
            # logout
app_name = 'registerer'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview'),
]
