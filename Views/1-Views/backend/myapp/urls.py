# #  1)  ///////////  Class-based Views    //////////

# from django.urls import path
# from .views import ListUsers
# from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns = [
#     path('list/', ListUsers.as_view()),    
#     path('auth/', obtain_auth_token),
# ]


# # 2)  ///////////  Class-based Views    //////////
from django.urls import path
from .views import hello_world
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', hello_world ),    
    
]
