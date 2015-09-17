from django.contrib.auth.models import User, Group
from upline.models import *
from rest_framework import serializers
from django.core.files.uploadedfile import SimpleUploadedFile
import mimetypes, json, base64, uuid

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("id", 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = ("id",'groups', 'username', 'email')

class UsernameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username')

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ("id",'title','image','points_range_from','points_range_to')

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
        fields = ("id",'quickblox_id','parent','create_time','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','dream1','dream2','status','level','training_steps')

class MemberRegisterSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.SlugField()
    email = serializers.EmailField()
    grant_type = serializers.CharField(initial="password")
    password = serializers.CharField(style={'input_type': 'password'})
    parent_user = serializers.SlugField()

    def validate_parent_user(self,value):
        members = Member.objects.filter(user__username=value)
        if len(members) != 1:
            raise serializers.ValidationError("Invalid Parent ID")
        return value

    def validate_username(self, value):
        users = User.objects.filter(username=value)
        if len(users) > 0:
            raise serializers.ValidationError("Username already registered")
        return value


    def save(self):
        user = User()
        user.username = self.validated_data['username']
        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.groups.add(Group.objects.get(id=3))
        user.save()
        member = Member()
        member.parent = Member.objects.get(user__username=self.validated_data['parent_user'])
        member.name = self.validated_data['name']
        member.phone = self.validated_data['phone']
        member.gender = self.validated_data['gender']
        member.postal_code = self.validated_data['postal_code']
        member.birthday = self.validated_data['birthday']
        member.user = user
        member.save()

    class Meta:
        model = Member
        fields = ("id",'name','grant_type','parent_user','username','password','phone','birthday','gender','postal_code')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    level = LevelSerializer(many=False, read_only=True)
    training_steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    downlines = DownlineSerializer(many=True, read_only=True)
    avatar_base64 = serializers.CharField(write_only=True)

    def save(self):
        super(MemberSerializer, self).save()
        avatar = validated_data.pop('avatar_base64')
        if len(avatar) > 0:
            avatar_base64 = avatar.split(',')[1]
            avatar_mime = avatar.split(';')[0].split(':')[1]
            avatar_extension = avatar_mime.split('/')[1]
            self.avatar = SimpleUploadedFile(name=str(uuid.uuid4())+'.'+avatar_extension, content=base64.b64decode(avatar_base64), content_type=avatar_mime)
            self.save()

    class Meta:
        model = Member
        fields = ("id","user","avatar_base64",'quickblox_id','parent','downlines','create_time','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','dream1','dream2','status','level','training_steps')

class MemberLoginSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    level = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    training_steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    parent = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    downlines = DownlineSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields = ("id",'user','member_uid','quickblox_id','quickblox_password','parent','downlines','create_time','external_id','name','points','avatar','phone','gender','postal_code','city','state','address','dream1','dream2','status','level','training_steps')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    member = MemberSerializer(read_only=True)
    avatar_base64 = serializers.CharField(write_only=True)

    def create(self,validated_data):
        contact = Contact()
        member = Member.objects.get(user=self.context['request'].user)
        contact.owner = member

        avatar = validated_data.pop('avatar_base64')
        if len(avatar) > 0:
            avatar_base64 = avatar.split(',')[1]
            avatar_mime = avatar.split(';')[0].split(':')[1]
            avatar_extension = avatar_mime.split('/')[1]
            contact.avatar = SimpleUploadedFile(name=str(uuid.uuid4())+'.'+avatar_extension, content=base64.b64decode(avatar_base64), content_type=avatar_mime)

        # contact.avatar = validated_data.pop('avatar')
        contact.email = validated_data.pop('email')
        contact.cellphone = validated_data.pop('cellphone')
        contact.birthday = validated_data.pop('birthday')
        contact.cpf = validated_data.pop('cpf')
        contact.rg = validated_data.pop('rg')
        contact.region = validated_data.pop('region')
        contact.contact_category = validated_data.pop('contact_category')
        contact.name = validated_data.pop('name')
        contact.phone = validated_data.pop('phone')
        contact.gender = validated_data.pop('gender')
        contact.postal_code = validated_data.pop('postal_code')
        contact.city = validated_data.pop('city')
        contact.state = validated_data.pop('state')
        contact.address = validated_data.pop('address')
        contact.save()
        return contact

    class Meta:
        model = Contact
        fields = ("id","avatar_base64","avatar","email","cellphone","birthday","cpf","rg","region",'member','contact_category','name','phone','gender','postal_code','city','state','address')

class ContactDownlineSerializer(serializers.HyperlinkedModelSerializer):
    member = DownlineSerializer(read_only=True)
    class Meta:
        model = Contact
        fields = ("id","avatar","email","cellphone","birthday","cpf","rg","region",'member','contact_category','name','phone','gender','postal_code','city','state','address')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("id","name","active","points","table_value","create_time")

class SaleItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = SaleItem
        fields = ("id","product","quantity","total","notificate_at")

class SaleItemRegisterSerializer(serializers.HyperlinkedModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(many=False, queryset=Sale.objects.all(),write_only=True)
    product = serializers.PrimaryKeyRelatedField(many=False, queryset=Product.objects.all())
    class Meta:
        model = SaleItem
        fields = ("id","product","quantity","notificate_at","sale")

class SaleSerializer(serializers.HyperlinkedModelSerializer):
    client = ContactDownlineSerializer(read_only=True)
    sale_items = SaleItemSerializer(many=True,read_only=True)
    class Meta:
        model = Sale
        fields = ("id","client","sale_items","active","total","points","create_time","paid","sent","send_time")

class SaleRegisterSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.PrimaryKeyRelatedField(many=False, queryset=Contact.objects.all())
    sale_items = SaleItemRegisterSerializer(many=True)
    class Meta:
        model = Sale
        fields = ("id","client","sale_items")

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
    training_steps = TrainingStepSerializer(many=True,read_only=True)
    class Meta:
        model = Training
        fields = ('id','name','training_steps')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id',"user","title","category","content","media","create_time","update_time")

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    def create(self,validated_data):
        calendar = Calendar()
        calendar.name = validated_data.pop('name')
        calendar.user = self.context['request'].user
        calendar.save()
        return calendar

    class Meta:
        model = Calendar
        fields = ("id","name")

class EventSerializer(serializers.HyperlinkedModelSerializer):
    invited = ContactSerializer(many=True,read_only=True)
    members = DownlineSerializer(many=True,read_only=True)
    calendar = CalendarSerializer(read_only=True)

    public = serializers.SerializerMethodField()

    def get_public(self,event):
        return event.calendar.public

    class Meta:
        model = Event
        fields = ("id","public","title","all_day","begin_time","end_time","invited","members","calendar","note","postal_code","number","complement","lat","lng")

class EventRegisterSerializer(serializers.HyperlinkedModelSerializer):
    invited = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=Member.objects.all())
    calendar = serializers.PrimaryKeyRelatedField(many=False, queryset=Calendar.objects.all())

    def create(self,validated_data):
        validated_data['owner'] = self.context['request'].user
        return super(EventRegisterSerializer, self).create(validated_data)

    class Meta:
        model = Event
        fields = ("id","title","all_day","begin_time","end_time","invited","members","calendar","note","postal_code","number","complement","lat","lng")


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ("id","acronym","name")

class CitySerializer(serializers.HyperlinkedModelSerializer):
    state = StateSerializer(many=False)
    class Meta:
        model = State
        fields = ("id","state","name")

class PostalCodeSerializer(serializers.HyperlinkedModelSerializer):
    city = CitySerializer(many=False)
    class Meta:
        model = PostalCode
        fields = ("city","street","neighborhood","postal_code","street_type")

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=False, queryset=Level.objects.all())

    def create(self,validated_data):
        goal = Goal()
        goal.level = validated_data.pop('level')
        member = Member.objects.get(user=self.context['request'].user)
        goal.member = member
        goal.date = validated_data.pop('date')
        goal.save()
        return goal

    class Meta:
        model = Goal
        fields = ("id","level","date")

class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ("id","name","media_file")

class MediaCategorySerializer(serializers.HyperlinkedModelSerializer):
    medias = MediaSerializer(many=True,read_only=True)
    class Meta:
        model = MediaCategory
        fields = ("id","name",",media_type","medias")