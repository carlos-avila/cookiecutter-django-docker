from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailsnippets.models import register_snippet
from wobbly.blocks import FOOTER_BLOCKS, HEADER_BLOCKS


# region Snippets

@register_snippet
class Header(models.Model):
    name = models.CharField(max_length=256)
    contents = StreamField(HEADER_BLOCKS)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('contents')
    ]

    def __str__(self):
        return self.name


@register_snippet
class Footer(models.Model):
    name = models.CharField(max_length=256)
    contents = StreamField(FOOTER_BLOCKS)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('contents'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class SocialNetwork(models.Model):
    name = models.CharField('Name', max_length=256, default='Facebook')
    style = models.CharField('Class', max_length=256, default='social-facebook')
    url = models.URLField('URL', max_length=256, default='http://facebook.com')

    panels = [
        FieldPanel('name', classname='title'),
        FieldPanel('style'),
        FieldPanel('url'),
    ]

    def __str__(self):
        return self.name


# endregion

# region Settings

@register_setting(icon='view')
class DesignSettings(BaseSetting):
    header = models.ForeignKey(
        'core.Header',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    footer = models.ForeignKey(
        'core.Footer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        MultiFieldPanel([
            SnippetChooserPanel('header'),
            SnippetChooserPanel('footer'),
        ], heading='Template'),
        MultiFieldPanel([

        ], heading='Style'),
    ]

    class Meta:
        verbose_name = 'Design'

# endregion
