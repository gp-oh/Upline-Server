import json
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

class Login(APIView,OAuthLibMixin):
    permission_classes = (permissions.AllowAny,)
    server_class = Server
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def post(self,request, *args, **kwargs):
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

    def list(self, request):
        queryset = Sale.objects.filter(member__user=request.user)
        serializer = SaleSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

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

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

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

