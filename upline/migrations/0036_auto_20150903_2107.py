# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
# import autoslug.fields
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0035_member_outpooring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='public',
            field=models.BooleanField(default=False, verbose_name='public'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='user',
            field=models.ForeignKey(verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(verbose_name='estado', to='upline.State'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='address', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(upload_to=b'contacts', null=True, verbose_name='avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(null=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cellphone',
            field=models.CharField(max_length=45, null=True, verbose_name='cellphone', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='cidade', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_category',
            field=models.IntegerField(verbose_name='contact_category', choices=[(0, b'Contato'), (1, b'Cliente')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cpf',
            field=models.CharField(max_length=45, null=True, verbose_name='cpf', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=255, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.IntegerField(verbose_name='gender', choices=[(0, b'Masculino'), (1, b'Feminino')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='member',
            field=models.ForeignKey(related_name='contact_member', verbose_name='membro', blank=True, to='upline.Member', null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(related_name='contact_owner', verbose_name='owner', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=45, null=True, verbose_name='phone', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='postal_code',
            field=models.CharField(max_length=255, verbose_name='postal_code'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='region',
            field=models.CharField(max_length=255, null=True, verbose_name='region', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='rg',
            field=models.CharField(max_length=45, null=True, verbose_name='rg', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=255, null=True, verbose_name='estado', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(default=False, verbose_name='all_day'),
        ),
        migrations.AlterField(
            model_name='event',
            name='begin_time',
            field=models.DateTimeField(null=True, verbose_name='begin_time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='calendar',
            field=models.ForeignKey(related_name='events', verbose_name='calend\xe1rio', to='upline.Calendar'),
        ),
        migrations.AlterField(
            model_name='event',
            name='complement',
            field=models.CharField(max_length=255, null=True, verbose_name='complement', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='end_time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(to='upline.Contact', verbose_name='invited', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='lat',
            field=models.FloatField(default=None, null=True, verbose_name='lat', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='lng',
            field=models.FloatField(default=None, null=True, verbose_name='lng', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='upline.Member', verbose_name='membros', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='note',
            field=models.TextField(null=True, verbose_name='note', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='number',
            field=models.CharField(max_length=255, null=True, verbose_name='number', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='postal_code',
            field=models.ForeignKey(default=None, blank=True, to='upline.PostalCode', null=True, verbose_name='postal_code'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='level',
            field=models.ForeignKey(verbose_name='n\xedvel', to='upline.Level'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='member',
            field=models.ForeignKey(verbose_name='membro', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='level',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='level',
            name='description',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='level',
            name='gift',
            field=models.TextField(null=True, verbose_name='gift'),
        ),
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(upload_to=b'levels', null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='level',
            name='points_range_from',
            field=models.IntegerField(verbose_name='points_range_from'),
        ),
        migrations.AlterField(
            model_name='level',
            name='points_range_to',
            field=models.IntegerField(verbose_name='points_range_to'),
        ),
        migrations.AlterField(
            model_name='level',
            name='title',
            field=models.CharField(unique=True, max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='level',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='agent',
            field=models.CharField(max_length=255, null=True, verbose_name='agent', blank=True),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='ipv4_address',
            field=models.CharField(max_length=15, null=True, verbose_name='ipv4_address', blank=True),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='ipv6_address',
            field=models.CharField(max_length=40, null=True, verbose_name='ipv6_address', blank=True),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='member',
            field=models.ForeignKey(verbose_name='membro', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_category',
            field=models.ForeignKey(related_name='medias', verbose_name='media_category', to='upline.MediaCategory'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_file',
            field=models.FileField(upload_to=b'multimidida', verbose_name='media_file'),
        ),
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='mediacategory',
            name='media_type',
            field=models.IntegerField(verbose_name='media_type', choices=[(0, b'Imagem'), (1, b'Audio'), (2, b'Video')]),
        ),
        migrations.AlterField(
            model_name='mediacategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='address', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(upload_to=b'members', null=True, verbose_name='avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='cidade', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='member',
            name='dream1',
            field=models.ImageField(default=None, upload_to=b'dreams', null=True, verbose_name='dream1', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dream2',
            field=models.ImageField(default=None, upload_to=b'dreams', null=True, verbose_name='dream2', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='external_id',
            field=models.IntegerField(unique=True, null=True, verbose_name='external_id', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.IntegerField(verbose_name='gender', choices=[(0, b'Masculino'), (1, b'Feminino')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='level',
            field=models.ForeignKey(verbose_name='n\xedvel', to='upline.Level', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='member',
            name='outpooring',
            field=models.IntegerField(default=0, verbose_name='outpooring'),
        ),
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='downlines', verbose_name='parent', blank=True, to='upline.Member', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=45, null=True, verbose_name='phone', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='points',
            field=models.IntegerField(default=0, verbose_name='points'),
        ),
        migrations.AlterField(
            model_name='member',
            name='postal_code',
            field=models.CharField(max_length=255, verbose_name='postal_code'),
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_id',
            field=models.CharField(max_length=255, null=True, verbose_name='quickblox_id'),
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_login',
            field=models.CharField(max_length=255, null=True, verbose_name='quickblox_login'),
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_password',
            field=models.CharField(max_length=255, null=True, verbose_name='quickblox_password'),
        ),
        # migrations.AlterField(
        #     model_name='member',
        #     name='slug',
        #     field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='slug'),
        # ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(max_length=255, null=True, verbose_name='estado', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.TextField(null=True, verbose_name='status', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='membertraingstep',
            name='answer',
            field=models.TextField(verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='membertraingstep',
            name='member',
            field=models.ForeignKey(related_name='training_steps', verbose_name='membro', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='membertraingstep',
            name='training_step',
            field=models.ForeignKey(related_name='members', verbose_name='training_step', to='upline.TrainingStep'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=None, null=True, verbose_name='content', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='post',
            name='level',
            field=models.ForeignKey(verbose_name='n\xedvel', to='upline.Level'),
        ),
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.FileField(default=None, upload_to=b'posts', null=True, verbose_name='midia', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(related_name='posts', verbose_name='usu\xe1rio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='approved'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='city',
            field=models.ForeignKey(verbose_name='cidade', to='upline.City'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='neighborhood',
            field=models.CharField(max_length=255, verbose_name='neighborhood'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='postal_code',
            field=models.CharField(max_length=255, verbose_name='postal_code'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='street',
            field=models.CharField(max_length=255, verbose_name='street'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='street_type',
            field=models.CharField(max_length=255, verbose_name='street_type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='product',
            name='points',
            field=models.IntegerField(default=0, verbose_name='points'),
        ),
        migrations.AlterField(
            model_name='product',
            name='table_value',
            field=models.DecimalField(verbose_name='table_value', max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='client',
            field=models.ForeignKey(verbose_name='client', to='upline.Contact'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='member',
            field=models.ForeignKey(verbose_name='membro', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='paid'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='points',
            field=models.IntegerField(default=0, verbose_name='points'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='send_time',
            field=models.DateTimeField(null=True, verbose_name='send_time'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='sent'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total',
            field=models.DecimalField(default=b'0.00', verbose_name='total', max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sale',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='notificate_at',
            field=models.DateField(verbose_name='notificate_at'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='notified',
            field=models.BooleanField(default=False, verbose_name='notified'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(verbose_name='produto', to='upline.Product'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='sale',
            field=models.ForeignKey(related_name='sale_items', verbose_name='venda', to='upline.Sale'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='total',
            field=models.DecimalField(default=b'0.00', verbose_name='total', max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='state',
            name='acronym',
            field=models.CharField(max_length=2, verbose_name='acronym'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='team',
            name='member',
            field=models.ForeignKey(related_name='team_member', verbose_name='membro', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(related_name='team_owner', verbose_name='owner', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.IntegerField(verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='training',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='training',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='training',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='answer_type',
            field=models.IntegerField(verbose_name='answer_type'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_14_notification_description',
            field=models.TextField(null=True, verbose_name='day_14_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_1_notification_description',
            field=models.TextField(null=True, verbose_name='day_1_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_28_notification_description',
            field=models.TextField(null=True, verbose_name='day_28_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_2_notification_description',
            field=models.TextField(null=True, verbose_name='day_2_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_3_notification_description',
            field=models.TextField(null=True, verbose_name='day_3_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_4_notification_description',
            field=models.TextField(null=True, verbose_name='day_4_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_5_notification_description',
            field=models.TextField(null=True, verbose_name='day_5_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_6_notification_description',
            field=models.TextField(null=True, verbose_name='day_6_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_7_notification_description',
            field=models.TextField(null=True, verbose_name='day_7_notification_description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='media',
            field=models.FileField(upload_to=b'training_steps', null=True, verbose_name='midia', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='meetings_per_week',
            field=models.IntegerField(verbose_name='meetings_per_week'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='need_answer',
            field=models.BooleanField(default=False, verbose_name='need_answer'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='nr_contacts',
            field=models.IntegerField(verbose_name='nr_contacts'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='step',
            field=models.IntegerField(verbose_name='step'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='training',
            field=models.ForeignKey(related_name='training_steps', verbose_name='treinamento', to='upline.Training'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update_time'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='weeks',
            field=models.IntegerField(verbose_name='weeks'),
        ),
    ]
