from django.conf.urls import url, include
from rest_framework import routers
from upline.views import api

r = routers.DefaultRouter()
r.register(r'users', api.UserViewSet)
r.register(r'sales', api.SaleViewSet)
r.register(r'groups', api.GroupViewSet)
r.register(r'contacts', api.ContactViewSet)
r.register(r'member', api.MemberViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/v1/', include(r.urls)),
]