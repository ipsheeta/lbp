
from django.utils.translation import ugettext_lazy as _
from feincms.content.medialibrary.v2 import MediaFileContent
from feincms.module.medialibrary.models import MediaFile

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.application.models import ApplicationContent
from feincms.content.video.models import VideoContent
from elephantblog.models import Entry
from elephantblog.navigation_extensions import treeinfo
from feincms.utils.html.cleanse import cleanse_html
from pennyblack.content.richtext import TextOnlyNewsletterContent, TextWithImageNewsletterContent
from pennyblack.models import Newsletter

### PAGES ###

Page.register_extensions('feincms.module.extensions.datepublisher',
                         'feincms.module.extensions.seo',
                         'feincms.module.page.extensions.navigation',
                         'feincms.module.page.extensions.titles',
                         'feincms.module.extensions.changedate',)

Page.register_templates({
    'title': 'Home Page',
    'path': 'home_hero.html',
    'regions': (
        ('banner', 'Banner'),
        ('main', 'Main'),
        ('sidebar', 'Sidebar'),
    ),
    },
    {
        'title': 'Internal Page',
        'path': 'internal.html',
        'regions':(
            ('main', 'Main'),
            )
    },
    {
    'title': 'About Page',
    'path': 'about.html',
    'regions':(
        ('banner', 'Banner'),
        ('about', 'About'),
        ('staff', 'Staff'),
        ('advisory_committee', 'Advisory Committee'),
        ('local_success', 'Local Success'),
        ('working_with', 'Partners'),
        ('newsletters', 'Newsletters'),
        )
    })

Page.create_content_type(RichTextContent)
Page.create_content_type(MediaFileContent, TYPE_CHOICES = (('lightbox', 'Lightbox'),
                                                           ('block','Block Image')))
Page.create_content_type(ApplicationContent, APPLICATIONS= (
        ('elephantblog.urls', 'Blog'),
        ('pagemaker.forms_urls', 'Forms'),
    ))

### BLOG ENTRIES ###

Entry.register_extensions(#'feincms.module.extensions.datepublisher',
                          'elephantblog.extensions.blogping',
                          'elephantblog.extensions.tags',)
Entry.register_regions(
    ('main', _('Main content area')),
    ('featured', _('Featured Image')),
    ('teaser', _('Teaser')),
)
Entry.create_content_type(RichTextContent, cleanse=cleanse_html, regions=('main','teaser'))
Entry.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
    ))
Entry.create_content_type(VideoContent, regions=('main', 'teaser'))

### NEWSLETTERS ###

Newsletter.register_templates({
    'key': 'base',
    'title': 'Youth Seed Newsletter',
    'path': 'youthseed/ys-newsletter.html',
    'regions': (
        ('main', 'Main Region'),
    )
})

Newsletter.create_content_type(TextOnlyNewsletterContent)
Newsletter.create_content_type(TextWithImageNewsletterContent)

### CUSTOM ###

from django.db import models
from django import forms
from django.template.loader import render_to_string

class CarouselContent(models.Model):
    images = models.ManyToManyField(MediaFile)

    def __unicode__(self):
        # ToDo: (mo) NOt sure what the return value should be for this.
        return ("The MediaFile returns various images by their file/caption name")

    class Meta:
        abstract = True

    @property
    def media(self):
        return forms.Media(
            css={'all': ('css/carousel.css',),},
            # Jquery is a dependency
            js=('js/jquery.js', 'js/carousel_config.js',),
            )

    def render(self, **kwargs):
        return render_to_string('carousel.html', {
            'carousel': self,
        })

Page.create_content_type(CarouselContent)


class EventContent(models.Model):
    title = models.CharField(blank=False, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/events')
    description = models.TextField(blank=False)
    date = models.DateTimeField(blank=False)
    location = models.CharField(max_length=200, blank=False)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return ("A reusable Event widget")

    class Meta:
        abstract = True

    def render_sidebar(self, **kwargs):
        return render_to_string('snippet_event_sidebar.html', {
            'event': self,
            })
    def render_main(self, **kwargs):
        return render_to_string('snippet_event_main.html', {
            'event': self,
            })

Page.create_content_type(EventContent)


class PersonContent(models.Model):
    name = models.CharField(blank=False, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/people')
    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=False)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return ("A reusable person contentType")

    class Meta:
        abstract = True

    def render(self, **kwargs):
        return render_to_string('snippet_person.html', {
            'person': self,
            })

Page.create_content_type(PersonContent)
