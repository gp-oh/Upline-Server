# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('upline', '0036_auto_20150903_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'not\xedcia', 'verbose_name_plural': 'not\xedcias'},
        ),
        migrations.RemoveField(
            model_name='member',
            name='slug',
        ),
        migrations.AlterField(
            model_name='calendar',
            name='public',
            field=models.BooleanField(default=False, verbose_name='p\xfablico'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='endere\xe7o', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(null=True, verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cellphone',
            field=models.CharField(max_length=45, null=True, verbose_name='celular', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_category',
            field=models.IntegerField(verbose_name='categoria do contato', choices=[(0, b'Contato'), (1, b'Cliente')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cpf',
            field=models.CharField(max_length=45, null=True, verbose_name='CPF', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.IntegerField(verbose_name='sexo', choices=[(0, b'Masculino'), (1, b'Feminino')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(related_name='contact_owner', verbose_name='dono', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=45, null=True, verbose_name='fone', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='region',
            field=models.CharField(max_length=255, null=True, verbose_name='regi\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='rg',
            field=models.CharField(max_length=45, null=True, verbose_name='RG', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(default=False, verbose_name='o dia inteiro'),
        ),
        migrations.AlterField(
            model_name='event',
            name='begin_time',
            field=models.DateTimeField(null=True, verbose_name='data de in\xedcio'),
        ),
        migrations.AlterField(
            model_name='event',
            name='complement',
            field=models.CharField(max_length=255, null=True, verbose_name='complemento', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='data final'),
        ),
        migrations.AlterField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(to='upline.Contact', verbose_name='convidados', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='lat',
            field=models.FloatField(default=None, null=True, verbose_name='latitude', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='lng',
            field=models.FloatField(default=None, null=True, verbose_name='longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='note',
            field=models.TextField(null=True, verbose_name='nota', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='number',
            field=models.CharField(max_length=255, null=True, verbose_name='n\xfamero', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(verbose_name='dono', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='t\xedtulo'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='date',
            field=models.DateTimeField(verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='level',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='level',
            name='description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='level',
            name='gift',
            field=models.TextField(null=True, verbose_name='presente'),
        ),
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(upload_to=b'levels', null=True, verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='level',
            name='points_range_from',
            field=models.IntegerField(verbose_name='pontua\xe7\xe3o inicial'),
        ),
        migrations.AlterField(
            model_name='level',
            name='points_range_to',
            field=models.IntegerField(verbose_name='pontua\xe7\xe3o final'),
        ),
        migrations.AlterField(
            model_name='level',
            name='title',
            field=models.CharField(unique=True, max_length=255, verbose_name='t\xedtulo'),
        ),
        migrations.AlterField(
            model_name='level',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='agent',
            field=models.CharField(max_length=255, null=True, verbose_name='navegador', blank=True),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='ipv4_address',
            field=models.CharField(max_length=15, null=True, verbose_name='endere\xe7o ipv4', blank=True),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='ipv6_address',
            field=models.CharField(max_length=40, null=True, verbose_name='edere\xe7o ipv6', blank=True),
        ),
        migrations.AlterField(
            model_name='logmemberlogin',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_category',
            field=models.ForeignKey(related_name='medias', verbose_name='categoria de midia', to='upline.MediaCategory'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_file',
            field=models.FileField(upload_to=b'multimidida', verbose_name='arquivo de midia'),
        ),
        migrations.AlterField(
            model_name='mediacategory',
            name='media_type',
            field=models.IntegerField(verbose_name='tipo de midia', choices=[(0, b'Imagem'), (1, b'Audio'), (2, b'Video')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='endere\xe7o', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True, verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='member',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='member',
            name='dream1',
            field=models.ImageField(default=None, upload_to=b'dreams', null=True, verbose_name='sonho 1', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dream2',
            field=models.ImageField(default=None, upload_to=b'dreams', null=True, verbose_name='sonho 2', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='external_id',
            field=models.IntegerField(unique=True, null=True, verbose_name='id externo', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.IntegerField(verbose_name='sexo', choices=[(0, b'Masculino'), (1, b'Feminino')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='outpooring',
            field=models.IntegerField(default=0, verbose_name='derramamento'),
        ),
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='downlines', verbose_name='pai', blank=True, to='upline.Member', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=45, null=True, verbose_name='fone', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='points',
            field=models.IntegerField(default=0, verbose_name='pontos'),
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_id',
            field=models.CharField(max_length=255, null=True, verbose_name='id do quickblox'),
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_login',
            field=models.CharField(max_length=255, null=True, verbose_name='login do quickblox'),
        ),
        migrations.AlterField(
            model_name='member',
            name='quickblox_password',
            field=models.CharField(max_length=255, null=True, verbose_name='senha do quickblox'),
        ),
        migrations.AlterField(
            model_name='member',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='membertraingstep',
            name='answer',
            field=models.TextField(verbose_name='resposta'),
        ),
        migrations.AlterField(
            model_name='membertraingstep',
            name='training_step',
            field=models.ForeignKey(related_name='members', verbose_name='etapa de treinamento', to='upline.TrainingStep'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=None, null=True, verbose_name='conte\xfado', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='t\xedtulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='aprovado'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='neighborhood',
            field=models.CharField(max_length=255, verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='street',
            field=models.CharField(max_length=255, verbose_name='rua'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='street_type',
            field=models.CharField(max_length=255, verbose_name='tipo de rua'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='product',
            name='points',
            field=models.IntegerField(default=0, verbose_name='pontos'),
        ),
        migrations.AlterField(
            model_name='product',
            name='table_value',
            field=models.DecimalField(verbose_name='valor de tabela', max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='client',
            field=models.ForeignKey(verbose_name='cliente', to='upline.Contact'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='points',
            field=models.IntegerField(default=0, verbose_name='pontos'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='send_time',
            field=models.DateTimeField(null=True, verbose_name='data de envio'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='enviado'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='notificate_at',
            field=models.DateField(verbose_name='notificar em'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='notified',
            field=models.BooleanField(default=False, verbose_name='notificado'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='quantidade'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='state',
            name='acronym',
            field=models.CharField(max_length=2, verbose_name='sigla'),
        ),
        migrations.AlterField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(related_name='team_owner', verbose_name='dono', to='upline.Member'),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.IntegerField(verbose_name='posi\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='training',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='training',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='answer_type',
            field=models.IntegerField(verbose_name='tipo de resposta'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_14_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 14', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_1_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 1', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_28_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 28', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_2_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 2', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_3_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 3', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_4_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 4', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_5_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 5', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_6_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 6', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='day_7_notification_description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o da notifica\xe7\xe3o do dia 7', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='description',
            field=models.TextField(null=True, verbose_name='descri\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='meetings_per_week',
            field=models.IntegerField(verbose_name='reuni\xf5es por semana'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='need_answer',
            field=models.BooleanField(default=False, verbose_name='necessita resposta'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='nr_contacts',
            field=models.IntegerField(verbose_name='n\xfamero de contatos'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='step',
            field=models.IntegerField(verbose_name='etapa'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='title',
            field=models.CharField(max_length=255, verbose_name='t\xedtulo'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='data de altera\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='trainingstep',
            name='weeks',
            field=models.IntegerField(verbose_name='semanas'),
        ),
    ]
