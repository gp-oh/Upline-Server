from django.conf.urls import url, include
from rest_framework import routers
from upline.views import api
from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet, GCMDeviceAuthorizedViewSet

r = routers.DefaultRouter()
r.register(r'sale', api.SaleViewSet)
r.register(r'contact', api.ContactViewSet)
r.register(r'member', api.MemberViewSet)
r.register(r'training', api.TrainingViewSet)
r.register(r'post', api.PostViewSet)
r.register(r'event', api.EventViewSet)
r.register(r'state', api.StateViewSet)
r.register(r'city', api.CityViewSet)
r.register(r'postal-code', api.PostalCodeViewSet)
r.register(r'goal', api.GoalViewSet)
r.register(r'product', api.ProductViewSet)
r.register(r'level', api.LevelViewSet)
r.register(r'calendar', api.CalendarViewSet)
r.register(r'media', api.MediaCategoryViewSet)
r.register(r'apns', APNSDeviceAuthorizedViewSet)
r.register(r'gcm', GCMDeviceAuthorizedViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/v1/', include(r.urls)),
    url(r'^api/v1/login/$',api.Login.as_view())
]