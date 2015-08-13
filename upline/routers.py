from rest_framework import routers
from upline.views import api

def router():
    r = routers.DefaultRouter()
    r.register(r'users', api.UserViewSet)
    r.register(r'groups', api.GroupViewSet)
    return r