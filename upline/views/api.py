import json, datetime, urllib
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from upline.forms import *
from upline.models import *
from upline.permissions import IsAuthenticatedOrCreate
from upline.serializers import *
from oauthlib.oauth2 import Server
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.models import AccessToken
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route, list_route
from django.db.models import Q
from django.http import HttpRequest

class Login(APIView,OAuthLibMixin):
    permission_classes = (permissions.AllowAny,)
    server_class = Server
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def post(self,request, *args, **kwargs):
        params = json.loads(request.body)
        # request.body = params
        request.POST = params
        print request.POST
        url, headers, body, s = self.create_token_response(request)
        token = json.loads(body)
        if s == 200:
            user = AccessToken.objects.get(token=token["access_token"]).user
            member = Member.objects.get(user=user)
            serializer = MemberLoginSerializer(member)
            return Response({"token":token,"member":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(token, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = Member.objects.all()
    server_class = Server
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def list(self, request):
        queryset = Member.objects.filter(parent__user=request.user)
        serializer = MemberSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = MemberRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Login.as_view()(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return MemberRegisterSerializer
        else:
            return MemberSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request):
        queryset = Contact.objects.filter(owner__user=request.user)
        serializer = ContactSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    @list_route(methods=['get'])
    def send(self,request):
        sales = Sale.objects.filter(active=True,sent=False,member__user=request.user)
        print sales
        for sale in sales:
            sale.sent = True
            sale.send_time = datetime.datetime.now()
            sale.save()
        serializer = SaleSerializer(sales,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['get'])
    def inactive(self,request, pk=None):
        sale = self.get_object()
        if sale.active and not sale.sent and sale.member.user == request.user:
            sale.active = False
            sale.save()
            serializer = SaleSerializer(sale)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':['Invalid sale']}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Sale.objects.filter(member__user=request.user)
        serializer = SaleSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        sale = Sale()
        sale.member = Member.objects.get(user=request.user)
        sale.client = Contact.objects.get(id=request.data['client'])
        sale.save()
        sale_items = []
        for sale_item in request.data['sale_items']:
            sale_item['sale'] = sale.id
            si = SaleItemRegisterSerializer(data=sale_item)
            if si.is_valid():
                si.save()
            else:
                print si.errors
            serializer = SaleSerializer(sale)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return SaleRegisterSerializer
        else:
            return SaleSerializer

class TrainingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class UsernameViewSet(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    def retrieve(self, request, pk=None):
        queryset = User.objects.filter(username=pk)
        if len(queryset) > 0:
            return Response({'status':False}, status=status.HTTP_417_EXPECTATION_FAILED)
        return Response({'status':True}, status=status.HTTP_202_ACCEPTED)
        
    queryset = User.objects.all()
    serializer_class = UsernameSerializer

class PostalCodeViewSet(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    def retrieve(self, request, pk=None):
        queryset = PostalCode.objects.all()
        user = get_object_or_404(queryset, postal_code=pk)
        serializer = PostalCodeSerializer(user)
        return Response(serializer.data)

    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer

class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityViewSet(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    def retrieve(self, request, pk=None):
        queryset = City.objects.filter(state__acronym=pk)
        serializer = CitySerializer(queryset,many=True)
        return Response(serializer.data)

    queryset = City.objects.all()
    serializer_class = CitySerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    def list(self, request):
        queryset = Calendar.objects.filter(Q(public=True) | Q(user=request.user))
        serializer = CalendarSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return EventRegisterSerializer
        else:
            return EventSerializer
            
class MediaCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MediaCategory.objects.all()
    serializer_class = MediaCategorySerializer

