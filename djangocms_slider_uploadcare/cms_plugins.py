# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import UploadcareSlide, UploadcareSlider


class UploadcareSlidePlugin(CMSPluginBase):
    model = UploadcareSlide
    module = _("Slider")
    name = _("Slide")
    render_template = 'djangocms_slider/slide.html'

plugin_pool.register_plugin(UploadcareSlidePlugin)


class UploadcareSliderPlugin(CMSPluginBase):
    model = UploadcareSlider
    name = _('Slider')
    module = _("Slideshow")
    render_template = 'djangocms_slider/slider.html'
    allow_children = True
    child_classes = ["UploadcareSlidePlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(UploadcareSliderPlugin)
