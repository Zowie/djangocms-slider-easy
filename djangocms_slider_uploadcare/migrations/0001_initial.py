# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadcareSlide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='djangocms_slider_uploadcare_uploadcareslide', parent_link=True, to='cms.CMSPlugin')),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('url', models.CharField(verbose_name='link', max_length=255, blank=True, null=True, help_text='If present, clicking on image will take user to link.')),
                ('caption', models.TextField(verbose_name='caption', max_length=255, blank=True, null=True, help_text='Specifies text that occurs on the slide.')),
                ('page_link', models.ForeignKey(verbose_name='page', blank=True, null=True, help_text='If present, clicking on image will take user to specified page.', to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='UploadcareSlider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='djangocms_slider_uploadcare_uploadcareslider', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
