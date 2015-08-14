from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from upline.serializers import *
from upline.models import *
from rest_framework.response import Response


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
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ContactViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Contact.objects.filter(owner__user=request.user)
        serializer = ContactSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contact.objects.filter()
    serializer_class = ContactSerializer