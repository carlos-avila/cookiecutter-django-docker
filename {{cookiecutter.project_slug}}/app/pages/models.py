import six
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, PageBase
from wagtail.wagtailsearch import index
from wagtailmetadata.models import MetadataPageMixin

from core.blocks import BodyStreamBlock


class HomePage(six.with_metaclass(PageBase, MetadataPageMixin, Page)):
    parent_page_types = ['wagtailcore.Page']

    @classmethod
    def can_create_at(cls, parent):
        # You can only create one of these!
        return super(HomePage, cls).can_create_at(parent) and not cls.objects.exists()


class FlatPage(six.with_metaclass(PageBase, MetadataPageMixin, Page)):
    parent_page_types = ['pages.HomePage']
    subpage_types = []

    body = StreamField(BodyStreamBlock())

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + MetadataPageMixin.panels
