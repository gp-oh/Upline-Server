from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from upline.serializers import *
from upline.models import *
from upline.forms import *
from rest_framework.response import Response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from oauth2_provider.views import TokenView
from upline.permissions import IsAuthenticatedOrCreate

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = Member.objects.all()
    def list(self, request):
        queryset = Member.objects.filter(parent__user=request.user)
        serializer = MemberSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = MemberRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return TokenView.as_view()(request, *args, **kwargs)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        print 'Method is:', self.request.method
        if self.request.method == "POST":
            return MemberRegisterSerializer
        else:
            return MemberSerializer

class ContactViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Contact.objects.filter(owner__user=request.user)
        serializer = ContactSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class SaleViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Sale.objects.filter(member__user=request.user)
        serializer = SaleSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer