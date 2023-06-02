# 1) ///////////////
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view()
# def home_api(request):
#     return Response({'name':'Elyor'})

## 2) //////////////////////
# from django.contrib.auth.models import User
# from myapp.serializers import UserSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
# from .authentication import TokenAuthentication

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]
#     authentication_classes = [TokenAuthentication]


# # 2) //////////////////////
# from django.contrib.auth.models import User
# from myapp.serializers import UserSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
# from .authentication import TokenAuthentication
# from rest_framework.response import Response

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]
#     authentication_classes = [TokenAuthentication]

#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)


# # 3) //////////////////////
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .authentication import TokenAuthentication
from rest_framework.response import Response

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
 


