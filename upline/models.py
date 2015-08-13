from django.db import models
from django.contrib.auth.models import User

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
    media_url = models.CharField(max_length=255, blank=True, null=True)
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
    parent = models.ForeignKey('self', blank=True, null=True)
    external_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    points = models.IntegerField()
    avatar_url = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=100)
    dream = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    level = models.ForeignKey(Level)
    training_steps = models.ManyToManyField(TrainingStep)


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
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    postal_code = models.CharField(max_length=255)
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
