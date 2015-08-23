from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class State(models.Model):
    acronym = models.CharField(max_length=2)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name ='State'
        verbose_name_plural ='States'

    def __unicode__(self):
        return self.acronym
    
class City(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name ='City'
        verbose_name_plural ='Citys'

    def __unicode__(self):
        return self.state.acronym+' - '+self.name

    def to_json(self):
        return {'state':self.state.acronym,'name':self.name,'id':self.id}

class PostalCode(models.Model):
    city = models.ForeignKey(City)
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    street_type = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    class Meta:
        verbose_name ='Postal Code'
        verbose_name_plural ='Postal Codes'

    def __unicode__(self):
        return self.postal_code

    def to_json(self):
        return { 'city':self.city.name,'state':self.city.state.acronym,'street':'%s %s'%(self.street_type,self.street),'zip_code':self.zip_code, 'neighborhood':self.neighborhood }


class Training(models.Model):
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Training"
        verbose_name_plural = "Trainings"

    def __unicode__(self):
        return self.name

class TrainingStep(models.Model):
    training = models.ForeignKey(Training,related_name='training_steps')
    title = models.CharField(max_length=255)
    media = models.FileField(upload_to="training_steps",blank=True, null=True)
    step = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    need_answer = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Training Step"
        verbose_name_plural = "Training Steps"

    def __unicode__(self):
        return self.title

class Level(models.Model):
    title = models.CharField(unique=True, max_length=255)
    points_range_from = models.IntegerField()
    points_range_to = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"

    def __unicode__(self):
        return self.title

class Member(models.Model):
    user = models.OneToOneField(User)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='downlines')
    external_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    quickblox_id = models.CharField(max_length=255,null=True)
    quickblox_login = models.CharField(max_length=255,null=True)
    quickblox_password = models.CharField(max_length=255,null=True)
    slug = AutoSlugField(populate_from='name',unique=True)
    points = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='members', blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    dream1 = models.ImageField(upload_to="dreams",blank=True, null=True,default=None)
    dream2 = models.ImageField(upload_to="dreams",blank=True, null=True,default=None)
    status = models.TextField(blank=True, null=True)
    birthday = models.DateField(null=True)
    level = models.ForeignKey(Level,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __unicode__(self):
        return self.name

class MemberTraingStep(models.Model):
    member = models.ForeignKey(Member,related_name='training_steps')
    training_step = models.ForeignKey(TrainingStep,related_name='members')
    answer = models.TextField()

    class Meta:
        verbose_name = "MemberTraingStep"
        verbose_name_plural = "MemberTraingSteps"

    def __unicode__(self):
        return self.member.name+' - '+self.training_step.title

class Team(models.Model):
    owner = models.ForeignKey(Member,related_name="team_owner")
    member = models.ForeignKey(Member,related_name="team_member")
    position = models.IntegerField()

    class Meta:
        verbose_name = "Member Team"
        verbose_name_plural = "Member Teams"

    def __unicode__(self):
        return self.owner.name +" - "+ self.member.name

class Contact(models.Model):
    owner = models.ForeignKey(Member,related_name="contact_owner")
    member = models.ForeignKey(Member,related_name="contact_member", blank=True, null=True)
    avatar = models.ImageField(upload_to='contacts', blank=True, null=True)
    contact_category = models.IntegerField(choices=((0,'Contato'),(1,'Cliente')))
    gender = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    cellphone = models.CharField(max_length=45, blank=True, null=True)
    birthday = models.DateField(null=True)
    cpf = models.CharField(max_length=45, blank=True, null=True)
    rg = models.CharField(max_length=45, blank=True, null=True)
    postal_code = models.CharField(max_length=255)
    region = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __unicode__(self):
        return self.name

class Goal(models.Model):
    member = models.ForeignKey(Member)
    level = models.ForeignKey(Level)
    date = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __unicode__(self):
        return self.level.title+" - "+self.member.name

class LogMemberLogin(models.Model):
    member = models.ForeignKey(Member)
    ipv4_address = models.CharField(max_length=15, blank=True, null=True)
    ipv6_address = models.CharField(max_length=40, blank=True, null=True)
    agent = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Log Member Login"
        verbose_name_plural = "Log Member Logins"

    def __unicode__(self):
        return self.member.name

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    points = models.IntegerField(default=0)
    table_value = models.DecimalField(max_digits=11, decimal_places=2)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return self.name

class Sale(models.Model):
    member = models.ForeignKey(Member)
    client = models.ForeignKey(Contact)
    active = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=11, decimal_places=2,default="0.00")
    points = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    send_time = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __unicode__(self):
        return str(self.id)

class SaleItem(models.Model):
    product = models.ForeignKey(Product)
    sale = models.ForeignKey(Sale,related_name='sale_items')
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=11, decimal_places=2,default="0.00")
    notificate_at = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "SaleItem"
        verbose_name_plural = "SaleItems"

    def __unicode__(self):
        return str(self.id)
    
class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts')
    title = models.CharField(max_length=255)
    category = models.IntegerField()
    content = models.TextField(null=True,blank=True,default=None)
    media = models.FileField(upload_to="posts",null=True,blank=True,default=None)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.title
    
class Calendar(models.Model):
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User,null=True)
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"

    def __unicode__(self):
        return self.name
    
class Event(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    all_day = models.BooleanField(default=False)
    begin_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    invited = models.ManyToManyField(Contact,null=True,blank=True)
    members = models.ManyToManyField(Member,null=True,blank=True)
    calendar = models.ForeignKey(Calendar,related_name='events')
    note = models.TextField(null=True,blank=True)

    postal_code = models.ForeignKey(PostalCode,null=True,blank=True,default=None)
    number = models.CharField(max_length=255, blank=True, null=True)
    complement = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(null=True,blank=True,default=None)
    lng = models.FloatField(null=True,blank=True,default=None)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __unicode__(self):
        return self.title

class MediaType(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = "MediaType"
        verbose_name_plural = "MediaTypes"

    def __unicode__(self):
        return self.name
    
class MediaCategory(models.Model):
    media_type = models.ForeignKey(MediaType,related_name='categories')
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = "MediaCategory"
        verbose_name_plural = "MediaCategorys"

    def __unicode__(self):
        return self.name

class Media(models.Model):
    media_category = models.ForeignKey(MediaCategory,related_name='medias')
    name = models.CharField(max_length=255)
    media_type = models.IntegerField()
    media_file = models.FileField(upload_to="multimidida")
    
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medias"

    def __unicode__(self):
        return self.name
    

