# # 1) ///////////  Class-based Views ////////////////////
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions
# from django.contrib.auth.models import User
# from .authentication import TokenAuthentication


# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)


# 2) ///////////  Function Based Views ////////////////////
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

# 3) ///////////  Function Based Views ////////////////////
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})