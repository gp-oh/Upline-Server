from django.contrib.auth.models import User, Group
from upline.models import *
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("id",'url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id",'url', 'username', 'email', 'groups')

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ("id",'title','points_range_from','points_range_to')

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = ("id",'name',)

class TrainingSetpSerializer(serializers.HyperlinkedModelSerializer):
    training = TrainingSerializer()
    class Meta:
        model = TrainingStep
        fields = ("id",'training','title','media','step','description',)

class DownlineSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    training_steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Member
        fields = ("id",'parent','slug','create_time','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','dream','status','level','training_steps')

class MemberRegisterSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.EmailField()
    grant_type = serializers.CharField(initial="password")
    password = serializers.CharField(style={'input_type': 'password'})
    parent_slug = serializers.SlugField()

    def validate_parent_slug(self,value):
        members = Member.objects.filter(slug=value)
        if len(members) != 1:
            raise serializers.ValidationError("Invalid Parent ID")
        return value

    def validate_email(self, value):
        users = User.objects.filter(username=value)
        if len(users) > 0:
            raise serializers.ValidationError("Email already registered")
        return value


    def save(self):
        user = User()
        user.username = self.validated_data['username']
        user.email = self.validated_data['username']
        user.set_password(self.validated_data['password'])
        user.save()
        member = Member()
        member.parent = Member.objects.get(slug=self.validated_data['parent_slug'])
        member.name = self.validated_data['name']
        member.phone = self.validated_data['phone']
        member.gender = self.validated_data['gender']
        member.postal_code = self.validated_data['postal_code']
        member.birthday = self.validated_data['birthday']
        member.user = user
        member.save()

    class Meta:
        model = Member
        fields = ("id",'name','grant_type','parent_slug','username','password','phone','birthday','gender','postal_code')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    training_steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    downlines = DownlineSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields = ("id",'parent','downlines','create_time','slug','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','dream','status','level','training_steps')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    contact_category = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    member = MemberSerializer()
    class Meta:
        model = Contact
        fields = ("id",'member','contact_category','name','phone','gender','postal_code','city','state','address')

class DistributionCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DistributionCenter
        fields = ("id",'name')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("id","name","active","reference_value","table_value","create_time")

class SaleItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = SaleItem
        fields = ("id","product","quantity","total","delivery_prevision","notificate_at")

class SaleSerializer(serializers.HyperlinkedModelSerializer):
    client = ContactSerializer()
    sale_items = SaleItemSerializer(many=True)
    class Meta:
        model = Sale
        fields = ("id","client","sale_items","active","total","points","create_time")

class TrainingStepSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    def get_status(self,training_step):
        members = training_step.members.filter(member__user=self.context['request'].user)
        if len(members) > 0:
            return True
        return False

    def get_answer(self,training_step):
        members = training_step.members.filter(member__user=self.context['request'].user)
        if len(members) > 0:
            return members[0].answer
        return None

    class Meta:
        model = TrainingStep
        fields = ('id','status','answer','title','media','step','description','need_answer')

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    training_steps = TrainingStepSerializer(many=True)
    class Meta:
        model = Training
        fields = ('id','name','training_steps')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ('id',"user","title","category","content","media","create_time","update_time")


