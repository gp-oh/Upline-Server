 # -*- coding: utf-8 -*-
import os

from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.conf import settings


class S3DirectWidget(widgets.TextInput):

    html = (
        u'<div class="s3direct" data-policy-url="{policy_url}">'
        u'  <a class="file-link" target="_blank" href="{file_url}">{file_name}</a>'
        u'  <a class="file-remove" href="#remove">Remove</a>'
        u'  <input class="file-url" type="hidden" value="{file_url}" id="{element_id}" name="{name}" />'
        u'  <input class="file-dest" type="hidden" value="{dest}">'
        u'  <input class="file-input" type="file" />'
        u'  <div class="progress progress-striped active">'
        u'    <div class="bar"></div>'
        u'  </div>'
        u'</div>'
    )

    class Media:
        js = (
            's3direct/js/scripts.js',
        )
        css = {
            'all': (
                's3direct/css/bootstrap-progress.min.css',
                's3direct/css/styles.css',
            )
        }

    def __init__(self, *args, **kwargs):
        self.dest = kwargs.pop('dest', None)
        super(S3DirectWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        output = self.html.format(
            policy_url=reverse('s3direct'),
            element_id=self.build_attrs(attrs).get('id'),
            file_name=os.path.basename(value or ''),
            dest=self.dest,
            file_url=unicode(value) or '',
            name=unicode(name))

        return mark_safe(output)
