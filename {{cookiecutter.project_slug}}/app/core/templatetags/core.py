from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

from core.feeds import BlogIndexFeedRSS, BlogIndexFeedAtom
from core.utils import wagtail_children_live_in_menu_all, wagtail_children_live_in_menu_top, TypekitException

register = template.Library()


# region Filters

@register.filter
def get_type(value):
    return type(value)


# endregion

# region Simple Tags

# endregion

# region Assignment Tags

@register.assignment_tag(takes_context=True)
def get_wagtail_all_menu_items(context, parent=None, caller=None):
    """
    Retrieves all menu items - all pages with In Menu flag turned on.

    :param context: used for automatic resolution ofcalling page and site's root page
    :param parent: the root page to start the search
    :param caller: the current active page being requested
    :return: dictionary tree with all pages in menu
    """
    call_page = caller if caller else context['page']
    root_page = parent if parent else context['request'].site.root_page
    return wagtail_children_live_in_menu_all(root_page, call_page)


@register.assignment_tag(takes_context=True)
def get_wagtail_top_menu_items(context, parent=None, caller=None):
    """
    Retrieves the top menu items - the immediate children of the parent page.

    :param context: used for automatic resolution ofcalling page and site's root page
    :param parent: the root page to start the search
    :param caller: the current active page being requested
    :return: dictionary tree with all pages in menu
    """
    call_page = caller if caller else context['page']
    root_page = parent if parent else context['request'].site.root_page
    return wagtail_children_live_in_menu_top(root_page, call_page)


@register.assignment_tag(takes_context=True)
def get_wagtail_root_page(context):
    """this returns a core.Page, not the implementation-specific model used
    so object-comparison to self will return false as objects would differ"""
    return context['request'].site.root_page


# endregion

# region Inclusion Tags

@register.inclusion_tag('core/includes/typekit.html')
def core_typekit(kit_id=None):
    if kit_id is None:
        try:
            kit_id = getattr(settings, "TYPEKIT_ID")
        except AttributeError:
            raise TypekitException("TYPEKIT_ID setting: not found")

        if kit_id is None:
            raise TypekitException("TYPEKIT_ID setting is set to None")

    return {id: kit_id}


@register.inclusion_tag('core/includes/shivs.html')
def core_shivs():
    return {}


@register.inclusion_tag('core/includes/feeds.html', takes_context=True)
def core_feeds(context):
    """
    Autodiscovery link elements for feeds used in the head tag.
    :param context:
    :return:
    """
    request = context['request']
    bi_rss = BlogIndexFeedRSS()
    bi_atm = BlogIndexFeedAtom()
    feeds = [
        {
            'type': bi_rss.feed_type.mime_type.split(';')[0],
            'title': bi_rss.title(bi_rss.get_object(request)),
            'url': request.build_absolute_uri(reverse('blog_rss')),
        },
        {
            'type': BlogIndexFeedAtom.feed_type.mime_type.split(';')[0],
            'title': bi_atm.title(bi_atm.get_object(request)),
            'url': request.build_absolute_uri(reverse('blog_atom')),
        },
    ]

    return {'feeds': feeds}

# endregion Inclusion Tags
