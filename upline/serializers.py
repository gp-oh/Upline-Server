from django.contrib.auth.models import User, Group
from upline.models import *
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('title','points_range_from','points_range_to')

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = ('name',)

class TrainingSetpSerializer(serializers.HyperlinkedModelSerializer):
    training = TrainingSerializer()
    class Meta:
        model = TrainingStep
        fields = ('training','title','media','step','description',)

class DownlineSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    training_steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Member
        fields = ('parent','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','dream','status','level','training_steps')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    training_steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    downlines = DownlineSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields = ('parent','downlines','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','dream','status','level','training_steps')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    contact_category = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    member = MemberSerializer()
    class Meta:
        model = Contact
        fields = ('member','contact_category','name','phone','gender','postal_code','city','state','address')




