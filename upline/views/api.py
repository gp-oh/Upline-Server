# -*- coding: utf-8 -*-
import json
import datetime
from django.contrib.auth.models import User, Group
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
from rest_framework.decorators import list_route
from decimal import Decimal
from rest_framework_bulk import BulkCreateModelMixin


class Login(APIView, OAuthLibMixin):
    permission_classes = (permissions.AllowAny,)
    server_class = Server
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        request.POST = params
        url, headers, body, s = self.create_token_response(request)
        token = json.loads(body)
        if s == 200:
            user = AccessToken.objects.get(token=token["access_token"]).user
            members = Member.objects.filter(user=user)
            if len(members) > 0:
                member = members[0]
                serializer = MemberLoginSerializer(
                    member, context={'request': request})
                training_step = TrainingStepLoginSerializer(
                    SiteConfiguration.get_solo().first_training, context={'request': request})
                return Response({"token": token, "member": serializer.data, "first_training_step": training_step.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"token": token}, status=status.HTTP_201_CREATED)
        else:
            return Response(token, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrCreate,)
    queryset = Member.objects.all()
    server_class = Server
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    def list(self, request):
        if "only_children" in request.GET and len(request.GET['only_children']) == 1 and request.GET['only_children'] == "0":
            queryset = Member.objects.get(user=request.user).get_descendants()
        else:
            queryset = Member.objects.filter(parent__user=request.user)

        if "member_type" in request.GET and len(request.GET['member_type']) == 1:
            queryset = queryset.filter(member_type=request.GET['member_type'])
        serializer = MemberSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = MemberRegisterSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MemberSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            if 'avatar_base64' in request.data:
                avatar = request.data['avatar_base64']
                if len(avatar) > 0:
                    avatar_base64 = avatar.split(',')[1]
                    avatar_mime = avatar.split(';')[0].split(':')[1]
                    avatar_extension = avatar_mime.split('/')[1]
                    instance.avatar = SimpleUploadedFile(name=str(uuid.uuid4(
                    )) + '.' + avatar_extension, content=base64.b64decode(avatar_base64), content_type=avatar_mime)

            if 'dream1_base64' in request.data:
                dream1 = request.data['dream1_base64']
                if len(dream1) > 0:
                    dream1_base64 = dream1.split(',')[1]
                    dream1_mime = dream1.split(';')[0].split(':')[1]
                    dream1_extension = dream1_mime.split('/')[1]
                    instance.dream1 = SimpleUploadedFile(name=str(uuid.uuid4(
                    )) + '.' + dream1_extension, content=base64.b64decode(dream1_base64), content_type=dream1_mime)

            if 'dream2_base64' in request.data:
                dream2 = request.data['dream2_base64']
                if len(dream2) > 0:
                    dream2_base64 = dream2.split(',')[1]
                    dream2_mime = dream2.split(';')[0].split(':')[1]
                    dream2_extension = dream2_mime.split('/')[1]
                    instance.dream2 = SimpleUploadedFile(name=str(uuid.uuid4(
                    )) + '.' + dream2_extension, content=base64.b64decode(dream2_base64), content_type=dream2_mime)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action == "create":
            return MemberRegisterSerializer
        else:
            return MemberSerializer


class ContactViewSet(viewsets.ModelViewSet, BulkCreateModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request):
        queryset = Contact.objects.filter(owner__user=request.user)
        if "contact_category" in request.GET and len(request.GET['contact_category']) == 1:
            queryset = queryset.filter(
                contact_category=request.GET['contact_category'])
        serializer = ContactSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    @list_route(methods=['get'])
    def send(self, request):
        sales = Sale.objects.filter(status=0, member__user=request.user)
        for sale in sales:
            sale.status = 1
            sale.send_time = datetime.datetime.now()
            sale.save()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def inactive(self, request):
        sales = request.POST.get('sale_ids')
        for sale in sales:
            if sale.status == 0 and sale.member.user == request.user:
                sale.remove()
            else:
                return Response({'error': {'message': 'Invalid sale', 'sale_id': sale.id}}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': True}, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = Sale.objects.filter(member__user=request.user)
        if 'status' in request.GET:
            queryset = queryset.filter(status=int(request.GET['status']))
        serializer = SaleSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        sale = Sale()
        sale.member = Member.objects.get(user=request.user)
        sale.client = Contact.objects.get(id=request.data['client_id'])
        sale.save()
        total = Decimal('0.00')
        total_points = Decimal('0.00')
        for sale_item in request.data['sale_items']:
            sale_item['sale'] = sale.id
            si = SaleItemRegisterSerializer(data=sale_item)
            if si.is_valid():
                s = si.save()
                total_points += s.product.points * s.quantity
                s.total = s.product.table_value * s.quantity
                total += s.total
                s.save()
            else:
                print si.errors
        sale.points = total_points
        sale.total = total
        sale.save()
        serializer = SaleSerializer(sale)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors,
        # status=status.HTTP_400_BAD_REQUEST)

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

    def list(self, request):
        queryset = Post.objects.filter(
            groups__in=request.user.groups.all(), converted=True).order_by('-update_time')
        if 'limit' in request.GET and 'offset' in request.GET:
            offset = int(request.GET['offset'])
            limit = int(request.GET['offset']) + int(request.GET['limit'])
            if len(queryset) >= limit:
                queryset = queryset[offset:limit]
            elif len(queryset) >= offset:
                queryset = queryset[offset:]
            else:
                queryset = []

        serializer = PostSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class UsernameViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter(username=pk)
        if len(queryset) > 0:
            return Response({'status': False}, status=status.HTTP_417_EXPECTATION_FAILED)
        return Response({'status': True}, status=status.HTTP_202_ACCEPTED)

    queryset = User.objects.all()
    serializer_class = UsernameSerializer


class PostalCodeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    def retrieve(self, request, pk=None):
        queryset = PostalCode.objects.all()
        user = get_object_or_404(queryset, postal_code=pk)
        serializer = PostalCodeSerializer(user)
        return Response(serializer.data)

    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer
    permission_classes = (permissions.AllowAny,)


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    def retrieve(self, request, pk=None):
        queryset = City.objects.filter(state__acronym=pk)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    queryset = City.objects.all()
    serializer_class = CitySerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def list(self, request):
        member = Member.objects.get(user=request.user)
        queryset = Goal.objects.filter(
            member=member, level__points_range_from__gt=member.points)
        serializer = GoalSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MemberTrainingStepViewSet(viewsets.ModelViewSet):
    queryset = MemberTrainingStep.objects.all()
    serializer_class = MemberTrainingStepSerializer

    def list(self, request):
        queryset = MemberTrainingStep.objects.filter(member__user=request.user)
        serializer = MemberTrainingStepSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CalendarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer_class(self):
        print self.action
        if self.action == "create" or self.action == "update" or self.action == "partial_update":
            return EventRegisterSerializer
        else:
            return EventSerializer

    def list(self, request):
        queryset = Event.objects.filter(owner=request.user)
        serializer = EventSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class InviteViewSet(viewsets.ModelViewSet):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    def list(self, request):
        queryset = Invite.objects.filter(member__user=request.user)
        serializer = InviteSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class MediaCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MediaCategory.objects.all()
    serializer_class = MediaCategorySerializer
