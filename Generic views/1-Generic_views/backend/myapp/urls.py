# # 1)  /////////////////////
# from django.urls import path
# from .views import home_api

# urlpatterns = [
#     path('', home_api)
# ]

# 2)  /////////////////////
from django.urls import path
from .views import UserList
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('list/', UserList.as_view()),
    path('create/', UserList.as_view()),
    path('auth/', obtain_auth_token),
]

