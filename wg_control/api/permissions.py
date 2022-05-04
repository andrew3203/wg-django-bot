from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Order, Referral, User, Client


class IsOwnerOrAdminUser(BasePermission):

    def has_permission(self, request, view):  
        client = request.user
        if client and (client.is_staff or client.is_superuser):
            return True

        a = str(type(view)) == "<class 'api.views.UserViewSet'>" and request.method != 'POST'
        b = str(type(view)) == "<class 'api.views.ReferralViewSet'>" 
        c = str(type(view)) == "<class 'api.views.OrderViewSet'>" 
        d = str(type(view)) == "<class 'api.views.UserViewSet'>" and request.method == 'POST'

        if client and client.is_authenticated:
            return a or b or c
        else:
            return d

        

    def has_object_permission(self, request, view, obj):
        
        
        print(request.method, '- - - - - - - - - - - - ')


        client = request.user
        if client and (client.is_staff or client.is_superuser):
            return True

        if str(type(obj)) == "<class 'api.models.Client'>":
            return obj == client

        elif str(type(obj)) == "<class 'api.models.User'>":
            return obj.client == client

        elif str(type(obj)) == "<class 'api.models.Referral'>":
            return obj.owner.client == client 

        elif str(type(obj)) == "<class 'api.models.Order'>":
            return obj.user.client == client

        return False


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
