from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

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
    training = models.ForeignKey(Training)
    title = models.CharField(max_length=255)
    media = models.FileField(upload_to="training_steps",blank=True, null=True)
    step = models.IntegerField()
    description = models.TextField(blank=True, null=True)
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
    slug = AutoSlugField(populate_from='name',unique=True)
    points = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='members', blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    dream = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    birthday = models.DateField(null=True)
    level = models.ForeignKey(Level,null=True)
    training_steps = models.ManyToManyField(TrainingStep,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __unicode__(self):
        return self.name

class Team(models.Model):
    owner = models.ForeignKey(Member,related_name="team_owner")
    member = models.ForeignKey(Member,related_name="team_member")
    position = models.IntegerField()

    class Meta:
        verbose_name = "Member Team"
        verbose_name_plural = "Member Teams"

    def __unicode__(self):
        return self.owner.name +" - "+ self.member.name

class ContactCategory(models.Model):
    title = models.CharField(unique=True, max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Category"
        verbose_name_plural = "Contact Categorys"

    def __unicode__(self):
        return self.title

class Contact(models.Model):
    owner = models.ForeignKey(Member,related_name="contact_owner")
    member = models.ForeignKey(Member,related_name="contact_member", blank=True, null=True)
    contact_category = models.ForeignKey(ContactCategory)
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


class DistributionCenter(models.Model):
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "DistributionCenter"
        verbose_name_plural = "DistributionCenters"

    def __unicode__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    reference_value = models.DecimalField(max_digits=11, decimal_places=2)
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
    total = models.DecimalField(max_digits=11, decimal_places=2)
    points = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __unicode__(self):
        return str(self.id)

class SaleItem(models.Model):
    product = models.ForeignKey(Product)
    sale = models.ForeignKey(Sale,related_name='sale_items')
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=11, decimal_places=2)
    delivery_prevision = models.DateField()
    notificate_at = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "SaleItem"
        verbose_name_plural = "SaleItems"

    def __unicode__(self):
        return str(self.id)
    
    

